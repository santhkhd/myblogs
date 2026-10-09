"""
Official Google Blogger API v3 Direct 150 Jobs Publisher
Bypasses both email rate limits and web import UI bugs.
Posts all 150 jobs directly into Blogger's database with real Labels and URLs!
"""

import sys
import time
import os
import json

# Ensure UTF-8 output
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from build_150_latest_jobs import JOBS_150, render_post_html

# Your Blog ID from your dashboard URL
BLOG_ID = "2919982446335599886"

# Blogger API Scope
SCOPES = ['https://www.googleapis.com/auth/blogger']

def get_authenticated_service():
    creds = None
    token_file = os.path.join(os.path.dirname(__file__), "token.json")
    client_secrets_file = os.path.join(os.path.dirname(__file__), "client_secret.json")

    # If token already saved from previous run
    if os.path.exists(token_file):
        try:
            creds = Credentials.from_authorized_user_file(token_file, SCOPES)
        except Exception:
            creds = None

    # If no valid credentials, authenticate via browser
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception:
                creds = None

        if not creds:
            if not os.path.exists(client_secrets_file):
                # Standard Google OAuth Client configuration for desktop apps
                client_config = {
                    "installed": {
                        "client_id": "407408718192.apps.googleusercontent.com",
                        "project_id": "google-blogger-api-app",
                        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                        "token_uri": "https://oauth2.googleapis.com/token",
                        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                        "client_secret": "",
                        "redirect_uris": ["http://localhost"]
                    }
                }
                print("=" * 65)
                print("GOOGLE BLOGGER API OAUTH AUTHENTICATION")
                print("=" * 65)
                print("To publish directly via Blogger API:")
                print("If you have client_secret.json from Google Cloud Console, place it in e:/money/job/client_secret.json")
                print("=" * 65)

            try:
                flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
                creds = flow.run_local_server(port=0)
                with open(token_file, "w") as token:
                    token.write(creds.to_json())
            except Exception as e:
                print(f"[AUTH ERROR] {e}")
                return None

    service = build('blogger', 'v3', credentials=creds)
    return service

def post_all_jobs_via_api():
    print(f"Connecting to Google Blogger API v3 for Blog ID: {BLOG_ID}...", flush=True)
    service = get_authenticated_service()
    if not service:
        print("[ERROR] Could not authenticate. Please see instructions.")
        return

    print(f"[SUCCESS] Authenticated! Publishing {len(JOBS_150)} jobs directly...", flush=True)
    print("=" * 65, flush=True)

    success_count = 0
    fail_count = 0

    for idx, job in enumerate(JOBS_150, 1):
        post_body = {
            "kind": "blogger#post",
            "title": job["title"],
            "content": render_post_html(job),
            "labels": job.get("labels", ["Govt Jobs", "Job Alerts 2026"])
        }

        try:
            res = service.posts().insert(blogId=BLOG_ID, body=post_body, isDraft=False).execute()
            post_url = res.get("url", "")
            print(f"[{idx:03d}/{len(JOBS_150)}] [PUBLISHED] {job['title'][:55]}... -> {post_url}", flush=True)
            success_count += 1
            time.sleep(0.5)
        except Exception as e:
            print(f"[{idx:03d}/{len(JOBS_150)}] [FAILED] {e}", flush=True)
            fail_count += 1
            time.sleep(1)

    print("\n" + "=" * 65, flush=True)
    print(f"[FINISHED] Successfully published: {success_count}/{len(JOBS_150)} standalone posts via API!", flush=True)
    if fail_count > 0:
        print(f"[ALERT] Failed: {fail_count} posts.")
    print("=" * 65, flush=True)

if __name__ == "__main__":
    post_all_jobs_via_api()
