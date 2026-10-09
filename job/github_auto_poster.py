"""
GitHub Actions Cloud Auto-Poster Script
Runs automatically in GitHub Actions on a daily cron schedule.
Fetches latest government jobs and posts them to Blogger without requiring your local PC.
"""

import os
import sys
import smtplib
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
BLOGGER_EMAIL = os.environ.get("BLOGGER_POST_EMAIL")
SENDER_GMAIL = os.environ.get("SENDER_GMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_GMAIL_APP_PASSWORD")

def publish_via_email(job):
    """Publishes a job post via Blogger Email to Post with clean multipart MIME"""
    if not (BLOGGER_EMAIL and SENDER_GMAIL and SENDER_PASSWORD):
        print("ℹ️ Skipping email dispatch: GitHub Secrets BLOGGER_POST_EMAIL / SENDER_GMAIL not set.")
        return False

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

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_GMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_GMAIL, BLOGGER_EMAIL, msg.as_string())
        print(f"✅ Published to Blogger: {job['title']}")
        return True
    except Exception as e:
        print(f"❌ Email error: {e}")
        return False

def main():
    print("="*60)
    print("🚀 GitHub Actions Daily Job Bot Execution Started...")
    print("="*60)

    # 1. Fetch live fresh jobs (deduplicated against history)
    new_jobs, all_jobs = fetch_new_jobs(limit=50)
    jobs_to_post = new_jobs if new_jobs else all_jobs
    jobs_to_post = jobs_to_post[:50]

    print(f"📋 Total fresh jobs to publish in this run: {len(jobs_to_post)}")

    # 2. Publish to Blogger with safe anti-block delay
    published_count = 0
    import time
    for job in jobs_to_post:
        success = publish_via_email(job)
        if success:
            published_count += 1
            time.sleep(4)  # 4-second anti-spam delay between posts

    # 3. Always generate fresh XML backup
    xml_file = generate_blogger_xml(jobs_to_post, "daily_jobs_export.xml")
    print(f"📦 Generated updated XML: {xml_file}")
    print("="*60)
    print(f"🎉 Completed! Published: {published_count}/{len(jobs_to_post)} jobs.")
    print("="*60)

if __name__ == "__main__":
    main()
