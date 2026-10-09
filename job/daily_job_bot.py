"""
Daily Job Bot Controller
Runs the complete workflow:
1. Fetches latest active government & Kerala job notifications.
2. Checks against history to prevent duplicate posts.
3. Formats jobs into the clean IndGovtJobs style responsive template.
4. Generates a fresh Blogger XML import file (e.g. daily_jobs_export.xml).
"""

import os
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

from job_fetcher import fetch_new_jobs, get_curated_live_jobs
from job_publisher import generate_blogger_xml

def run_bot(force_all=False):
    print("="*60)
    print(">> Running Daily Government Job Post Bot...")
    print("="*60)
    
    if force_all:
        jobs = get_curated_live_jobs()
        print(f">> Compiling all {len(jobs)} curated job notifications...")
    else:
        jobs, all_jobs = fetch_new_jobs()
        if not jobs:
            print(">> No new unseen jobs found today. Compiling latest active batch...")
            jobs = all_jobs
        else:
            print(f">> Found {len(jobs)} new job notifications!")

    xml_path = generate_blogger_xml(jobs, "daily_jobs_export.xml")
    
    print("\n" + "="*60)
    print(">> SUCCESS! Daily Job Posts XML Generated!")
    print(f">> Output File: {xml_path}")
    print(f">> Total Jobs Included: {len(jobs)}")
    for i, j in enumerate(jobs, 1):
        print(f"   {i}. {j['title']} (Last Date: {j['last_date']})")
    print("="*60)
    print(">> To Publish: In Blogger Dashboard -> Settings -> Import content -> Select 'daily_jobs_export.xml'")
    print("="*60)

if __name__ == "__main__":
    force = "--all" in sys.argv
    run_bot(force_all=force)
