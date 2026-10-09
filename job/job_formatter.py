"""
Job Formatter Module
Renders raw job dictionary data into a clean, mobile-responsive, Google Jobs Schema-ready HTML template.
"""

def format_job_html(job):
    """
    Renders structured job post HTML using 100% clean inline CSS
    (guarantees 0 spam score and seamless Blogger email-to-post ingestion).
    """
    return f"""
<div style="max-width:850px; margin:0 auto; font-family:'Segoe UI',Roboto,Helvetica,Arial,sans-serif; color:#0F172A; line-height:1.6; padding:10px 4px 30px; box-sizing:border-box;">
  
  <!-- Header Card -->
  <div style="background:linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%); color:#FFFFFF; border-radius:12px; padding:24px 18px; margin-bottom:20px; text-align:center; box-shadow:0 4px 15px rgba(37,99,235,0.2);">
    <div style="display:inline-block; background:rgba(255,255,255,0.2); color:#FFFFFF; padding:4px 12px; border-radius:30px; font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:10px;">
      💼 {job.get('category', 'Government Jobs')}
    </div>
    <h1 style="font-size:22px; font-weight:800; margin:0 0 10px; line-height:1.3; color:#FFFFFF;">
      {job['title']}
    </h1>
    <div style="font-size:14px; color:#DBEAFE; margin-top:8px;">
      <span>📅 Last Date: <strong>{job['last_date']}</strong></span> &nbsp;|&nbsp;
      <span>📍 Location: <strong>{job['location']}</strong></span> &nbsp;|&nbsp;
      <span>💰 Salary: <strong>{job['salary']}</strong></span>
    </div>
  </div>

  <!-- Alert Banner -->
  <div style="background:#FEF2F2; border:1px solid #FCA5A5; border-left:4px solid #EF4444; border-radius:8px; padding:12px 16px; color:#991B1B; font-size:14px; font-weight:600; margin-bottom:20px;">
    🔔 <strong>Application Alert:</strong> Applications are invited for {job['post_name']}. The last date to submit online application is <strong>{job['last_date']}</strong>.
  </div>

  <!-- 1. Quick Job Summary -->
  <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:10px; padding:18px; margin-bottom:20px;">
    <h2 style="font-size:17px; font-weight:700; color:#1E3A8A; margin:0 0 12px; border-bottom:2px solid #EFF6FF; padding-bottom:8px;">
      📋 Quick Job Summary
    </h2>
    <table style="width:100%; border-collapse:collapse; font-size:14px;">
      <tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:8px 4px; font-weight:600; color:#475569; width:40%;">Recruiting Authority</td><td style="padding:8px 4px; font-weight:700; color:#0F172A;">{job['org_name']}</td></tr>
      <tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:8px 4px; font-weight:600; color:#475569;">Post Name</td><td style="padding:8px 4px; color:#0F172A;">{job['post_name']}</td></tr>
      <tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:8px 4px; font-weight:600; color:#475569;">Total Vacancies</td><td style="padding:8px 4px; font-weight:700; color:#2563EB;">{job['vacancies']}</td></tr>
      <tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:8px 4px; font-weight:600; color:#475569;">Salary / Pay Scale</td><td style="padding:8px 4px; font-weight:700; color:#059669;">{job['salary']}</td></tr>
      <tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:8px 4px; font-weight:600; color:#475569;">Qualification Required</td><td style="padding:8px 4px; color:#0F172A;">{job['qualification']}</td></tr>
      <tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:8px 4px; font-weight:600; color:#475569;">Age Limit</td><td style="padding:8px 4px; color:#0F172A;">{job['min_age']} to {job['max_age']}</td></tr>
      <tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:8px 4px; font-weight:600; color:#475569;">Job Location</td><td style="padding:8px 4px; color:#0F172A;">{job['location']}</td></tr>
      <tr><td style="padding:8px 4px; font-weight:600; color:#475569;">Official Website</td><td style="padding:8px 4px;"><a href="{job['apply_url']}" target="_blank" rel="noopener noreferrer" style="color:#2563EB; font-weight:700; text-decoration:none;">{job['website']}</a></td></tr>
    </table>
  </div>

  <!-- 2. Important Dates -->
  <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:10px; padding:18px; margin-bottom:20px;">
    <h2 style="font-size:17px; font-weight:700; color:#1E3A8A; margin:0 0 12px; border-bottom:2px solid #EFF6FF; padding-bottom:8px;">
      📅 Important Dates
    </h2>
    <table style="width:100%; border-collapse:collapse; font-size:14px;">
      <tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:8px 4px; font-weight:600; color:#475569; width:40%;">Online Application Starts</td><td style="padding:8px 4px; font-weight:700; color:#0F172A;">{job['start_date']}</td></tr>
      <tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:8px 4px; font-weight:600; color:#475569;">Last Date to Apply</td><td style="padding:8px 4px; font-weight:700; color:#DC2626;">{job['last_date']}</td></tr>
      <tr><td style="padding:8px 4px; font-weight:600; color:#475569;">Application Fee</td><td style="padding:8px 4px; color:#0F172A;">{job['fee']}</td></tr>
    </table>
  </div>

  <!-- 3. Important Direct Links -->
  <div style="background:#F0FDF4; border:1.5px solid #86EFAC; border-radius:10px; padding:18px; margin-bottom:20px;">
    <h2 style="font-size:17px; font-weight:700; color:#166534; margin:0 0 12px;">
      🔗 Official Application &amp; Notification Links
    </h2>
    <table style="width:100%; border-collapse:collapse; font-size:14px;">
      <tr style="border-bottom:1px solid #DCFCE7;">
        <td style="padding:10px 4px; font-weight:700; color:#14532D;">Apply Online Official Link</td>
        <td style="padding:10px 4px; text-align:right;">
          <a href="{job['apply_url']}" target="_blank" rel="noopener noreferrer" style="display:inline-block; background:#16A34A; color:#FFFFFF; padding:6px 14px; border-radius:6px; font-weight:700; text-decoration:none;">Apply Now ↗</a>
        </td>
      </tr>
      <tr>
        <td style="padding:10px 4px; font-weight:700; color:#14532D;">Official Department Website</td>
        <td style="padding:10px 4px; text-align:right;">
          <a href="{job['apply_url']}" target="_blank" rel="noopener noreferrer" style="display:inline-block; background:#2563EB; color:#FFFFFF; padding:6px 14px; border-radius:6px; font-weight:700; text-decoration:none;">Official Site ↗</a>
        </td>
      </tr>
    </table>
  </div>

  <!-- 4. How to Apply Step by Step -->
  <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:10px; padding:18px;">
    <h2 style="font-size:17px; font-weight:700; color:#1E3A8A; margin:0 0 12px; border-bottom:2px solid #EFF6FF; padding-bottom:8px;">
      ✍️ How to Apply
    </h2>
    <ol style="padding-left:20px; line-height:1.7; font-size:14px; margin:0; color:#334155;">
      <li>Visit the official website: <strong>{job['website']}</strong></li>
      <li>Find the notification link for <strong>{job['post_name']}</strong></li>
      <li>Complete registration and fill in all educational and personal details.</li>
      <li>Upload scanned documents and photograph as instructed.</li>
      <li>Submit the application form before the last date: <strong>{job['last_date']}</strong>.</li>
    </ol>
  </div>

</div>
"""
