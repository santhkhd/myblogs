"""
Job Formatter Module
Renders raw job dictionary data into a clean, mobile-responsive, Google Jobs Schema-ready HTML template.
"""

def format_job_html(job):
    """
    Renders structured job post HTML matching IndGovtJobs / FreeJobAlert modern style.
    """
    return f"""
<div class="job-post-container" style="max-width:900px; margin:0 auto; font-family:'Inter',system-ui,-apple-system,sans-serif; color:#0F172A; line-height:1.65; padding:0 4px 30px; box-sizing:border-box;">
  <style type="text/css">
    .job-post-container, .job-post-container * {{ box-sizing: border-box !important; }}
    [data-theme='dark'] .job-post-container {{ color: #F8FAFC !important; }}
    .job-header-card {{
      background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 50%, #3B82F6 100%);
      color: #FFFFFF !important;
      border-radius: 16px;
      padding: 1.75rem 1.5rem;
      margin-bottom: 1.5rem;
      box-shadow: 0 10px 25px rgba(37,99,235,0.25);
      text-align: center;
    }}
    .job-tag-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255,255,255,0.2);
      color: #FFFFFF;
      padding: 4px 14px;
      border-radius: 50px;
      font-size: 0.8rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 0.75rem;
      border: 1px solid rgba(255,255,255,0.3);
    }}
    .job-post-title {{
      font-size: clamp(1.4rem, 3.5vw, 1.95rem);
      font-weight: 900;
      margin: 0 0 0.5rem;
      line-height: 1.3;
      color: #FFFFFF !important;
    }}
    .job-urgent-alert {{
      background: #FEF2F2;
      border: 1.5px solid #FCA5A5;
      border-left: 5px solid #EF4444;
      border-radius: 12px;
      padding: 0.9rem 1.25rem;
      color: #991B1B;
      font-size: 0.95rem;
      font-weight: 700;
      margin-bottom: 1.5rem;
    }}
    [data-theme='dark'] .job-urgent-alert {{
      background: rgba(239,68,68,0.15) !important;
      border-color: rgba(239,68,68,0.4) !important;
      color: #FCA5A5 !important;
    }}
    .job-section-box {{
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 14px;
      padding: 1.5rem;
      margin-bottom: 1.5rem;
      box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }}
    [data-theme='dark'] .job-section-box {{
      background: #131E32 !important;
      border-color: rgba(255,255,255,0.09) !important;
    }}
    .job-sec-heading {{
      font-size: 1.25rem;
      font-weight: 800;
      color: #1E3A8A;
      margin: 0 0 1rem;
      display: flex;
      align-items: center;
      gap: 8px;
      border-bottom: 2px solid #EFF6FF;
      padding-bottom: 0.5rem;
    }}
    [data-theme='dark'] .job-sec-heading {{
      color: #60A5FA !important;
      border-bottom-color: rgba(255,255,255,0.08) !important;
    }}
    .job-overview-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 0.5rem;
    }}
    .job-overview-table tr {{
      border-bottom: 1px solid #F1F5F9;
    }}
    [data-theme='dark'] .job-overview-table tr {{
      border-bottom-color: rgba(255,255,255,0.06) !important;
    }}
    .job-overview-table td {{
      padding: 0.75rem 0.5rem;
      font-size: 0.95rem;
      vertical-align: top;
    }}
    .job-overview-table td:first-child {{
      font-weight: 700;
      color: #475569;
      width: 38%;
    }}
    [data-theme='dark'] .job-overview-table td:first-child {{
      color: #94A3B8 !important;
    }}
    .job-overview-table td:last-child {{
      font-weight: 600;
      color: #0F172A;
    }}
    [data-theme='dark'] .job-overview-table td:last-child {{
      color: #F8FAFC !important;
    }}
    .job-dates-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 12px;
      margin-top: 0.5rem;
    }}
    .job-date-card {{
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 10px;
      padding: 1rem;
      text-align: center;
    }}
    [data-theme='dark'] .job-date-card {{
      background: #0E1726 !important;
      border-color: rgba(255,255,255,0.06) !important;
    }}
    .job-date-label {{
      font-size: 0.8rem;
      font-weight: 700;
      color: #64748B;
      text-transform: uppercase;
      margin-bottom: 4px;
    }}
    .job-date-value {{
      font-size: 1.05rem;
      font-weight: 800;
      color: #2563EB;
    }}
    [data-theme='dark'] .job-date-value {{
      color: #38BDF8 !important;
    }}
    .job-action-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #2563EB;
      color: #FFFFFF !important;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 0.88rem;
      font-weight: 700;
      text-decoration: none !important;
      transition: all 0.2s;
    }}
    .btn-green {{
      background: #059669 !important;
    }}
    @media (max-width: 600px) {{
      .job-header-card {{ padding: 1.25rem 1rem; }}
      .job-section-box {{ padding: 1.15rem 1rem; }}
      .job-overview-table td:first-child {{ width: 45%; }}
      .job-dates-grid {{ grid-template-columns: 1fr; }}
    }}
  </style>

  <!-- Job Alert Header Banner -->
  <div class="job-header-card">
    <div class="job-tag-badge">💼 {job.get('category', 'Government Jobs')}</div>
    <h1 class="job-post-title">{job['title']}</h1>
    <div style="font-size:0.92rem; color:#DBEAFE; display:flex; flex-wrap:wrap; justify-content:center; gap:12px; margin-top:0.5rem;">
      <span>📅 Last Date: <strong>{job['last_date']}</strong></span>
      <span>📍 Location: <strong>{job['location']}</strong></span>
      <span>💰 Salary: <strong>{job['salary']}</strong></span>
    </div>
  </div>

  <!-- Urgent Application Alert -->
  <div class="job-urgent-alert">
    🔔 <strong>Alert:</strong> Online application registration is currently open. Ensure you verify all eligibility parameters and submit your form prior to the deadline: <strong>{job['last_date']}</strong>.
  </div>

  <!-- 1. Quick Job Overview Table -->
  <div class="job-section-box">
    <h2 class="job-sec-heading">📋 Quick Job Summary</h2>
    <table class="job-overview-table">
      <tr><td>Organization / Department</td><td><strong>{job['org_name']}</strong></td></tr>
      <tr><td>Post Name</td><td>{job['post_name']}</td></tr>
      <tr><td>Total Vacancies</td><td><strong>{job['vacancies']}</strong></td></tr>
      <tr><td>Pay Scale / Salary</td><td><strong>{job['salary']}</strong></td></tr>
      <tr><td>Educational Qualification</td><td><strong>{job['qualification']}</strong></td></tr>
      <tr><td>Age Limit</td><td>{job['min_age']} to {job['max_age']}</td></tr>
      <tr><td>Application Mode</td><td><strong>Online</strong></td></tr>
      <tr><td>Job Location</td><td>{job['location']}</td></tr>
      <tr><td>Official Portal</td><td><a href="{job['apply_url']}" target="_blank" rel="noopener noreferrer" style="color:#2563EB; font-weight:700;">{job['website']}</a></td></tr>
    </table>
  </div>

  <!-- 2. Important Dates -->
  <div class="job-section-box">
    <h2 class="job-sec-heading">📅 Important Dates</h2>
    <div class="job-dates-grid">
      <div class="job-date-card">
        <div class="job-date-label">Apply Online Starts</div>
        <div class="job-date-value">{job['start_date']}</div>
      </div>
      <div class="job-date-card">
        <div class="job-date-label">Last Date to Apply</div>
        <div class="job-date-value" style="color:#DC2626;">{job['last_date']}</div>
      </div>
      <div class="job-date-card">
        <div class="job-date-label">Exam Date</div>
        <div class="job-date-value">{job.get('exam_date', 'To be announced')}</div>
      </div>
    </div>
  </div>

  <!-- 3. Eligibility Criteria & Fees -->
  <div class="job-section-box">
    <h2 class="job-sec-heading">🎓 Eligibility Criteria &amp; Application Fee</h2>
    <h3 style="font-size:1rem; font-weight:800; margin:0.75rem 0 0.3rem;">Educational Qualifications:</h3>
    <p style="margin:0 0 1rem;">Candidate must possess <strong>{job['qualification']}</strong> from a recognized Board / University / Institution.</p>

    <h3 style="font-size:1rem; font-weight:800; margin:0.75rem 0 0.3rem;">Application Fee:</h3>
    <p style="margin:0 0 1rem;"><strong>{job['fee']}</strong>. (Payment can be completed online or through authorized portal payment gateways).</p>
  </div>

  <!-- 4. Important Links (Action Area) -->
  <div class="job-section-box" style="border:2px solid #2563EB;">
    <h2 class="job-sec-heading" style="color:#2563EB;">🔗 Important Direct Links</h2>
    <table style="width:100%; border-collapse:collapse;">
      <tr style="border-bottom:1px solid #E2E8F0;">
        <td style="padding:0.85rem 0.5rem; font-weight:700;">Official Notification (PDF)</td>
        <td style="text-align:center; padding:0.85rem 0.5rem;">
          <a href="{job['pdf_url']}" target="_blank" rel="noopener noreferrer" class="job-action-btn">Download PDF ↗</a>
        </td>
      </tr>
      <tr style="border-bottom:1px solid #E2E8F0;">
        <td style="padding:0.85rem 0.5rem; font-weight:700;">Apply Online Portal</td>
        <td style="text-align:center; padding:0.85rem 0.5rem;">
          <a href="{job['apply_url']}" target="_blank" rel="noopener noreferrer" class="job-action-btn btn-green">Apply Online ↗</a>
        </td>
      </tr>
      <tr>
        <td style="padding:0.85rem 0.5rem; font-weight:700;">Official Department Website</td>
        <td style="text-align:center; padding:0.85rem 0.5rem;">
          <a href="{job['pdf_url']}" target="_blank" rel="noopener noreferrer" class="job-action-btn">Visit Website ↗</a>
        </td>
      </tr>
    </table>
  </div>

  <!-- 5. How to Apply Step by Step -->
  <div class="job-section-box">
    <h2 class="job-sec-heading">✍️ How to Apply Step-by-Step</h2>
    <ol style="padding-left:1.25rem; line-height:1.8; margin:0;">
      <li>Visit the official application portal: <strong>{job['website']}</strong>.</li>
      <li>Register or log in with your credentials.</li>
      <li>Locate the notification for <strong>{job['post_name']}</strong>.</li>
      <li>Fill out the required educational, personal, and identity details.</li>
      <li>Upload scanned photograph and signature in the prescribed file size.</li>
      <li>Pay the application fee (if applicable) and submit the final form.</li>
      <li>Print and save your confirmation acknowledgment slip for future reference.</li>
    </ol>
  </div>
</div>
"""
