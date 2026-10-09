"""
One-Time Google Blogger OAuth 2.0 Helper Script
Run this script ONCE on your computer to authenticate with Google and obtain your REFRESH_TOKEN.
"""

import os
import sys
import json

try:
    from google_auth_oauthlib.flow import InstalledAppFlow
except ImportError:
    print("Installing google-auth-oauthlib...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-auth-oauthlib", "google-api-python-client"])
    from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/blogger']

def main():
    print("=" * 65)
    print("🔑 ONE-TIME GOOGLE BLOGGER API AUTHENTICATION")
    print("=" * 65)
    print("This script will generate your BLOGGER_REFRESH_TOKEN for GitHub Actions.")
    print("=" * 65)

    client_id = input("\nEnter your Google Client ID: ").strip()
    client_secret = input("Enter your Google Client Secret: ").strip()

    if not client_id or not client_secret:
        print("❌ Client ID and Client Secret are required.")
        return

    client_config = {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": ["http://localhost"]
        }
    }

    try:
        flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
        creds = flow.run_local_server(port=0)

        print("\n" + "=" * 65)
        print("🎉 AUTHENTICATION SUCCESSFUL!")
        print("=" * 65)
        print("\nAdd these 3 Secrets in GitHub (Settings > Secrets and variables > Actions):")
        print("-" * 65)
        print(f"BLOGGER_CLIENT_ID     : {client_id}")
        print(f"BLOGGER_CLIENT_SECRET : {client_secret}")
        print(f"BLOGGER_REFRESH_TOKEN : {creds.refresh_token}")
        print("-" * 65)
        print("\nOnce added, GitHub Actions will automatically post all jobs to Blogger every day!")
        print("=" * 65)

        # Save locally for easy copy
        with open("blogger_api_credentials.txt", "w", encoding="utf-8") as f:
            f.write(f"BLOGGER_CLIENT_ID={client_id}\n")
            f.write(f"BLOGGER_CLIENT_SECRET={client_secret}\n")
            f.write(f"BLOGGER_REFRESH_TOKEN={creds.refresh_token}\n")
            f.write(f"BLOGGER_BLOG_ID=2919982446335599886\n")
        print("💾 Credentials also saved to 'blogger_api_credentials.txt' (Do not commit to git).")

    except Exception as e:
        print(f"❌ Error during authentication: {e}")

if __name__ == "__main__":
    main()
