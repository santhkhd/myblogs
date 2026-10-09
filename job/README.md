# 🚀 Automated Daily Government Job Post System for Blogger

This system automatically fetches, formats, and publishes latest **Kerala Govt, Central Govt, Banking, Railway, SSC, Police, and IT Job notifications** directly to your Blogger blog using the high-converting universal style inspired by portals like `kerala.indgovtjobs.net` and `FreeJobAlert`.

---

## 📁 System Files in `e:\money\job\`:

| File | Purpose |
| :--- | :--- |
| **`daily_job_bot.py`** | Master script. Fetches latest jobs, deduplicates, and generates the Blogger XML export file. |
| **`job_fetcher.py`** | Fetches live government job notifications with qualification, salary, dates, PDF link, and apply portal. |
| **`job_formatter.py`** | Converts raw job data into the clean, responsive HTML template with overview tables, action buttons & FAQ Schema. |
| **`job_publisher.py`** | Compiles jobs into Blogger Atom XML (`daily_jobs_export.xml`) for 1-click import. |
| **`email_job_poster.py`** | Optional zero-setup direct auto-publishing via Blogger's built-in "Post using email" feature. |
| **`jobs_history.json`** | Local tracking database to ensure the bot **never posts duplicate jobs**. |
| **`daily_jobs_export.xml`** | The generated Blogger XML file ready for import. |

---

## 🛠️ How to Use:

### Method 1: Generate Daily XML for 1-Click Blogger Import (Easiest)

1. Open a terminal in `e:\money\job\` and run:
   ```bash
   python daily_job_bot.py
   ```
2. The bot will create/update **`daily_jobs_export.xml`**.
3. In your **Blogger Dashboard**:
   - Go to **Settings** > **Manage Blog** > **Import content**.
   - Select **`e:\money\job\daily_jobs_export.xml`**.
   - Click **Import**. All latest jobs are instantly published!

---

### Method 2: Fully Automatic Direct Publishing (Via Email-to-Blogger)

You can make Python publish posts directly to your blog every morning with **zero manual clicking**:

1. In your **Blogger Dashboard**:
   - Go to **Settings** > Scroll to **Email** > Click **Post using email**.
   - Choose **"Publish email immediately"**.
   - Create a secret word (e.g. `santhosh.jobbot99@blogger.com`).
2. Open [**`email_job_poster.py`**](file:///e:/money/job/email_job_poster.py) and enter your secret email.
3. The script will automatically email and publish new jobs live on your blog whenever new notifications appear!

---

### Method 3: Daily Auto-Run (Windows Task Scheduler)

To run the job bot automatically every day at 8:00 AM:
1. Open Windows **Task Scheduler**.
2. Click **Create Basic Task** > Name: `Daily Job Bot`.
3. Trigger: **Daily at 8:00 AM**.
4. Action: **Start a program** > Program: `python.exe` > Arguments: `daily_job_bot.py` > Start in: `E:\money\job`.

---

## 🎯 High-CPC Google AdSense Tips for Job Blogs:
- Post 3–5 notifications daily.
- Use categories/labels: `Kerala Govt Jobs`, `Bank Jobs`, `10th Pass Jobs`, `Graduate Jobs`, `Railway Jobs`.
- Place a responsive banner ad above the **"Important Direct Links"** table for maximum click-through rates.
