"""
GitHub Actions Cloud Auto-Poster Script
Runs automatically in GitHub Actions on a daily cron schedule.
Fetches latest government jobs and posts them to Blogger without requiring your local PC.
"""

import os
import sys
import smtplib
import time

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
SENDER_PASSWORD = os.environ.get("SENDER_GMAIL_APP_PASSWORD", "").replace(" ", "").strip()

def get_authenticated_smtp():
    """
    Establishes an authenticated connection to Gmail SMTP.
    Uses Port 587 with STARTTLS (Preferred for Cloud Runners like GitHub Actions),
    with automatic fallback to Port 465 SSL.
    """
    if not (BLOGGER_EMAIL and SENDER_GMAIL and SENDER_PASSWORD):
        print("ℹ️ Skipping email dispatch: GitHub Secrets BLOGGER_POST_EMAIL / SENDER_GMAIL not set.")
        return None

    # Method 1: Port 587 with STARTTLS (Industry standard for cloud runners)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=30)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(SENDER_GMAIL, SENDER_PASSWORD)
        return server
    except Exception as e587:
        # Method 2: Fallback to Port 465 SSL
        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30)
            server.login(SENDER_GMAIL, SENDER_PASSWORD)
            return server
        except Exception as e465:
            print(f"❌ SMTP Connection Error: Port 587 ({e587}), Port 465 ({e465})")
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
