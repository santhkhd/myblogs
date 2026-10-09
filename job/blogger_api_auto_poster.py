"""
Official Google Blogger REST API v3 Automatic Cloud Poster
Directly publishes 50 fresh unique government job posts to Blogger via Google REST API v3.
Runs 100% automatically in GitHub Actions on a daily cron schedule without requiring email.
"""

import os
import sys
import json
import time
import urllib.request
import urllib.parse
import datetime

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from job_fetcher import fetch_new_jobs
from job_formatter import format_job_html
from job_publisher import generate_blogger_xml

# Default Blog ID (can be overridden via GitHub Secrets)
BLOG_ID = os.environ.get("BLOGGER_BLOG_ID", "2919982446335599886").strip()
CLIENT_ID = os.environ.get("BLOGGER_CLIENT_ID", "").strip()
CLIENT_SECRET = os.environ.get("BLOGGER_CLIENT_SECRET", "").strip()
REFRESH_TOKEN = os.environ.get("BLOGGER_REFRESH_TOKEN", "").strip()

def get_access_token():
    """
    Exchanges OAuth2 Refresh Token for a fresh Access Token using Google's OAuth endpoint.
    Zero external dependencies (uses standard library urllib).
    """
    if not (CLIENT_ID and CLIENT_SECRET and REFRESH_TOKEN):
        print("⚠️ Missing required OAuth credentials (BLOGGER_CLIENT_ID, BLOGGER_CLIENT_SECRET, BLOGGER_REFRESH_TOKEN).")
        return None

    token_url = "https://oauth2.googleapis.com/token"
    data = urllib.parse.urlencode({
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": REFRESH_TOKEN,
        "grant_type": "refresh_token"
    }).encode("utf-8")

    req = urllib.request.Request(token_url, data=data, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")

    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            res_body = response.read().decode("utf-8")
            token_json = json.loads(res_body)
            access_token = token_json.get("access_token")
            if access_token:
                print("✅ Successfully generated fresh Google Blogger API Access Token!")
                return access_token
            else:
                print(f"❌ Error obtaining access token: {token_json}")
                return None
    except Exception as e:
        print(f"❌ OAuth token refresh failed: {e}")
        return None

def publish_job_to_blogger(access_token, job):
    """
    Directly posts a single job to Blogger using the official REST API v3 endpoint:
    POST https://www.googleapis.com/blogger/v3/blogs/{blogId}/posts/
    """
    url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/?isDraft=false"
    
    post_payload = {
        "kind": "blogger#post",
        "title": job["title"],
        "content": format_job_html(job),
        "labels": job.get("labels", ["Govt Jobs", "Job Alerts 2026", job.get("category", "Central Govt Jobs")])
    }

    json_data = json.dumps(post_payload).encode("utf-8")
    req = urllib.request.Request(url, data=json_data, method="POST")
    req.add_header("Authorization", f"Bearer {access_token}")
    req.add_header("Content-Type", "application/json; charset=UTF-8")

    with urllib.request.urlopen(req, timeout=30) as response:
        res_body = response.read().decode("utf-8")
        return json.loads(res_body)

def main():
    print("=" * 65)
    print(f"🚀 Google Blogger API v3 Automatic Poster Started for Blog ID: {BLOG_ID}")
    print("=" * 65)

    posts_limit = int(os.environ.get("POSTS_PER_RUN", "12"))
    new_jobs, all_jobs = fetch_new_jobs(limit=posts_limit)
    jobs_to_post = new_jobs if new_jobs else all_jobs
    jobs_to_post = jobs_to_post[:posts_limit]
    print(f"📋 Total fresh unique jobs to publish in this run: {len(jobs_to_post)}")

    # 2. Authenticate
    access_token = get_access_token()
    success_count = 0
    fail_count = 0

    if access_token:
        for idx, job in enumerate(jobs_to_post, 1):
            posted = False
            for attempt in range(1, 4):
                try:
                    res = publish_job_to_blogger(access_token, job)
                    post_url = res.get("url", "")
                    print(f"[{idx:02d}/{len(jobs_to_post)}] ✅ Published: {job['title'][:55]}... ➔ {post_url}")
                    success_count += 1
                    posted = True
                    time.sleep(4.5)  # Safe 4.5s spacing prevents Google 429 burst limit
                    break
                except urllib.error.HTTPError as http_err:
                    if http_err.code == 429:
                        wait_time = 12 * attempt
                        print(f"[{idx:02d}/{len(jobs_to_post)}] ⏳ Rate limit (429) hit. Pausing {wait_time}s (Attempt {attempt}/3)...")
                        time.sleep(wait_time)
                    else:
                        print(f"[{idx:02d}/{len(jobs_to_post)}] ❌ HTTP {http_err.code} Error: {http_err}")
                        break
                except Exception as e:
                    print(f"[{idx:02d}/{len(jobs_to_post)}] ❌ Error: {e}")
                    time.sleep(5)

            if not posted:
                fail_count += 1
    else:
        print("ℹ️ Skipping direct API post because API credentials are not yet set.")
        print("💡 Please configure BLOGGER_CLIENT_ID, BLOGGER_CLIENT_SECRET, BLOGGER_REFRESH_TOKEN in GitHub Secrets.")

    # 3. Always update export XML file as backup
    xml_path = generate_blogger_xml(jobs_to_post, "daily_jobs_export.xml")
    print(f"📦 Updated backup XML: {xml_path}")
    print("=" * 65)
    print(f"🎉 Run Complete! Published: {success_count}/{len(jobs_to_post)} jobs directly via API.")
    print("=" * 65)

if __name__ == "__main__":
    main()
