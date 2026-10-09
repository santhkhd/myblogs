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
from build_150_latest_jobs import JOBS_150, render_post_html

# Configuration
BLOGGER_POST_EMAIL = "santhkhd.jobs2026@blogger.com"
SENDER_GMAIL = "santhkhd@gmail.com"
SENDER_APP_PASSWORD = "irnknhbefumqeonq"

def connect_smtp(user, password):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=20)
    server.login(user, password)
    return server

def post_all_150_jobs(sender_email=None, sender_password=None, delay_seconds=1.2):
    gmail_user = sender_email or SENDER_GMAIL
    gmail_pass = sender_password or SENDER_APP_PASSWORD

    print(f"Connecting to Gmail SMTP as {gmail_user}...", flush=True)
    server = None
    try:
        server = connect_smtp(gmail_user, gmail_pass)
        print(f"[SUCCESS] Connected to Gmail SMTP successfully!", flush=True)
    except Exception as e:
        print(f"[ERROR] Failed to connect to Gmail: {e}", flush=True)
        return

    print(f"Starting bulk email publication of {len(JOBS_150)} jobs to {BLOGGER_POST_EMAIL}...", flush=True)
    print("=" * 65, flush=True)

    success_count = 0
    fail_count = 0

    for idx, job in enumerate(JOBS_150, 1):
        # Clean title without hashtag mess
        subject = job['title']
        body_html = render_post_html(job)

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = gmail_user
        msg["To"] = BLOGGER_POST_EMAIL
        msg.attach(MIMEText(body_html, "html", "utf-8"))

        # Reconnect every 25 emails to avoid SMTP connection drops
        if idx % 25 == 0:
            try:
                server.quit()
            except Exception:
                pass
            try:
                server = connect_smtp(gmail_user, gmail_pass)
            except Exception:
                pass

        posted = False
        for retry in range(3):
            try:
                if not server:
                    server = connect_smtp(gmail_user, gmail_pass)
                server.sendmail(gmail_user, BLOGGER_POST_EMAIL, msg.as_string())
                print(f"[{idx:03d}/{len(JOBS_150)}] [OK] Sent: {job['title'][:60]}...", flush=True)
                success_count += 1
                posted = True
                break
            except Exception as e:
                print(f"[{idx:03d}/{len(JOBS_150)}] [RETRY {retry+1}] SMTP error: {e}", flush=True)
                time.sleep(2)
                try:
                    server = connect_smtp(gmail_user, gmail_pass)
                except Exception:
                    server = None

        if not posted:
            print(f"[{idx:03d}/{len(JOBS_150)}] [FAILED] Could not send after 3 attempts.", flush=True)
            fail_count += 1

        if idx < len(JOBS_150):
            time.sleep(delay_seconds)

    try:
        if server:
            server.quit()
    except Exception:
        pass

    print("\n" + "=" * 65, flush=True)
    print(f"[FINISHED] Successfully posted: {success_count}/{len(JOBS_150)} jobs to Blogger!", flush=True)
    if fail_count > 0:
        print(f"[ALERT] {fail_count} jobs failed to send.", flush=True)
    print("Check your Blogger Posts dashboard to see all jobs published live!", flush=True)
    print("=" * 65, flush=True)

if __name__ == "__main__":
    post_all_150_jobs()
