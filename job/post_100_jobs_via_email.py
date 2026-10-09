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

# Import 150 jobs definition
from build_150_latest_jobs import JOBS_150 as JOBS_100, render_post_html

# Configuration
BLOGGER_POST_EMAIL = "santhkhd.jobs2026@blogger.com"
SENDER_GMAIL = "santhkhd@gmail.com"
SENDER_APP_PASSWORD = "irnknhbefumqeonq"

def post_all_100_jobs(sender_email=None, sender_password=None, delay_seconds=1.2):
    gmail_user = sender_email or SENDER_GMAIL
    gmail_pass = sender_password or SENDER_APP_PASSWORD

    print("Connecting to Gmail SMTP (smtp.gmail.com:465)...", flush=True)
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=20)
        server.login(gmail_user, gmail_pass)
        print(f"[SUCCESS] Connected & Authenticated as {gmail_user}!", flush=True)
    except Exception as e:
        print(f"[ERROR] Failed to connect to Gmail: {e}", flush=True)
        return

    print(f"Starting bulk publication of {len(JOBS_100)} genuine 2026 jobs to: {BLOGGER_POST_EMAIL}", flush=True)
    print("="*60, flush=True)

    success_count = 0
    fail_count = 0

    for idx, job in enumerate(JOBS_100, 1):
        # Clean subject line
        subject = job['title']
        body_html = render_post_html(job)

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = gmail_user
        msg["To"] = BLOGGER_POST_EMAIL
        msg.attach(MIMEText(body_html, "html", "utf-8"))

        try:
            server.sendmail(gmail_user, BLOGGER_POST_EMAIL, msg.as_string())
            print(f"[{idx}/{len(JOBS_100)}] [OK] Published: {job['title'][:65]}...", flush=True)
            success_count += 1
        except Exception as e:
            print(f"[{idx}/{len(JOBS_100)}] [FAIL] Error: {e}", flush=True)
            fail_count += 1
            # Reconnect if connection dropped
            try:
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.login(gmail_user, gmail_pass)
            except Exception:
                pass

        if idx < len(JOBS_100):
            time.sleep(delay_seconds)

    try:
        server.quit()
    except Exception:
        pass

    print("\n" + "="*60, flush=True)
    print(f"[COMPLETED] Successfully published: {success_count}/{len(JOBS_100)} jobs.", flush=True)
    if fail_count > 0:
        print(f"[WARNING] Failed: {fail_count} jobs.", flush=True)
    print("Visit your blog to see all 100 published jobs!", flush=True)
    print("="*60, flush=True)

if __name__ == "__main__":
    post_all_100_jobs()
