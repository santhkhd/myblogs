"""
Build Comprehensive, 100% Full-Width Mobile-Responsive Job Portal Theme
Includes State-wise, Sector-wise, and Qualification-wise directory grids and filters.
"""

import os
import xml.sax

JOB_THEME_XML = """<!DOCTYPE html>
<html b:version='2' class='blogger' expr:dir='data:blog.languageDirection' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
  <head>
    <meta charset='utf-8'/>
    <meta content='width=device-width, initial-scale=1, maximum-scale=5' name='viewport'/>
    <title><data:blog.pageTitle/></title>
    <link href='https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&amp;display=swap' rel='stylesheet'/>
    <link href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css' rel='stylesheet'/>
    
    <b:skin><![CDATA[
      /* Modern High-Speed Job Portal Design System */
      :root {
        --bg-page: #F8FAFC;
        --bg-surface: #FFFFFF;
        --bg-card: #FFFFFF;
        --bg-card-hover: #F1F5F9;
        --bg-header: #1E3A8A;
        --text-primary: #0F172A;
        --text-secondary: #475569;
        --text-muted: #94A3B8;
        --border-color: #E2E8F0;
        --border-hover: rgba(37, 99, 235, 0.4);
        --primary: #2563EB;
        --primary-hover: #1D4ED8;
        --primary-light: rgba(37, 99, 235, 0.08);
        --accent: #F59E0B;
        --success: #059669;
        --danger: #DC2626;
        --card-shadow: 0 3px 12px rgba(0, 0, 0, 0.04);
        --card-hover-shadow: 0 8px 24px rgba(37, 99, 235, 0.12);
        --radius: 12px;
        --transition: all 0.22s cubic-bezier(0.4, 0, 0.2, 1);
        --font: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      }

      [data-theme='dark'] {
        --bg-page: #0B1120;
        --bg-surface: #0E1726;
        --bg-card: #131E32;
        --bg-card-hover: #182640;
        --bg-header: #070D18;
        --text-primary: #F8FAFC;
        --text-secondary: #94A3B8;
        --text-muted: #64748B;
        --border-color: rgba(255, 255, 255, 0.09);
        --border-hover: rgba(59, 130, 246, 0.5);
        --primary: #3B82F6;
        --primary-hover: #60A5FA;
        --primary-light: rgba(59, 130, 246, 0.15);
        --card-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
        --card-hover-shadow: 0 10px 30px rgba(59, 130, 246, 0.25);
      }

      /* 100% True Full-Width Reset */
      * {
        box-sizing: border-box !important;
        margin: 0;
        padding: 0;
        -webkit-tap-highlight-color: transparent;
      }

      html, body {
        width: 100% !important;
        max-width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        background-color: var(--bg-page);
        color: var(--text-primary);
        font-family: var(--font);
        line-height: 1.6;
        overflow-x: hidden !important;
        transition: background-color 0.3s ease, color 0.3s ease;
      }

      /* Sticky Brand Header */
      header {
        background: var(--bg-surface);
        border-bottom: 1px solid var(--border-color);
        position: sticky;
        top: 0;
        z-index: 1000;
        width: 100%;
        box-shadow: 0 2px 8px rgba(0,0,0,0.02);
      }
      .header-wrap {
        width: 100%;
        max-width: 1400px;
        margin: 0 auto;
        padding: 0.65rem 1rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 0.75rem;
      }
      .site-logo {
        display: flex;
        align-items: center;
        gap: 8px;
        text-decoration: none;
        color: var(--text-primary);
        font-size: 1.25rem;
        font-weight: 900;
        letter-spacing: -0.02em;
        white-space: nowrap;
      }
      .site-logo i { color: var(--primary); font-size: 1.35rem; }
      .site-logo span {
        background: linear-gradient(135deg, #2563EB 0%, #7C3AED 100%);
        color: #FFFFFF;
        font-size: 0.7rem;
        padding: 2px 7px;
        border-radius: 6px;
        font-weight: 800;
        text-transform: uppercase;
      }

      .nav-links {
        display: flex;
        align-items: center;
        gap: 0.25rem;
      }
      .nav-links a {
        color: var(--text-secondary);
        text-decoration: none;
        padding: 0.4rem 0.8rem;
        font-size: 0.86rem;
        font-weight: 700;
        border-radius: 50px;
        transition: var(--transition);
        white-space: nowrap;
      }
      .nav-links a:hover,
      .nav-links a.active {
        color: #FFFFFF;
        background: var(--primary);
      }

      .theme-btn {
        background: var(--bg-page);
        border: 1px solid var(--border-color);
        color: var(--text-primary);
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        font-size: 0.9rem;
        flex-shrink: 0;
      }

      /* Hero Search Banner */
      .job-hero {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 60%, #3B82F6 100%);
        color: #FFFFFF;
        padding: 2.25rem 1rem 1.85rem;
        text-align: center;
        width: 100%;
      }
      .job-hero-title {
        font-size: clamp(1.75rem, 4vw, 2.4rem);
        font-weight: 900;
        margin: 0 0 0.4rem;
        letter-spacing: -0.02em;
        line-height: 1.2;
      }
      .job-hero-sub {
        font-size: 0.98rem;
        opacity: 0.92;
        max-width: 650px;
        margin: 0 auto 1.25rem;
      }

      /* Search Bar */
      .hero-search-box {
        max-width: 640px;
        margin: 0 auto;
        position: relative;
        display: flex;
        align-items: center;
      }
      .hero-search-box input {
        width: 100%;
        height: 48px;
        padding: 0 16px 0 46px;
        background: #FFFFFF;
        border: none;
        border-radius: 50px;
        font-size: 0.95rem;
        font-weight: 600;
        font-family: inherit;
        color: #0F172A;
        outline: none;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
      }
      .hero-search-box .search-icon {
        position: absolute;
        left: 18px;
        color: #2563EB;
        font-size: 1.05rem;
        pointer-events: none;
      }

      /* Sticky Category Bar */
      .job-cat-bar {
        background: var(--bg-surface);
        border-bottom: 1px solid var(--border-color);
        padding: 8px 0;
        position: sticky;
        top: 57px;
        z-index: 900;
        width: 100%;
        box-shadow: 0 2px 6px rgba(0,0,0,0.02);
      }
      .job-cat-track {
        width: 100%;
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 0.75rem;
        display: flex;
        gap: 6px;
        overflow-x: auto;
        white-space: nowrap;
        scrollbar-width: none;
        -webkit-overflow-scrolling: touch;
      }
      .job-cat-track::-webkit-scrollbar { display: none; }
      .job-cat-pill {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        padding: 6px 14px;
        background: var(--bg-page);
        color: var(--text-secondary);
        border: 1px solid var(--border-color);
        border-radius: 50px;
        font-size: 0.82rem;
        font-weight: 700;
        text-decoration: none;
        transition: var(--transition);
        flex-shrink: 0;
      }
      .job-cat-pill:hover,
      .job-cat-pill.active {
        background: var(--primary);
        color: #FFFFFF;
        border-color: var(--primary);
      }

      /* Multi-Section Quick Browse Blocks (Qualifications, States, Top Sectors) */
      .quick-browse-grid {
        width: 100%;
        max-width: 1400px;
        margin: 1.25rem auto 0;
        padding: 0 0.75rem;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 12px;
      }
      .browse-block {
        background: var(--bg-card);
        border: 1.5px solid var(--border-color);
        border-radius: var(--radius);
        padding: 1.1rem;
        box-shadow: var(--card-shadow);
      }
      .browse-header {
        font-size: 0.95rem;
        font-weight: 800;
        color: var(--text-primary);
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 2px solid var(--primary-light);
        padding-bottom: 0.4rem;
      }
      .browse-chips {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
      }
      .browse-chip {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        background: var(--bg-page);
        border: 1px solid var(--border-color);
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 700;
        color: var(--text-secondary);
        text-decoration: none;
        transition: var(--transition);
      }
      .browse-chip:hover {
        background: var(--primary);
        color: #FFFFFF;
        border-color: var(--primary);
      }

      /* Main Content Layout (100% width on Mobile) */
      .portal-layout {
        width: 100%;
        max-width: 1400px;
        margin: 1.5rem auto 3rem;
        padding: 0 0.75rem;
        display: grid;
        grid-template-columns: 1fr 340px;
        gap: 1.5rem;
      }
      @media (max-width: 960px) {
        .portal-layout {
          grid-template-columns: 100% !important;
          margin-top: 1rem;
          padding: 0 0.4rem;
        }
        .nav-links { display: none; }
      }

      /* Modern Job Notification Cards Grid */
      .job-feed {
        display: flex;
        flex-direction: column;
        gap: 12px;
        width: 100%;
      }

      .job-card {
        background: var(--bg-card);
        border: 1.5px solid var(--border-color);
        border-radius: var(--radius);
        padding: 1.15rem 1.25rem;
        box-shadow: var(--card-shadow);
        transition: var(--transition);
        text-decoration: none;
        color: inherit;
        display: flex;
        flex-direction: column;
        gap: 8px;
        width: 100%;
        position: relative;
        overflow: hidden;
      }
      .job-card:hover {
        transform: translateY(-2px);
        border-color: var(--primary);
        box-shadow: var(--card-hover-shadow);
        background: var(--bg-card-hover);
      }
      .job-card-top {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 8px;
        flex-wrap: wrap;
      }
      .job-org-badge {
        font-size: 0.76rem;
        font-weight: 800;
        color: var(--primary);
        background: var(--primary-light);
        padding: 3px 9px;
        border-radius: 6px;
        text-transform: uppercase;
        letter-spacing: 0.3px;
      }
      .job-date-badge {
        font-size: 0.76rem;
        font-weight: 800;
        color: var(--danger);
        background: #FEE2E2;
        padding: 2px 8px;
        border-radius: 6px;
        display: flex;
        align-items: center;
        gap: 4px;
      }
      [data-theme='dark'] .job-date-badge {
        background: rgba(220,38,38,0.2);
      }

      .job-card-title {
        font-size: 1.12rem;
        font-weight: 800;
        color: var(--text-primary);
        line-height: 1.35;
        margin: 0;
      }
      .job-card-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin: 6px 0;
      }
      .job-tag-chip {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        background: var(--primary-light);
        color: var(--primary);
        border: 1px solid rgba(37,99,235,0.18);
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.8rem;
        transition: var(--transition);
      }
      .job-tag-chip:hover {
        background: var(--primary);
        color: #FFFFFF;
      }
      [data-theme='dark'] .job-tag-chip {
        background: rgba(37,99,235,0.22);
        color: #93C5FD;
        border-color: rgba(147,197,253,0.25);
      }

      .job-card-footer {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-top: 2px;
        padding-top: 8px;
        border-top: 1px solid var(--border-color);
      }
      .job-apply-link {
        font-size: 0.88rem;
        font-weight: 800;
        color: var(--primary);
        display: inline-flex;
        align-items: center;
        gap: 5px;
      }

      /* Single Post View */
      .single-post-view {
        background: var(--bg-card);
        border: 1.5px solid var(--border-color);
        border-radius: var(--radius);
        padding: 1.5rem 1.25rem;
        box-shadow: var(--card-shadow);
        width: 100%;
      }

      /* Sidebar & Widgets */
      .sidebar-card {
        background: var(--bg-card);
        border: 1.5px solid var(--border-color);
        border-radius: var(--radius);
        padding: 1.25rem;
        margin-bottom: 1.25rem;
        box-shadow: var(--card-shadow);
      }
      .sidebar-title {
        font-size: 1.05rem;
        font-weight: 800;
        margin-bottom: 0.75rem;
        border-bottom: 2px solid var(--primary);
        padding-bottom: 0.4rem;
        color: var(--text-primary);
        display: flex;
        align-items: center;
        gap: 8px;
      }

      .telegram-cta {
        background: linear-gradient(135deg, #0284C7 0%, #0369A1 100%);
        color: #FFFFFF !important;
        border-radius: var(--radius);
        padding: 1.35rem;
        text-align: center;
        margin-bottom: 1.25rem;
        box-shadow: 0 6px 20px rgba(2,132,199,0.2);
      }
      .telegram-cta h3 { font-size: 1.15rem; font-weight: 900; margin: 0 0 4px; }
      .telegram-cta p { font-size: 0.85rem; opacity: 0.95; margin-bottom: 0.85rem; }
      .telegram-cta a {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #FFFFFF;
        color: #0284C7 !important;
        font-weight: 800;
        padding: 8px 18px;
        border-radius: 50px;
        text-decoration: none;
        font-size: 0.88rem;
      }

      .category-list {
        list-style: none;
        display: flex;
        flex-direction: column;
        gap: 6px;
      }
      .category-list a {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 7px 10px;
        background: var(--bg-page);
        border: 1px solid var(--border-color);
        border-radius: 6px;
        color: var(--text-primary);
        text-decoration: none;
        font-weight: 700;
        font-size: 0.85rem;
        transition: var(--transition);
      }
      .category-list a:hover {
        background: var(--primary);
        color: #FFFFFF;
        border-color: var(--primary);
      }

      /* Mobile Overrides (True 100% Width) */
      @media (max-width: 600px) {
        .header-wrap { padding: 0.5rem 0.65rem; }
        .site-logo { font-size: 1.1rem; }
        .job-hero { padding: 1.5rem 0.75rem 1.25rem; }
        .hero-search-box input { height: 44px; font-size: 0.9rem; }
        .browse-header { font-size: 0.88rem; }
        .browse-chip { font-size: 0.75rem; padding: 3px 8px; }
        .job-card { padding: 1rem 0.85rem; }
        .job-card-title { font-size: 1.02rem; }
        .single-post-view { padding: 1rem 0.65rem; }
      }

      /* Footer */
      footer {
        background: var(--bg-surface);
        border-top: 1px solid var(--border-color);
        padding: 2rem 1rem;
        text-align: center;
        font-size: 0.88rem;
        color: var(--text-secondary);
      }
      footer a { color: var(--primary); text-decoration: none; font-weight: 700; }
    ]]></b:skin>
  </head>
  <body>
    <!-- Top Header -->
    <header>
      <div class='header-wrap'>
        <a class='site-logo' expr:href='data:blog.homepageUrl'>
          <i class='fas fa-briefcase'/> <data:blog.title/> <span>LIVE 2026</span>
        </a>
        <div style='display:flex; align-items:center; gap:8px;'>
          <nav class='nav-links'>
            <a class='active' expr:href='data:blog.homepageUrl'>Home</a>
            <a href='/search/label/Kerala%20Govt%20Jobs'>Kerala Jobs</a>
            <a href='/search/label/Bank%20Jobs'>Bank Jobs</a>
            <a href='/search/label/Railway%20Jobs'>Railway Jobs</a>
            <a href='/search/label/SSC%20CGL'>SSC Jobs</a>
            <a href='/search/label/10th%20Pass'>10th Pass</a>
            <a href='/search/label/Degree%20Jobs'>Degree Jobs</a>
          </nav>
          <button class='theme-btn' onclick='toggleDark()' title='Toggle Theme' type='button'>
            <i class='fas fa-moon' id='themeIcon'/>
          </button>
        </div>
      </div>
    </header>

    <!-- Hero Search -->
    <b:if cond='data:blog.pageType != "item"'>
      <div class='job-hero'>
        <h1 class='job-hero-title'>Government Job Notifications 2026</h1>
        <p class='job-hero-sub'>Daily verified Kerala PSC, Central Govt, Banking, Railway, SSC &amp; Police recruitment updates.</p>
        <div class='hero-search-box'>
          <i class='fas fa-search search-icon'/>
          <input id='jobSearch' oninput='liveFilterJobs(this.value)' placeholder='Search Kerala PSC, Bank, Railway, SSC, 10th Pass, Degree...' type='text'/>
        </div>
      </div>

      <!-- Category Filter Pills Bar -->
      <div class='job-cat-bar'>
        <div class='job-cat-track'>
          <a class='job-cat-pill active' expr:href='data:blog.homepageUrl'>⚡ All Jobs</a>
          <a class='job-cat-pill' href='/search/label/Kerala%20Govt%20Jobs'>🌴 Kerala Govt Jobs</a>
          <a class='job-cat-pill' href='/search/label/Kerala%20PSC'>📜 Kerala PSC</a>
          <a class='job-cat-pill' href='/search/label/Bank%20Jobs'>🏦 Bank Jobs (SBI/IBPS)</a>
          <a class='job-cat-pill' href='/search/label/Railway%20Jobs'>🚆 Railway (RRB)</a>
          <a class='job-cat-pill' href='/search/label/SSC%20CGL'>📋 SSC &amp; UPSC</a>
          <a class='job-cat-pill' href='/search/label/Defence%20Jobs'>🎖️ Defence &amp; Army</a>
          <a class='job-cat-pill' href='/search/label/Police%20Jobs'>👮 Police Jobs</a>
          <a class='job-cat-pill' href='/search/label/Teaching%20Jobs'>👩‍🏫 Teaching</a>
          <a class='job-cat-pill' href='/search/label/Medical%20Jobs'>🏥 Medical / Nursing</a>
          <a class='job-cat-pill' href='/search/label/Engineering%20Jobs'>⚙️ Engineering</a>
        </div>
      </div>
    </b:if>

    <!-- Main Layout Container (Job Feed is at the Top!) -->
    <div class='portal-layout'>
      <!-- Feed / Main Content -->
      <main>
        <b:section id='main' showaddelement='yes'>
          <b:widget id='Blog1' locked='true' title='Blog Posts' type='Blog'>
            <b:includable id='main' var='top'>
              <b:if cond='data:blog.pageType == "item"'>
                <!-- Single Job Notification Post -->
                <b:loop values='data:posts' var='post'>
                  <article class='single-post-view'>
                    <div style='margin-bottom:1rem; display:flex; flex-wrap:wrap; gap:6px;'>
                      <b:loop values='data:post.labels' var='label'>
                        <a expr:href='data:label.url' style='background:var(--primary-light); color:var(--primary); padding:4px 10px; border-radius:6px; font-size:0.8rem; font-weight:700; text-decoration:none;'>
                          🏷️ <data:label.name/>
                        </a>
                      </b:loop>
                    </div>
                    <h1 style='font-size:clamp(1.5rem, 3.5vw, 2.2rem); font-weight:900; margin:0 0 1.25rem; color:var(--text-primary); line-height:1.3;'><data:post.title/></h1>
                    <data:post.body/>
                  </article>
                </b:loop>
              <b:else/>
                <!-- Modern Job Listing Cards Feed -->
                <div class='job-feed' id='jobFeedContainer'>
                  <b:loop values='data:posts' var='post'>
                    <a class='job-card' expr:href='data:post.url'>
                      <div class='job-card-top'>
                        <span class='job-org-badge'>
                          <i class='fas fa-building'/> Govt Notification
                        </span>
                        <span class='job-date-badge'><i class='far fa-clock'/> <data:post.dateHeader/></span>
                      </div>
                      <h2 class='job-card-title'><data:post.title/></h2>
                      
                      <!-- Display ALL Category & Label Chips Under Every Post -->
                      <div class='job-card-tags'>
                        <b:loop values='data:post.labels' var='label'>
                          <span class='job-tag-chip'>
                            <i class='fas fa-tag' style='color:var(--primary);'/> <data:label.name/>
                          </span>
                        </b:loop>
                      </div>

                      <div class='job-card-footer'>
                        <span style='font-size:0.85rem; color:var(--text-muted); font-weight:600;'>Verified Notification</span>
                        <span class='job-apply-link'>Apply Online &amp; PDF ➔</span>
                      </div>
                    </a>
                  </b:loop>
                </div>

                <!-- Modern Pagination Controls -->
                <div style='display:flex; align-items:center; justify-content:space-between; margin-top:1.5rem; gap:12px; flex-wrap:wrap;'>
                  <b:if cond='data:newerPageUrl'>
                    <a expr:href='data:newerPageUrl' style='padding:10px 20px; background:var(--bg-surface); border:1.5px solid var(--border-color); border-radius:50px; font-weight:800; text-decoration:none; color:var(--text-primary); font-size:0.9rem; display:inline-flex; align-items:center; gap:6px; box-shadow:var(--card-shadow);'>
                      ⬅ Newer Job Updates
                    </a>
                  </b:if>
                  <b:if cond='data:olderPageUrl'>
                    <a expr:href='data:olderPageUrl' style='padding:10px 20px; background:var(--primary); color:#FFFFFF; border-radius:50px; font-weight:800; text-decoration:none; font-size:0.9rem; display:inline-flex; align-items:center; gap:6px; margin-left:auto; box-shadow:0 4px 14px rgba(37,99,235,0.25);'>
                      Older Job Notifications ➔
                    </a>
                  </b:if>
                </div>
              </b:if>
            </b:includable>
            <b:includable id='backlinkDeleteIcon' var='backlink'/>
            <b:includable id='backlinks' var='post'/>
            <b:includable id='comment-form' var='post'/>
            <b:includable id='commentDeleteIcon' var='comment'/>
            <b:includable id='comment_picker' var='post'/>
            <b:includable id='comments' var='post'/>
            <b:includable id='feedLinks'/>
            <b:includable id='feedLinksBody' var='links'/>
            <b:includable id='iframe_comments' var='post'/>
            <b:includable id='mobile-index-post' var='post'/>
            <b:includable id='mobile-main' var='top'/>
            <b:includable id='mobile-nextprev'/>
            <b:includable id='mobile-post' var='post'/>
            <b:includable id='nextprev'/>
            <b:includable id='post' var='post'/>
            <b:includable id='postQuickEdit' var='post'/>
            <b:includable id='shareButtons' var='post'/>
            <b:includable id='status-message'/>
            <b:includable id='threaded-comment-form' var='post'/>
            <b:includable id='threaded_comment_js' var='post'/>
            <b:includable id='threaded_comments' var='post'/>
          </b:widget>
        </b:section>
      </main>

      <!-- Sidebar -->
      <aside>
        <!-- Telegram Alerts CTA -->
        <div class='telegram-cta'>
          <i class='fab fa-telegram-plane' style='font-size:2.2rem; margin-bottom:0.4rem;'/>
          <h3>Daily Job Alerts on Telegram</h3>
          <p>Get instant notifications for Kerala PSC, SSC, Bank &amp; Railway recruitment.</p>
          <a href='https://telegram.org' rel='noopener noreferrer' target='_blank'>Join Telegram Channel ↗</a>
        </div>

        <!-- Quick Categories -->
        <div class='sidebar-card'>
          <h3 class='sidebar-title'><i class='fas fa-th-list'/> Top Job Sectors</h3>
          <ul class='category-list'>
            <li><a href='/search/label/Kerala%20Govt%20Jobs'><span>🌴 Kerala Govt Jobs</span> <i class='fas fa-chevron-right'/></a></li>
            <li><a href='/search/label/Kerala%20PSC'><span>📜 Kerala PSC Notifications</span> <i class='fas fa-chevron-right'/></a></li>
            <li><a href='/search/label/Bank%20Jobs'><span>🏦 Banking (SBI / IBPS)</span> <i class='fas fa-chevron-right'/></a></li>
            <li><a href='/search/label/Railway%20Jobs'><span>🚆 Railway (RRB)</span> <i class='fas fa-chevron-right'/></a></li>
            <li><a href='/search/label/SSC%20CGL'><span>📋 SSC &amp; UPSC</span> <i class='fas fa-chevron-right'/></a></li>
            <li><a href='/search/label/Defence%20Jobs'><span>🎖️ Defence &amp; Armed Forces</span> <i class='fas fa-chevron-right'/></a></li>
          </ul>
        </div>
      </aside>
    </div>

    <!-- Quick Browse Directory Hubs (Cleanly Placed BELOW the Job Posts Feed!) -->
    <b:if cond='data:blog.pageType != "item"'>
      <div class='quick-browse-grid' style='margin-bottom: 2.5rem;'>
        <!-- Block 1: By Qualification -->
        <div class='browse-block'>
          <div class='browse-header'><span>🎓 Jobs by Qualification</span> <i class='fas fa-graduation-cap' style='color:var(--primary);'/></div>
          <div class='browse-chips'>
            <a class='browse-chip' href='/search/label/10th%20Pass'>10th Pass (SSLC)</a>
            <a class='browse-chip' href='/search/label/12th%20Pass'>12th Pass (+2)</a>
            <a class='browse-chip' href='/search/label/ITI%20Jobs'>ITI Pass</a>
            <a class='browse-chip' href='/search/label/Diploma%20Jobs'>Diploma</a>
            <a class='browse-chip' href='/search/label/Degree%20Jobs'>Any Graduate / Degree</a>
            <a class='browse-chip' href='/search/label/Engineering%20Jobs'>B.Tech / B.E</a>
            <a class='browse-chip' href='/search/label/Medical%20Jobs'>Nursing / GNM / MBBS</a>
            <a class='browse-chip' href='/search/label/PG%20Jobs'>Post Graduate (PG)</a>
            <a class='browse-chip' href='/search/label/Teaching%20Jobs'>B.Ed / Teacher</a>
            <a class='browse-chip' href='/search/label/Degree%20Jobs'>MBA / MCA / CA</a>
          </div>
        </div>

        <!-- Block 2: By Major Sectors -->
        <div class='browse-block'>
          <div class='browse-header'><span>🏛️ Jobs by Sector</span> <i class='fas fa-building' style='color:var(--primary);'/></div>
          <div class='browse-chips'>
            <a class='browse-chip' href='/search/label/Kerala%20PSC'>Kerala PSC</a>
            <a class='browse-chip' href='/search/label/Bank%20Jobs'>Banking (SBI / IBPS)</a>
            <a class='browse-chip' href='/search/label/Railway%20Jobs'>Indian Railways (RRB)</a>
            <a class='browse-chip' href='/search/label/SSC%20CGL'>SSC (CGL / CHSL / MTS)</a>
            <a class='browse-chip' href='/search/label/UPSC%20Jobs'>UPSC / Civil Services</a>
            <a class='browse-chip' href='/search/label/Defence%20Jobs'>Army / Navy / Airforce</a>
            <a class='browse-chip' href='/search/label/Police%20Jobs'>Police / Paramilitary</a>
            <a class='browse-chip' href='/search/label/PSU%20Jobs'>PSU (ISRO / DRDO / IOCL)</a>
            <a class='browse-chip' href='/search/label/Medical%20Jobs'>AIIMS &amp; Health</a>
            <a class='browse-chip' href='/search/label/Central%20Govt%20Jobs'>India Post / GDS</a>
          </div>
        </div>

        <!-- Block 3: State-Wise Jobs -->
        <div class='browse-block'>
          <div class='browse-header'><span>📍 Jobs by State</span> <i class='fas fa-map-marker-alt' style='color:var(--primary);'/></div>
          <div class='browse-chips'>
            <a class='browse-chip' href='/search/label/Kerala%20Govt%20Jobs' style='font-weight:800; color:var(--primary); background:var(--primary-light);'>🌴 Kerala</a>
            <a class='browse-chip' href='/search/label/Central%20Govt%20Jobs' style='font-weight:800;'>🇮🇳 All India / Central</a>
            <a class='browse-chip' href='/search/label/Tamil%20Nadu%20Jobs'>Tamil Nadu</a>
            <a class='browse-chip' href='/search/label/Karnataka%20Jobs'>Karnataka</a>
            <a class='browse-chip' href='/search/label/Maharashtra%20Jobs'>Maharashtra</a>
            <a class='browse-chip' href='/search/label/Delhi%20Jobs'>Delhi NCR</a>
            <a class='browse-chip' href='/search/label/Andhra%20Jobs'>Andhra Pradesh</a>
            <a class='browse-chip' href='/search/label/Telangana%20Jobs'>Telangana</a>
            <a class='browse-chip' href='/search/label/Uttar%20Pradesh%20Jobs'>Uttar Pradesh</a>
            <a class='browse-chip' href='/search/label/West%20Bengal%20Jobs'>West Bengal</a>
            <a class='browse-chip' href='/search/label/Bihar%20Jobs'>Bihar</a>
            <a class='browse-chip' href='/search/label/Gujarat%20Jobs'>Gujarat</a>
            <a class='browse-chip' href='/search/label/Rajasthan%20Jobs'>Rajasthan</a>
            <a class='browse-chip' href='/search/label/Punjab%20Jobs'>Punjab &amp; Haryana</a>
            <a class='browse-chip' href='/search/label/Odisha%20Jobs'>Odisha</a>
            <a class='browse-chip' href='/search/label/Madhya%20Pradesh%20Jobs'>Madhya Pradesh</a>
            <a class='browse-chip' href='/search/label/Assam%20Jobs'>Assam &amp; NE</a>
            <a class='browse-chip' href='/search/label/Jammu%20Kashmir%20Jobs'>Jammu &amp; Kashmir</a>
          </div>
        </div>
      </div>
    </b:if>

    <!-- Footer -->
    <footer>
      <p style='margin-bottom:0.4rem;'>
        <strong><data:blog.title/></strong> - Daily Government Job Notifications, Admit Cards &amp; Results Portal.
      </p>
      <p style='font-size:0.82rem; color:var(--text-muted);'>
        Disclaimer: We provide recruitment updates for informational purposes. Candidates must verify notifications on official government portals.
      </p>
    </footer>

    <!-- Interactive JS wrapped in CDATA for 100% valid XML parsing -->
    <script type='text/javascript'>
      //<![CDATA[
      function toggleDark() {
        var isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        if (isDark) {
          document.documentElement.removeAttribute('data-theme');
          document.getElementById('themeIcon').className = 'fas fa-moon';
          localStorage.setItem('jobTheme', 'light');
        } else {
          document.documentElement.setAttribute('data-theme', 'dark');
          document.getElementById('themeIcon').className = 'fas fa-sun';
          localStorage.setItem('jobTheme', 'dark');
        }
      }
      if (localStorage.getItem('jobTheme') === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
        var icon = document.getElementById('themeIcon');
        if (icon) icon.className = 'fas fa-sun';
      }

      function liveFilterJobs(query) {
        var q = (query || '').trim().toLowerCase();
        var cards = document.querySelectorAll('#jobFeedContainer .job-card');
        for (var i = 0; i < cards.length; i++) {
          var title = cards[i].innerText.toLowerCase();
          if (!q || title.indexOf(q) !== -1) {
            cards[i].style.display = 'flex';
          } else {
            cards[i].style.display = 'none';
          }
        }
      }

      function formatJobTagsAndTitles() {
        var cards = document.querySelectorAll('.job-card');
        for (var i = 0; i < cards.length; i++) {
          var card = cards[i];
          var titleEl = card.querySelector('.job-card-title');
          var tagsContainer = card.querySelector('.job-card-tags');
          if (titleEl) {
            var titleText = titleEl.innerText || '';
            if (titleText.indexOf('#') !== -1) {
              var parts = titleText.split('#');
              var cleanTitle = parts[0].trim();
              titleEl.innerText = cleanTitle;
              if (tagsContainer && tagsContainer.children.length === 0) {
                for (var j = 1; j < parts.length; j++) {
                  var tag = parts[j].replace(/,/g, '').trim();
                  if (tag) {
                    var chip = document.createElement('span');
                    chip.className = 'job-tag-chip';
                    chip.innerHTML = '<i class="fas fa-tag" style="color:var(--primary);"></i> ' + tag;
                    tagsContainer.appendChild(chip);
                  }
                }
              }
            }
          }
        }
        var singleTitle = document.querySelector('.single-post-view h1');
        if (singleTitle && singleTitle.innerText.indexOf('#') !== -1) {
          singleTitle.innerText = singleTitle.innerText.split('#')[0].trim();
        }
      }
      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', formatJobTagsAndTitles);
      } else {
        formatJobTagsAndTitles();
      }
      //]]>
    </script>
  </body>
</html>"""

def main():
    out_file = os.path.join(os.path.dirname(__file__), "job_theme.xml")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(JOB_THEME_XML.strip())

    # Strict XML validation test
    xml.sax.parseString(JOB_THEME_XML.encode('utf-8'), xml.sax.ContentHandler())
    print(f"SUCCESS: 'job_theme.xml' with full State, Sector, & Qualification grids validated with 0 errors!")

if __name__ == "__main__":
    main()
