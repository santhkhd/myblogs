"""
Blogger Email Auto-Poster Module
Automatically publishes latest government jobs directly to your Blogger blog via Blogger's built-in 'Post using email' feature!
NO API KEYS OR COMPLEX GOOGLE CLOUD OAUTH REQUIRED.

How to set up:
1. Go to Blogger Dashboard -> Settings -> Email -> 'Post using email'.
2. Select 'Publish email immediately' and choose your secret word (e.g. yourname.jobalert123@blogger.com).
3. Paste that email address below in BLOGGER_POST_EMAIL.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from job_formatter import format_job_html

# Configuration (Fill with your SMTP / Gmail App Password)
BLOGGER_POST_EMAIL = "santhkhd.jobs2026@blogger.com"  # Your Blogger secret email address
SENDER_GMAIL = "santhkhd@gmail.com"                     # Your Gmail address
SENDER_APP_PASSWORD = "irnknhbefumqeonq"               # Google App Password (16 characters)

def send_job_to_blogger(job):
    """
    Sends a single job post to Blogger via Email to publish automatically.
    """
    if "yourblog.secretword" in BLOGGER_POST_EMAIL:
        print("⚠️ Please configure BLOGGER_POST_EMAIL in email_job_poster.py with your Blogger secret email.")
        return False
        
    subject = f"{job['title']} #{', '.join(job.get('labels', ['Govt Jobs']))}"
    body_html = format_job_html(job)

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = SENDER_GMAIL
    msg["To"] = BLOGGER_POST_EMAIL

    msg.attach(MIMEText(body_html, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_GMAIL, SENDER_APP_PASSWORD)
            server.sendmail(SENDER_GMAIL, BLOGGER_POST_EMAIL, msg.as_string())
        print(f"✅ Successfully published to Blogger: {job['title']}")
        return True
    except Exception as e:
        print(f"❌ Failed to email post to Blogger: {e}")
        return False
