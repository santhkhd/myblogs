import os
import sys

# Ensure UTF-8 output in Windows PowerShell / CMD immediately
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Import 50 jobs definition
from build_50_genuine_jobs import JOBS_50, render_post_html

# Configuration
BLOGGER_POST_EMAIL = "santhkhd.jobs2026@blogger.com"
SENDER_GMAIL = "santhkhd@gmail.com"
SENDER_APP_PASSWORD = "irnknhbefumqeonq"

def post_all_jobs(sender_email=None, sender_password=None, delay_seconds=2):
    gmail_user = sender_email or SENDER_GMAIL
    gmail_pass = sender_password or SENDER_APP_PASSWORD

    if gmail_user == "your_email@gmail.com" or gmail_pass == "your_app_password":
        print("="*60)
        print("⚠️ ACTION REQUIRED:")
        print("Please enter your Gmail and 16-letter App Password to start publishing.")
        print("1. Go to: https://myaccount.google.com/apppasswords")
        print("2. Create an App password named 'BloggerBot'")
        print("="*60)
        try:
            gmail_user = input("Enter your Gmail address (e.g. yourname@gmail.com): ").strip()
            gmail_pass = input("Enter your 16-letter Gmail App Password: ").strip().replace(" ", "")
        except EOFError:
            print("Non-interactive mode: Please set SENDER_GMAIL and SENDER_APP_PASSWORD environment variables or edit this file.")
            return

    if not gmail_user or not gmail_pass:
        print("❌ Gmail credentials are required to send emails.")
        return

    print("Connecting to Gmail SMTP (smtp.gmail.com:465)...", flush=True)
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(gmail_user, gmail_pass)
        print(f"[SUCCESS] Connected & Authenticated as {gmail_user}!", flush=True)
    except Exception as e:
        print(f"[ERROR] Failed to connect to Gmail: {e}", flush=True)
        return

    print(f"Starting bulk publication of {len(JOBS_50)} genuine jobs to: {BLOGGER_POST_EMAIL}", flush=True)
    print("="*60, flush=True)

    success_count = 0
    fail_count = 0

    for idx, job in enumerate(JOBS_50, 1):
        # Format labels into Blogger hashtags in subject line
        tags_str = ", ".join([f"#{lbl}" for lbl in job.get("labels", ["Govt Jobs"])])
        subject = f"{job['title']} {tags_str}"
        body_html = render_post_html(job)

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = gmail_user
        msg["To"] = BLOGGER_POST_EMAIL
        msg.attach(MIMEText(body_html, "html", "utf-8"))

        try:
            server.sendmail(gmail_user, BLOGGER_POST_EMAIL, msg.as_string())
            print(f"[{idx}/{len(JOBS_50)}] [OK] Published: {job['title'][:65]}...", flush=True)
            success_count += 1
        except Exception as e:
            print(f"[{idx}/{len(JOBS_50)}] [FAIL] Error: {e}", flush=True)
            fail_count += 1
            # Reconnect if connection dropped
            try:
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.login(gmail_user, gmail_pass)
            except Exception:
                pass

        if idx < len(JOBS_50):
            time.sleep(delay_seconds)

    try:
        server.quit()
    except Exception:
        pass

    print("\n" + "="*60, flush=True)
    print(f"[COMPLETED] Successfully published: {success_count}/{len(JOBS_50)} jobs.", flush=True)
    if fail_count > 0:
        print(f"[WARNING] Failed: {fail_count} jobs.", flush=True)
    print(f"Visit your blog to see all published jobs with categories and apply buttons!", flush=True)
    print("="*60, flush=True)

if __name__ == "__main__":
    post_all_jobs()
