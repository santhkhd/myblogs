"""
GitHub Actions Cloud Auto-Poster Script
Runs automatically in GitHub Actions on a daily cron schedule.
Fetches latest government jobs and posts them to Blogger without requiring your local PC.
"""

import os
import sys
import smtplib
import socket
import ssl
import time

# Force IPv4 socket resolution for GitHub Actions cloud runners
# (Gmail SMTP servers drop IPv6 connections from cloud runner IP ranges)
_orig_getaddrinfo = socket.getaddrinfo
def _ipv4_getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
    return _orig_getaddrinfo(host, port, socket.AF_INET, type, proto, flags)
socket.getaddrinfo = _ipv4_getaddrinfo

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Ensure UTF-8 output in logs
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

from job_fetcher import fetch_new_jobs, generate_daily_50_jobs
from job_formatter import format_job_html
from job_publisher import generate_blogger_xml

# GitHub Secrets / Environment Variables
BLOGGER_EMAIL = os.environ.get("BLOGGER_POST_EMAIL", "").strip()
SENDER_GMAIL = os.environ.get("SENDER_GMAIL", "").strip()
SENDER_PASSWORD = os.environ.get("SENDER_GMAIL_APP_PASSWORD", "").replace(" ", "").replace('"', '').replace("'", "").strip()

def mask_email(email):
    if "@" in email:
        name, domain = email.split("@", 1)
        masked_name = name[:2] + "***" if len(name) > 2 else name + "***"
        return f"{masked_name}@{domain}"
    return "***"

def get_authenticated_smtp():
    """
    Establishes an authenticated connection to Gmail SMTP via IPv4 with step-by-step diagnostics.
    """
    if not (BLOGGER_EMAIL and SENDER_GMAIL and SENDER_PASSWORD):
        print("ℹ️ Skipping email dispatch: Required GitHub Secrets (BLOGGER_POST_EMAIL, SENDER_GMAIL, SENDER_GMAIL_APP_PASSWORD) not fully configured.")
        return None

    print(f"📧 SENDER_GMAIL: {mask_email(SENDER_GMAIL)}")
    print(f"🎯 BLOGGER_EMAIL: {mask_email(BLOGGER_EMAIL)}")
    print(f"🔑 SENDER_GMAIL_APP_PASSWORD length: {len(SENDER_PASSWORD)} characters")

    ssl_context = ssl.create_default_context()

    # --- Strategy 1: Port 587 STARTTLS ---
    for host in ["smtp.gmail.com", "smtp.googlemail.com"]:
        print(f"\n🔌 Attempting connection to {host}:587 (STARTTLS)...")
        try:
            server = smtplib.SMTP(host, 587, timeout=30)
            server.set_debuglevel(1)
            print(f"   [1/4] Socket connected to {host}:587. Sending EHLO...")
            server.ehlo()
            print("   [2/4] Negotiating STARTTLS...")
            server.starttls(context=ssl_context)
            server.ehlo()
            print(f"   [3/4] Authenticating with Gmail App Password...")
            server.login(SENDER_GMAIL, SENDER_PASSWORD)
            print("   [4/4] ✅ Authentication successful! Gmail SMTP session established.")
            return server
        except Exception as e:
            print(f"   ❌ Failed on {host}:587 -> {type(e).__name__}: {e}")

    # --- Strategy 2: Port 465 SSL ---
    for host in ["smtp.gmail.com", "smtp.googlemail.com"]:
        print(f"\n🔌 Attempting connection to {host}:465 (Direct SSL)...")
        try:
            server = smtplib.SMTP_SSL(host, 465, context=ssl_context, timeout=30)
            server.set_debuglevel(1)
            print(f"   [1/3] SSL Socket connected to {host}:465. Sending EHLO...")
            server.ehlo()
            print(f"   [2/3] Authenticating with Gmail App Password...")
            server.login(SENDER_GMAIL, SENDER_PASSWORD)
            print("   [3/3] ✅ Authentication successful! Gmail SMTP session established.")
            return server
        except Exception as e:
            print(f"   ❌ Failed on {host}:465 -> {type(e).__name__}: {e}")

    print("\n❌ Could not connect or authenticate to Gmail SMTP across all endpoints.")
    print("💡 Troubleshooting Tips:")
    print("   1. Verify your App Password at: https://myaccount.google.com/apppasswords")
    print("   2. Ensure 2-Step Verification is active on your Google Account.")
    print("   3. Check your Gmail inbox for any Google 'Security alert / Sign-in attempt blocked' notifications.")
    return None

def build_job_email(job):
    tags = ", ".join([f"#{lbl}" for lbl in job.get("labels", ["Govt Jobs"])])
    subject = f"{job['title']} {tags}"
    body_html = format_job_html(job)
    plain_text = f"{job['title']}\n\nAuthority: {job['org_name']}\nPost: {job['post_name']}\nVacancies: {job['vacancies']}\nSalary: {job['salary']}\nQualification: {job['qualification']}\nApply Online: {job['apply_url']}\nOfficial Website: {job['website']}"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = SENDER_GMAIL
    msg["To"] = BLOGGER_EMAIL
    
    # Attach plain text first, then HTML (RFC compliant for 0 spam score)
    msg.attach(MIMEText(plain_text, "plain", "utf-8"))
    msg.attach(MIMEText(body_html, "html", "utf-8"))
    return msg

def main():
    print("="*60)
    print("🚀 GitHub Actions Daily Job Bot Execution Started...")
    print("="*60)

    # 1. Fetch live fresh jobs (deduplicated against history)
    new_jobs, all_jobs = fetch_new_jobs(limit=50)
    jobs_to_post = new_jobs if new_jobs else all_jobs
    jobs_to_post = jobs_to_post[:50]

    print(f"📋 Total fresh jobs to publish in this run: {len(jobs_to_post)}")

    # 2. Connect to Gmail SMTP
    server = get_authenticated_smtp()
    published_count = 0

    if server:
        for idx, job in enumerate(jobs_to_post, 1):
            try:
                msg = build_job_email(job)
                server.sendmail(SENDER_GMAIL, BLOGGER_EMAIL, msg.as_string())
                print(f"[{idx}/{len(jobs_to_post)}] ✅ Published: {job['title'][:60]}...")
                published_count += 1
                time.sleep(3.5)  # Safe 3.5s anti-spam delay between dispatches
            except Exception as e:
                print(f"[{idx}/{len(jobs_to_post)}] ⚠️ Retrying connection on error: {e}")
                try:
                    server = get_authenticated_smtp()
                    if server:
                        msg = build_job_email(job)
                        server.sendmail(SENDER_GMAIL, BLOGGER_EMAIL, msg.as_string())
                        print(f"[{idx}/{len(jobs_to_post)}] ✅ Published on retry: {job['title'][:60]}...")
                        published_count += 1
                except Exception as retry_err:
                    print(f"[{idx}/{len(jobs_to_post)}] ❌ Error sending job: {retry_err}")

        try:
            server.quit()
        except Exception:
            pass

    # 3. Always generate fresh XML backup
    xml_file = generate_blogger_xml(jobs_to_post, "daily_jobs_export.xml")
    print(f"📦 Generated updated XML: {xml_file}")
    print("="*60)
    print(f"🎉 Completed! Published: {published_count}/{len(jobs_to_post)} jobs.")
    print("="*60)

if __name__ == "__main__":
    main()
