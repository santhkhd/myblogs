# 📖 Complete Government Job Portal & Blogger Auto-Post Guide

This guide covers everything you need to run, import, and automatically post daily government jobs to your Blogger blog.

---

## 📑 Table of Contents
1. [Theme Installation (Full-Width, Mobile Responsive)](#1-theme-installation)
2. [Importing 50 Genuine Job Posts](#2-importing-50-genuine-job-posts)
3. [Bypassing Blogger Import Rate Limits](#3-bypassing-blogger-import-rate-limits)
4. [Setting Up "Post Using Email" (Zero Rate Limits)](#4-setting-up-post-using-email-zero-limits)
5. [Running the Python Automated Job Poster](#5-running-the-python-automated-job-poster)
6. [100% Free Daily Cloud Automation with GitHub Actions](#6-100-free-daily-cloud-automation-with-github-actions)

---

## 1. Theme Installation

Your theme file is located at:
📁 `e:\money\job\job_theme.xml`

### How to Install:
1. Open your **[Blogger Dashboard](https://www.blogger.com)**.
2. In the left sidebar, click **Theme**.
3. Click the **down arrow (▾)** next to the orange **`CUSTOMIZE`** button.
4. Select **Restore** ➔ Click **Upload**.
5. Select `e:\money\job\job_theme.xml`.
6. Once uploaded, your blog will have:
   - ⚡ Fast loading speed & 100% full-width mobile layout.
   - 🌙 Dark / Light mode switch.
   - 🔍 Live instant search bar.
   - 🎓 Complete Qualification directory (`10th Pass`, `12th Pass`, `Degree`, `Diploma`, `Engineering`, etc.).
   - 📍 All States directory (`Kerala`, `Central`, `Tamil Nadu`, `Karnataka`, `Delhi`, etc.).
   - 🏛️ Sector directories (`Kerala PSC`, `Bank`, `Railway RRB`, `SSC`, `UPSC`, `Defence`, `Police`, `PSU`).

---

## 2. Importing 50 Genuine Job Posts

Your 50 pre-formatted, genuine 2026 recruitment posts are located at:
📁 `e:\money\job\50_genuine_jobs_import.xml`

### How to Import:
1. In Blogger Dashboard, click **Settings** in the left sidebar.
2. Scroll down to the **Manage blog** section.
3. Click **Import content**.
4. **Important**: Make sure **"Automatically publish all imported posts and pages"** is switched **ON**.
5. Select `e:\money\job\50_genuine_jobs_import.xml` and click **Import**.

---

## 3. Bypassing Blogger Import Rate Limits

If Blogger shows the message:
> *"Seems like you tried to import too many times. Please try again later."*

Follow any of these solutions:
- **Check Drafts Tab**: Often Blogger already imported the posts in the background. Go to **Posts** ➔ Click **Drafts** ➔ Select All ➔ Click **Publish (✈️)**.
- **Mobile Hotspot Bypass**: Disconnect Wi-Fi and connect your PC to your phone's mobile hotspot. This gives you a fresh IP address and clears the rate limit instantly.
- **Incognito Window**: Open an Incognito window (`Ctrl + Shift + N`), login to Blogger, and import.
- **Cooldown**: Wait 15–30 minutes and the limit will reset automatically.

---

## 4. Setting Up "Post Using Email" (Zero Limits)

Blogger allows direct publishing by sending an email. This **never** hits the web import rate limit.

### Step 1: Enable Email Publishing on Blogger
### Step 1: Your Configured Blogger Email
Your publishing address is set to:
```text
santhkhd.jobs2026@blogger.com
```

### How Blogger Handles Emails:
- **Email Subject**: Becomes the **Post Title** and **Labels**.
  - Example: `Kerala PSC Sub Inspector 2026 #Kerala Govt Jobs, #Degree Jobs`
  - Anything after `#` becomes post tags/labels automatically.
- **Email Body**: Becomes the **Post Content** (full HTML tables, badges, buttons, and apply links).

---

## 5. Publish All 50 Jobs via Email Automatically

We created a dedicated bulk publisher script:
📁 [`e:\money\job\post_all_50_jobs_via_email.py`](file:///e:/money/job/post_all_50_jobs_via_email.py)

### Step 1: Generate a Free Google App Password (1 minute)
1. Open **[Google Account App Passwords](https://myaccount.google.com/apppasswords)**.
2. In the App name box, type: `BloggerBot`.
3. Click **Create** ➔ Copy the **16-letter password** (e.g. `abcd efgh ijkl mnop`).

### Step 2: Run the Bulk Publisher
Open PowerShell in `e:\money\job\` and run:
```powershell
python post_all_50_jobs_via_email.py
```
It will ask for:
1. Your Gmail address (e.g. `yourname@gmail.com`)
2. Your 16-letter App Password

The script will automatically send all **50 genuine job notifications** directly to `santhkhd.jobs2026@blogger.com` with formatted tables, badges, tags, and apply links!
Open `e:\money\job\email_job_poster.py` and set your details:
```python
BLOGGER_POST_EMAIL = "santhkhd.jobs2026@blogger.com"  # From Step 4
SENDER_GMAIL = "santhkhd@gmail.com"                    # Your Gmail
SENDER_APP_PASSWORD = "irnk nhbe fumq eonq"              # Your 16-letter App Password
```

### Step 3: Run the Bot
Open your terminal in `e:\money\job\` and run:
```powershell
python daily_job_bot.py
```
The bot will fetch fresh jobs from official feeds and publish them to your blog via email automatically.

---

## 6. 100% Free Daily Cloud Automation with GitHub Actions

You don't need to keep your computer turned on. GitHub will run the bot automatically 3 times every day for free.

### Files already configured:
- `.github/workflows/daily_job_bot.yml`
- `github_auto_poster.py`

### Setup Steps:
1. Push the `e:\money\job\` folder to a private or public GitHub repository.
2. In your GitHub repository:
   - Go to **Settings** ➔ **Secrets and variables** ➔ **Actions**.
   - Click **New repository secret**.
   - Add these 3 secrets:
     - `BLOGGER_POST_EMAIL`: Your Blogger secret email (`yourusername.jobs2026@blogger.com`)
     - `SENDER_GMAIL`: Your Gmail address
     - `SENDER_APP_PASSWORD`: Your 16-letter Google App Password
3. That's it! GitHub Actions will now automatically fetch and post new government jobs every day at **6:00 AM, 12:00 PM, and 6:00 PM UTC**.

---

## 📂 Summary of Project Files

| File | Function |
| :--- | :--- |
| [`job_theme.xml`](file:///e:/money/job/job_theme.xml) | Main modern, mobile-responsive full-width Blogger theme. |
| [`50_genuine_jobs_import.xml`](file:///e:/money/job/50_genuine_jobs_import.xml) | 50 Genuine 2026 recruitment posts ready to import. |
| [`email_job_poster.py`](file:///e:/money/job/email_job_poster.py) | Python module to publish posts via Gmail/Blogger email. |
| [`daily_job_bot.py`](file:///e:/money/job/daily_job_bot.py) | Local bot to fetch, format, and publish jobs. |
| [`job_fetcher.py`](file:///e:/money/job/job_fetcher.py) | RSS/Website scraper for latest recruitment updates. |
| [`job_formatter.py`](file:///e:/money/job/job_formatter.py) | Formats raw job data into structured tables & cards. |
| [`github_auto_poster.py`](file:///e:/money/job/github_auto_poster.py) | Cloud entry point for GitHub Actions. |
| [`.github/workflows/daily_job_bot.yml`](file:///e:/money/job/.github/workflows/daily_job_bot.yml) | 24/7 Cloud scheduler workflow. |
