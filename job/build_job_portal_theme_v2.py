"""
All-India Smart Government Job Portal Theme (Version 5.0)
- Mobile-First: Big, Clear, Legible Job Titles on Mobile (1.15rem, font-weight 900)
- "Filter by State & Territory" placed cleanly under the main job feed with dynamic job counts on every state card
- Removed duplicate "Jobs by State" block
- Expanded "Top Job Sectors" with all 15 major sectors + live job counts
- Every category, qualification, state, and sector shows live dynamic total job counts
- Dynamic application status badges (🟢 Live, 🟠 Closing Soon, 🔴 Expired)
- 100% Valid XML with 0 Errors
"""

import json
import os
import xml.sax
from build_150_latest_jobs import JOBS_150

THEME_TEMPLATE = r"""<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html>
<html b:css='false' b:defaultwidgetversion='2' b:layoutsversion='3' b:responsive='true' lang='en' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
  <head>
    <meta content='width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=5, viewport-fit=cover' name='viewport'/>
    <title><data:blog.pageTitle/></title>
    <b:include data='blog' name='all-head-content'/>

    <!-- Advanced SEO Meta Tags -->
    <meta content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' name='robots'/>
    <meta content='Government Jobs, Kerala PSC Notifications, Bank Recruitment, Railway RRB, SSC CGL, UPSC, 10th Pass Jobs, Central Govt Jobs, Police Recruitment' name='keywords'/>
    <meta content='Daily verified Government Job notifications, Kerala PSC, Central Govt, Banking, Railway RRB, SSC, Defence and Police recruitment updates with direct apply links.' name='description'/>
    <meta content='summary_large_image' name='twitter:card'/>
    <meta expr:content='data:blog.pageTitle' name='twitter:title'/>
    <meta content='Daily verified Government Job notifications across Kerala, Banking, Railways, SSC, and Central Govt sectors.' name='twitter:description'/>
    <meta expr:content='data:blog.canonicalUrl' property='og:url'/>
    <meta expr:content='data:blog.pageTitle' property='og:title'/>
    <meta content='website' property='og:type'/>
    <meta content='Daily verified Government Job notifications across Kerala, Banking, Railways, SSC, and Central Govt sectors.' property='og:description'/>
    <meta expr:content='data:blog.title' property='og:site_name'/>
    <link expr:href='data:blog.canonicalUrl' rel='canonical'/>

    <!-- Structured Data JSON-LD Schema (Google Search Rich Results) -->
    <script type='application/ld+json'>
    {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "Government Jobs Portal",
      "url": "https://www.example.com/",
      "potentialAction": {
        "@type": "SearchAction",
        "target": "https://www.example.com/?q={search_term_string}",
        "query-input": "required name=search_term_string"
      }
    }
    </script>

    <!-- Google Fonts -->
    <link href='https://fonts.googleapis.com' rel='preconnect'/>
    <link crossorigin='anonymous' href='https://fonts.gstatic.com' rel='preconnect'/>
    <link href='https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&amp;display=swap' rel='stylesheet'/>
    
    <!-- FontAwesome Icons -->
    <link href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css' rel='stylesheet'/>

    <b:skin><![CDATA[
      :root {
        --primary: #2563EB;
        --primary-dark: #1D4ED8;
        --primary-light: #EFF6FF;
        --secondary: #0F172A;
        --accent: #F59E0B;
        --success: #059669;
        --success-bg: #ECFDF5;
        --warning: #D97706;
        --warning-bg: #FEF3C7;
        --danger: #DC2626;
        --danger-bg: #FEE2E2;
        --bg-page: #F8FAFC;
        --bg-surface: #FFFFFF;
        --bg-card: #FFFFFF;
        --bg-card-hover: #F8FAFC;
        --text-primary: #0F172A;
        --text-secondary: #475569;
        --text-muted: #64748B;
        --border-color: #E2E8F0;
        --radius: 12px;
        --radius-sm: 8px;
        --card-shadow: 0 2px 4px rgba(0, 0, 0, 0.04), 0 1px 2px rgba(0, 0, 0, 0.03);
        --card-hover-shadow: 0 8px 16px -2px rgba(37, 99, 235, 0.08), 0 3px 6px -2px rgba(0, 0, 0, 0.04);
        --transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      }

      [data-theme='dark'] {
        --primary: #3B82F6;
        --primary-dark: #60A5FA;
        --primary-light: rgba(59, 130, 246, 0.15);
        --secondary: #F8FAFC;
        --bg-page: #0B1120;
        --bg-surface: #0F172A;
        --bg-card: #131E32;
        --bg-card-hover: #1A2742;
        --text-primary: #F8FAFC;
        --text-secondary: #94A3B8;
        --text-muted: #64748B;
        --border-color: rgba(255, 255, 255, 0.08);
        --success-bg: rgba(5, 150, 105, 0.2);
        --warning-bg: rgba(217, 119, 6, 0.2);
        --danger-bg: rgba(220, 38, 38, 0.2);
        --card-shadow: 0 3px 8px rgba(0, 0, 0, 0.3);
        --card-hover-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
      }

      * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
      }

      body {
        font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
        background-color: var(--bg-page);
        color: var(--text-primary);
        line-height: 1.6;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        overflow-x: hidden;
      }

      /* Top Header */
      header {
        background: var(--bg-surface);
        border-bottom: 1px solid var(--border-color);
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 1px 3px rgba(0,0,0,0.03);
      }

      .header-wrap {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0.75rem 1rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
      }

      .site-logo {
        display: flex;
        align-items: center;
        gap: 8px;
        font-weight: 900;
        font-size: 1.25rem;
        color: var(--text-primary);
        text-decoration: none;
        cursor: pointer;
      }
      .site-logo i { color: var(--primary); }
      .site-logo span {
        color: var(--primary);
        background: var(--primary-light);
        padding: 2px 8px;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 800;
        text-transform: uppercase;
      }

      .nav-links {
        display: flex;
        align-items: center;
        gap: 6px;
      }
      .nav-links a {
        color: var(--text-secondary);
        text-decoration: none;
        font-weight: 700;
        font-size: 0.88rem;
        padding: 6px 12px;
        border-radius: 8px;
        transition: var(--transition);
        cursor: pointer;
      }
      .nav-links a:hover, .nav-links a.active {
        color: var(--primary);
        background: var(--primary-light);
      }

      @media (max-width: 768px) {
        .nav-links { display: none; }
      }

      .theme-btn {
        background: var(--bg-page);
        border: 1px solid var(--border-color);
        color: var(--text-primary);
        width: 38px;
        height: 38px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: var(--transition);
      }
      .theme-btn:hover {
        background: var(--primary-light);
        color: var(--primary);
      }

      /* Ultra-Modern Eyecatching Hero Header */
      .job-hero {
        background: radial-gradient(circle at 15% 20%, rgba(99, 102, 241, 0.35) 0%, transparent 45%),
                    radial-gradient(circle at 85% 80%, rgba(59, 130, 246, 0.35) 0%, transparent 45%),
                    radial-gradient(circle at 50% 50%, rgba(37, 99, 235, 0.2) 0%, transparent 60%),
                    linear-gradient(135deg, #071228 0%, #0F2756 40%, #1E3A8A 75%, #2563EB 100%);
        color: #FFFFFF;
        padding: 3.25rem 1rem 2.25rem;
        text-align: center;
        position: relative;
        overflow: hidden;
        border-bottom: 1px solid rgba(255, 255, 255, 0.12);
      }
      .job-hero::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: radial-gradient(rgba(255, 255, 255, 0.1) 1px, transparent 1px);
        background-size: 24px 24px;
        opacity: 0.5;
        pointer-events: none;
      }
      .hero-live-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.28);
        padding: 6px 18px;
        border-radius: 50px;
        font-size: 0.78rem;
        font-weight: 800;
        letter-spacing: 0.6px;
        text-transform: uppercase;
        color: #FFFFFF;
        margin-bottom: 0.85rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        position: relative;
        z-index: 2;
      }
      .live-pulse-dot {
        width: 9px;
        height: 9px;
        background: #10B981;
        border-radius: 50%;
        display: inline-block;
        box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
        animation: pulseLive 1.8s infinite cubic-bezier(0.66, 0, 0, 1);
      }
      @keyframes pulseLive {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
        70% { transform: scale(1); box-shadow: 0 0 0 9px rgba(16, 185, 129, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
      }
      .job-hero-title {
        font-size: clamp(1.65rem, 4.5vw, 2.6rem);
        font-weight: 900;
        margin-bottom: 0.5rem;
        letter-spacing: -0.6px;
        line-height: 1.25;
        text-shadow: 0 2px 12px rgba(0, 0, 0, 0.35);
        position: relative;
        z-index: 2;
      }
      .job-hero-title span.highlight-year {
        background: linear-gradient(90deg, #FDE047 0%, #F59E0B 50%, #38BDF8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
      }
      .job-hero-sub {
        font-size: clamp(0.88rem, 2.2vw, 1.05rem);
        opacity: 0.95;
        max-width: 680px;
        margin: 0 auto 1.4rem;
        line-height: 1.6;
        color: #E2E8F0;
        font-weight: 500;
        position: relative;
        z-index: 2;
      }

      /* Hero Search Box */
      .hero-search-box {
        max-width: 660px;
        margin: 0 auto;
        position: relative;
        z-index: 3;
      }
      .hero-search-box input {
        width: 100%;
        height: 52px;
        border-radius: 50px;
        border: 2px solid rgba(255, 255, 255, 0.5);
        background: #FFFFFF;
        color: #0F172A;
        padding: 0 3.2rem 0 3.2rem;
        font-size: 0.98rem;
        font-weight: 600;
        outline: none;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
        transition: var(--transition);
      }
      .hero-search-box input:focus {
        border-color: #60A5FA;
        box-shadow: 0 12px 35px rgba(37, 99, 235, 0.4), 0 0 0 4px rgba(96, 165, 250, 0.3);
      }
      .hero-search-box .search-icon {
        position: absolute;
        left: 1.25rem;
        top: 50%;
        transform: translateY(-50%);
        color: #2563EB;
        font-size: 1.2rem;
      }
      .hero-search-box .clear-btn {
        position: absolute;
        right: 1.25rem;
        top: 50%;
        transform: translateY(-50%);
        background: none;
        border: none;
        color: #94A3B8;
        font-size: 1.15rem;
        cursor: pointer;
        display: none;
        padding: 4px;
        transition: var(--transition);
      }
      .hero-search-box .clear-btn:hover { color: #DC2626; }

      /* Quick Popular Search Tags */
      .hero-popular-tags {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        gap: 6px;
        margin-top: 1rem;
        font-size: 0.8rem;
        position: relative;
        z-index: 2;
      }
      .hero-popular-tags span.label {
        color: rgba(255, 255, 255, 0.85);
        font-weight: 800;
        margin-right: 2px;
      }
      .pop-tag {
        background: rgba(255, 255, 255, 0.14);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.25);
        color: #FFFFFF;
        padding: 3px 12px;
        border-radius: 20px;
        text-decoration: none;
        font-weight: 700;
        transition: var(--transition);
        cursor: pointer;
      }
      .pop-tag:hover {
        background: #FFFFFF;
        color: #1E3A8A;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
      }

      /* Category Pills Bar (Horizontal Scroll with Count Badges) */
      .job-cat-bar {
        background: var(--bg-surface);
        border-bottom: 1px solid var(--border-color);
        padding: 0.65rem 0;
        position: sticky;
        top: 55px;
        z-index: 90;
      }
      .job-cat-track {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
        display: flex;
        align-items: center;
        gap: 8px;
        overflow-x: auto;
        white-space: nowrap;
        scrollbar-width: none;
      }
      .job-cat-track::-webkit-scrollbar { display: none; }

      .job-cat-pill {
        background: var(--bg-page);
        color: var(--text-primary);
        border: 1px solid var(--border-color);
        padding: 5px 12px;
        border-radius: 50px;
        font-size: 0.82rem;
        font-weight: 700;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        cursor: pointer;
        transition: var(--transition);
      }
      .job-cat-pill:hover, .job-cat-pill.active {
        background: var(--primary);
        color: #FFFFFF !important;
        border-color: var(--primary);
        box-shadow: 0 3px 10px rgba(37,99,235,0.22);
      }
      .pill-count {
        background: rgba(0, 0, 0, 0.08);
        font-size: 0.72rem;
        padding: 1px 6px;
        border-radius: 20px;
        font-weight: 800;
      }
      .job-cat-pill.active .pill-count {
        background: rgba(255, 255, 255, 0.25);
        color: #FFFFFF;
      }
      .job-cat-pill.pill-today {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.12) 0%, rgba(245, 158, 11, 0.15) 100%);
        border-color: #F59E0B;
        color: #D97706;
        font-weight: 800;
      }
      .job-cat-pill.pill-today:hover, .job-cat-pill.pill-today.active {
        background: linear-gradient(135deg, #EF4444 0%, #F59E0B 100%) !important;
        color: #FFFFFF !important;
        border-color: transparent !important;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.35);
      }
      .job-cat-pill.pill-saved {
        border-color: #F59E0B;
        color: #D97706;
      }
      .job-cat-pill.pill-saved:hover, .job-cat-pill.pill-saved.active {
        background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%) !important;
        border-color: #D97706 !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.35);
      }
      .badge-today {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        background: linear-gradient(135deg, #EF4444 0%, #F59E0B 100%);
        color: #FFFFFF;
        font-size: 0.68rem;
        font-weight: 900;
        padding: 2px 7px;
        border-radius: 4px;
        text-transform: uppercase;
        letter-spacing: 0.4px;
        box-shadow: 0 2px 6px rgba(239, 68, 68, 0.3);
        animation: pulseToday 2s infinite ease-in-out;
      }
      @keyframes pulseToday {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.88; transform: scale(1.03); }
      }

      /* Breaking Live Alerts Marquee Ribbon */
      .breaking-ticker-ribbon {
        background: linear-gradient(90deg, #1E1B4B 0%, #312E81 50%, #1E3A8A 100%);
        color: #FFFFFF;
        border-bottom: 1px solid rgba(255, 255, 255, 0.12);
        font-size: 0.82rem;
        overflow: hidden;
        position: relative;
        z-index: 95;
      }
      .ticker-inner {
        max-width: 1200px;
        margin: 0 auto;
        padding: 6px 1rem;
        display: flex;
        align-items: center;
        gap: 12px;
      }
      .ticker-badge {
        background: #EF4444;
        color: #FFFFFF;
        font-weight: 900;
        font-size: 0.72rem;
        padding: 3px 10px;
        border-radius: 4px;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        white-space: nowrap;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        box-shadow: 0 2px 8px rgba(239, 68, 68, 0.4);
        flex-shrink: 0;
      }
      .ticker-dot {
        width: 6px;
        height: 6px;
        background: #FFFFFF;
        border-radius: 50%;
        animation: pulseTicker 1.5s infinite;
      }
      @keyframes pulseTicker {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.3; transform: scale(0.8); }
      }
      .ticker-scroll-track {
        display: flex;
        align-items: center;
        gap: 24px;
        overflow-x: auto;
        white-space: nowrap;
        scrollbar-width: none;
      }
      .ticker-scroll-track::-webkit-scrollbar { display: none; }
      .ticker-item {
        color: #F8FAFC;
        text-decoration: none;
        font-weight: 700;
        transition: var(--transition);
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 6px;
      }
      .ticker-item:hover {
        color: #FDE047;
        text-decoration: underline;
      }

      /* Portal Content Channels (Notifications, Admit Cards, Results, Answer Keys, Syllabus, Saved) */
      .portal-channels-bar {
        background: var(--bg-surface);
        border-bottom: 2px solid var(--border-color);
        padding: 0.5rem 0;
      }
      .portal-channels-track {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
        display: flex;
        align-items: center;
        gap: 6px;
        overflow-x: auto;
        white-space: nowrap;
        scrollbar-width: none;
      }
      .portal-channels-track::-webkit-scrollbar { display: none; }
      .channel-tab {
        background: var(--bg-page);
        color: var(--text-secondary);
        border: 1.5px solid var(--border-color);
        padding: 7px 14px;
        border-radius: 8px;
        font-size: 0.84rem;
        font-weight: 800;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 7px;
        transition: var(--transition);
      }
      .channel-tab:hover {
        background: var(--primary-light);
        color: var(--primary);
        border-color: var(--primary);
      }
      .channel-tab.active {
        background: var(--primary);
        color: #FFFFFF !important;
        border-color: var(--primary);
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.28);
      }
      .channel-tab .ch-cnt {
        background: rgba(0, 0, 0, 0.08);
        font-size: 0.72rem;
        padding: 2px 7px;
        border-radius: 12px;
        font-weight: 900;
      }
      .channel-tab.active .ch-cnt {
        background: rgba(255, 255, 255, 0.28);
        color: #FFFFFF;
      }
      .channel-tab.tab-saved {
        border-color: #F59E0B;
        color: #D97706;
      }
      .channel-tab.tab-saved.active {
        background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%) !important;
        border-color: #D97706;
        color: #FFFFFF !important;
      }

      /* Interactive Instant Eligibility & Age Matcher */
      .eligibility-calculator-card {
        background: var(--bg-card);
        border: 1.5px solid var(--border-color);
        border-radius: var(--radius);
        padding: 1rem 1.15rem;
        margin-bottom: 0.85rem;
        box-shadow: var(--card-shadow);
        transition: var(--transition);
      }
      .calc-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        cursor: pointer;
      }
      .calc-toggle-btn {
        background: var(--bg-page);
        border: 1px solid var(--border-color);
        color: var(--text-primary);
        width: 28px;
        height: 28px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        font-size: 0.8rem;
      }
      .calc-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 10px;
        margin: 0.85rem 0;
      }
      .calc-field label {
        display: block;
        font-size: 0.74rem;
        font-weight: 800;
        color: var(--text-secondary);
        margin-bottom: 4px;
        text-transform: uppercase;
        letter-spacing: 0.3px;
      }
      .calc-field select, .calc-field input {
        width: 100%;
        padding: 7px 10px;
        border-radius: 8px;
        border: 1.5px solid var(--border-color);
        background: var(--bg-page);
        color: var(--text-primary);
        font-weight: 700;
        font-size: 0.84rem;
        outline: none;
        transition: var(--transition);
      }
      .calc-field select:focus, .calc-field input:focus {
        border-color: var(--primary);
        box-shadow: 0 0 0 3px rgba(37,99,235,0.15);
      }
      .calc-actions {
        display: flex;
        align-items: center;
        gap: 8px;
        flex-wrap: wrap;
        padding-top: 0.5rem;
        border-top: 1px dashed var(--border-color);
      }
      .calc-btn-find {
        background: var(--primary);
        color: #FFFFFF;
        border: none;
        padding: 7px 16px;
        border-radius: 6px;
        font-weight: 800;
        font-size: 0.82rem;
        cursor: pointer;
        transition: var(--transition);
      }
      .calc-btn-find:hover {
        background: var(--primary-dark);
        box-shadow: 0 4px 12px rgba(37,99,235,0.3);
      }
      .calc-btn-reset {
        background: var(--bg-page);
        border: 1px solid var(--border-color);
        color: var(--text-secondary);
        padding: 7px 12px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.82rem;
        cursor: pointer;
      }
      .calc-btn-reset:hover {
        color: var(--danger);
      }

      /* Type Chips */
      .type-chip {
        font-size: 0.7rem;
        font-weight: 800;
        padding: 2px 7px;
        border-radius: 4px;
        text-transform: uppercase;
        letter-spacing: 0.3px;
        display: inline-flex;
        align-items: center;
        gap: 3px;
      }
      .chip-notif { background: #DBEAFE; color: #1E40AF; }
      .chip-admit { background: #F3E8FF; color: #6B21A8; }
      .chip-result { background: #D1FAE5; color: #065F46; }
      .chip-ans { background: #FEF3C7; color: #92400E; }
      .chip-syl { background: #E0E7FF; color: #3730A3; }
      [data-theme='dark'] .chip-notif { background: rgba(30, 64, 175, 0.3); color: #93C5FD; }
      [data-theme='dark'] .chip-admit { background: rgba(107, 33, 168, 0.3); color: #D8B4FE; }
      [data-theme='dark'] .chip-result { background: rgba(6, 95, 70, 0.3); color: #6EE7B7; }
      [data-theme='dark'] .chip-ans { background: rgba(146, 64, 14, 0.3); color: #FDE68A; }
      [data-theme='dark'] .chip-syl { background: rgba(55, 48, 163, 0.3); color: #A5B4FC; }

      /* Bookmark Star Button */
      .bookmark-btn {
        background: none;
        border: none;
        color: var(--text-muted);
        font-size: 1.05rem;
        cursor: pointer;
        padding: 4px 6px;
        border-radius: 6px;
        transition: var(--transition);
        display: flex;
        align-items: center;
        justify-content: center;
      }
      .bookmark-btn:hover {
        color: #F59E0B;
        transform: scale(1.15);
      }
      .bookmark-btn.saved, .bookmark-btn.saved i, .bookmark-btn i.saved {
        color: #F59E0B !important;
      }

      /* Layout */
      .portal-layout {
        max-width: 1200px;
        margin: 1.25rem auto 1.5rem;
        padding: 0 14px;
        display: grid;
        grid-template-columns: 1fr 330px;
        gap: 1.5rem;
        flex: 1;
        width: 100%;
      }

      @media (max-width: 920px) {
        .portal-layout {
          grid-template-columns: 1fr;
          margin: 0.85rem auto 1.5rem;
          padding: 0 12px;
        }
      }

      /* Minimal, Clear, High-Legibility Job Cards */
      .job-feed {
        display: flex;
        flex-direction: column;
        gap: 0.65rem;
      }

      .results-count-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        font-size: 0.85rem;
        font-weight: 700;
        color: var(--text-muted);
        padding: 0 2px 6px;
      }

      .saved-header-banner {
        background: linear-gradient(135deg, #FEF3C7 0%, #FFFBEB 100%);
        border: 1.5px solid #F59E0B;
        border-radius: var(--radius);
        padding: 0.95rem 1rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 10px;
        margin-bottom: 0.85rem;
        box-shadow: var(--card-shadow);
      }

      .job-card {
        background: var(--bg-card);
        border: 1.5px solid var(--border-color);
        border-radius: var(--radius);
        padding: 0.95rem 1rem;
        box-shadow: var(--card-shadow);
        text-decoration: none;
        color: inherit;
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        transition: var(--transition);
        cursor: pointer;
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
      .job-card-badges {
        display: flex;
        align-items: center;
        gap: 6px;
        flex-wrap: wrap;
        flex: 1;
        min-width: 0;
      }
      .job-card-actions {
        display: flex;
        align-items: center;
        gap: 6px;
        flex-shrink: 0;
        margin-left: auto;
      }
      .job-org-badge {
        font-size: 0.75rem;
        font-weight: 800;
        color: var(--primary);
        background: var(--primary-light);
        padding: 3px 8px;
        border-radius: 6px;
        text-transform: uppercase;
        letter-spacing: 0.3px;
        display: inline-flex;
        align-items: center;
        gap: 4px;
      }
      [data-theme='dark'] .job-org-badge {
        background: rgba(37,99,235,0.2);
        color: #93C5FD;
      }

      /* Dynamic Date Badges (Live = Green, Ending Soon = Orange, Closed = Red) */
      .status-badge {
        font-size: 0.75rem;
        font-weight: 800;
        padding: 3px 9px;
        border-radius: 6px;
        display: inline-flex;
        align-items: center;
        gap: 4px;
        white-space: nowrap;
      }
      .status-live {
        color: var(--success);
        background: var(--success-bg);
      }
      .status-closing {
        color: var(--warning);
        background: var(--warning-bg);
      }
      .status-closed {
        color: var(--danger);
        background: var(--danger-bg);
      }

      /* Job Title: Clear, Bold & Highly Legible */
      .job-card-title {
        font-size: 1.06rem;
        font-weight: 800;
        color: var(--text-primary);
        line-height: 1.35;
        margin: 0;
      }

      .job-card-bottom {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 8px;
        flex-wrap: wrap;
        margin-top: 2px;
      }
      .job-qual-chip {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        background: var(--bg-page);
        color: var(--text-secondary);
        border: 1px solid var(--border-color);
        padding: 3px 9px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.78rem;
      }
      .job-read-link {
        font-size: 0.82rem;
        font-weight: 800;
        color: var(--primary);
        display: inline-flex;
        align-items: center;
        gap: 3px;
        white-space: nowrap;
        margin-left: auto;
      }

      /* Mobile Overrides: Symmetrical, Uniform Gutter Margins */
      @media (max-width: 600px) {
        .header-wrap { padding: 0.5rem 12px; }
        .site-logo { font-size: 1.1rem; }
        .ticker-inner { padding: 6px 12px; }
        .job-hero { padding: 1.4rem 12px 1.15rem; }
        .job-cat-track { padding: 0 12px; }
        .portal-layout { padding: 0 12px; margin: 0.75rem auto 1.25rem; }
        .state-cards-section, .bank-cards-section { padding: 0 12px; }
        .quick-browse-grid { padding: 0 12px; }
        .hero-search-box input { height: 42px; font-size: 0.88rem; }
        .saved-header-banner { padding: 0.85rem; }
        .job-card { padding: 0.85rem; }
        .job-card-title { font-size: 1.12rem !important; font-weight: 900 !important; line-height: 1.32 !important; }
        .full-job-article { padding: 1.15rem 0.85rem; }
        .results-count-bar { padding: 0 2px 6px; }
      }

      /* Pagination Controls */
      .pagination-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
        margin-top: 1.25rem;
        flex-wrap: wrap;
      }
      .page-btn {
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        color: var(--text-primary);
        padding: 7px 14px;
        border-radius: 8px;
        font-size: 0.85rem;
        font-weight: 700;
        cursor: pointer;
        transition: var(--transition);
        min-width: 38px;
        text-align: center;
      }
      .page-btn:hover, .page-btn.active {
        background: var(--primary);
        color: #FFFFFF;
        border-color: var(--primary);
        box-shadow: 0 3px 8px rgba(37,99,235,0.25);
      }
      .page-btn.disabled {
        opacity: 0.4;
        cursor: not-allowed;
        pointer-events: none;
      }

      /* State Emoji Compact Cards Grid (Clean Section Placed Below Job Feed) */
      .state-cards-section {
        max-width: 1200px;
        margin: 1.5rem auto 2.5rem;
        padding: 0 1rem;
        width: 100%;
      }
      .state-section-card {
        background: var(--bg-card);
        border: 1.5px solid var(--border-color);
        border-radius: var(--radius);
        padding: 1.25rem;
        box-shadow: var(--card-shadow);
      }
      .section-heading-sm {
        font-size: 1rem;
        font-weight: 900;
        color: var(--text-primary);
        margin-bottom: 0.85rem;
        display: flex;
        align-items: center;
        gap: 8px;
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 0.4rem;
      }
      .state-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
        gap: 8px;
      }
      .state-card {
        background: var(--bg-page);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-sm);
        padding: 7px 10px;
        text-align: center;
        font-size: 0.82rem;
        font-weight: 700;
        color: var(--text-primary);
        cursor: pointer;
        text-decoration: none;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 4px;
        transition: var(--transition);
      }
      .state-card:hover, .state-card.active {
        background: var(--primary-light);
        color: var(--primary);
        border-color: var(--primary);
        transform: translateY(-1px);
      }
      [data-theme='dark'] .state-card:hover, [data-theme='dark'] .state-card.active {
        background: rgba(37,99,235,0.22);
        color: #93C5FD;
        border-color: #3B82F6;
      }
      .state-count {
        font-size: 0.72rem;
        font-weight: 800;
        color: var(--text-muted);
        background: rgba(0,0,0,0.06);
        padding: 1px 6px;
        border-radius: 12px;
      }
      [data-theme='dark'] .state-count {
        background: rgba(255,255,255,0.1);
        color: #94A3B8;
      }
      .state-card.active .state-count {
        background: var(--primary);
        color: #FFFFFF;
      }

      .toggle-states-btn {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: var(--bg-page);
        border: 1.5px solid var(--primary);
        color: var(--primary);
        padding: 7px 20px;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 800;
        cursor: pointer;
        margin-top: 1rem;
        transition: var(--transition);
      }
      .toggle-states-btn:hover {
        background: var(--primary);
        color: #FFFFFF;
      }

      /* Bank & Financial Institutions Compact Cards Grid */
      .bank-cards-section {
        max-width: 1200px;
        margin: 1.5rem auto 1.5rem;
        padding: 0 1rem;
        width: 100%;
      }
      .bank-section-card {
        background: var(--bg-card);
        border: 1.5px solid var(--border-color);
        border-radius: var(--radius);
        padding: 1.25rem;
        box-shadow: var(--card-shadow);
      }
      .bank-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(138px, 1fr));
        gap: 8px;
      }
      .bank-card {
        background: var(--bg-page);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-sm);
        padding: 7px 10px;
        text-align: center;
        font-size: 0.82rem;
        font-weight: 700;
        color: var(--text-primary);
        cursor: pointer;
        text-decoration: none;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 4px;
        transition: var(--transition);
      }
      .bank-card:hover, .bank-card.active {
        background: var(--primary-light);
        color: var(--primary);
        border-color: var(--primary);
        transform: translateY(-1px);
      }
      [data-theme='dark'] .bank-card:hover, [data-theme='dark'] .bank-card.active {
        background: rgba(37,99,235,0.22);
        color: #93C5FD;
        border-color: #3B82F6;
      }
      .bank-count {
        font-size: 0.72rem;
        font-weight: 800;
        color: var(--text-muted);
        background: rgba(0,0,0,0.06);
        padding: 1px 6px;
        border-radius: 12px;
      }
      [data-theme='dark'] .bank-count {
        background: rgba(255,255,255,0.1);
        color: #94A3B8;
      }
      .bank-card.active .bank-count {
        background: var(--primary);
        color: #FFFFFF;
      }
      .toggle-banks-btn {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: var(--bg-page);
        border: 1.5px solid var(--primary);
        color: var(--primary);
        padding: 7px 20px;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 800;
        cursor: pointer;
        margin-top: 1rem;
        transition: var(--transition);
      }
      .toggle-banks-btn:hover {
        background: var(--primary);
        color: #FFFFFF;
      }

      /* Dedicated Full-Page Article View */
      .full-job-article {
        background: var(--bg-card);
        border: 1.5px solid var(--border-color);
        border-radius: var(--radius);
        padding: 1.75rem 1.5rem;
        box-shadow: var(--card-shadow);
        width: 100%;
        display: none;
      }
      .back-nav-bar {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 18px;
        background: var(--bg-page);
        border: 1.5px solid var(--border-color);
        border-radius: 50px;
        font-weight: 800;
        color: var(--primary);
        text-decoration: none;
        font-size: 0.9rem;
        margin-bottom: 1.25rem;
        cursor: pointer;
        transition: var(--transition);
      }
      .back-nav-bar:hover {
        background: var(--primary);
        color: #FFFFFF;
        border-color: var(--primary);
      }

      .article-table {
        width: 100%;
        border-collapse: collapse;
        margin: 1rem 0 1.5rem;
      }
      .article-table tr {
        border-bottom: 1px solid var(--border-color);
      }
      .article-table td {
        padding: 10px 8px;
        font-size: 0.92rem;
        vertical-align: top;
      }
      .article-table td:first-child {
        font-weight: 700;
        color: var(--text-secondary);
        width: 36%;
      }
      .article-table td:last-child {
        font-weight: 800;
        color: var(--text-primary);
      }

      .share-bar {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin: 1.25rem 0 1rem;
        padding: 0.9rem;
        background: var(--bg-page);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        align-items: center;
      }
      .share-btn {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 8px 14px;
        border-radius: 50px;
        font-size: 0.82rem;
        font-weight: 700;
        color: #FFFFFF !important;
        text-decoration: none;
        transition: var(--transition);
      }
      .btn-whatsapp { background: #25D366; }
      .btn-telegram { background: #0088CC; }
      .btn-copy { background: #64748B; cursor: pointer; border: none; }

      /* Related Jobs Section (Under the Post) */
      .related-jobs-box {
        margin-top: 2.2rem;
        padding-top: 1.5rem;
        border-top: 2px solid var(--border-color);
      }
      .related-jobs-title {
        font-size: 1.15rem;
        font-weight: 900;
        color: var(--primary);
        margin-bottom: 0.9rem;
        display: flex;
        align-items: center;
        gap: 6px;
      }
      .related-jobs-list {
        display: flex;
        flex-direction: column;
        gap: 0.6rem;
      }

      /* Quick Browse Hubs (Qualifications & Sectors) */
      .quick-browse-grid {
        max-width: 1200px;
        margin: 0 auto 2.5rem;
        padding: 0 1rem;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 1.25rem;
        width: 100%;
      }
      .browse-block {
        background: var(--bg-card);
        border: 1.5px solid var(--border-color);
        border-radius: var(--radius);
        padding: 1.25rem 1.1rem;
        box-shadow: var(--card-shadow);
      }
      .browse-header {
        font-size: 0.98rem;
        font-weight: 800;
        color: var(--text-primary);
        margin-bottom: 0.85rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 0.45rem;
      }
      .browse-chips {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
      }
      .browse-chip {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        padding: 4px 10px;
        background: var(--bg-page);
        color: var(--text-secondary);
        border: 1px solid var(--border-color);
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 700;
        text-decoration: none;
        cursor: pointer;
        transition: var(--transition);
      }
      .browse-chip:hover {
        background: var(--primary);
        color: #FFFFFF;
        border-color: var(--primary);
      }
      .browse-chip .chip-cnt {
        font-size: 0.7rem;
        opacity: 0.85;
      }

      /* Sidebar */
      .sidebar-card {
        background: var(--bg-card);
        border: 1.5px solid var(--border-color);
        border-radius: var(--radius);
        padding: 1.2rem;
        margin-bottom: 1.25rem;
        box-shadow: var(--card-shadow);
      }
      .sidebar-title {
        font-size: 1.02rem;
        font-weight: 800;
        margin-bottom: 0.75rem;
        border-bottom: 2px solid var(--primary);
        padding-bottom: 0.4rem;
        color: var(--text-primary);
        display: flex;
        align-items: center;
        gap: 6px;
      }
      .telegram-cta {
        background: linear-gradient(135deg, #0284C7 0%, #0369A1 100%);
        color: #FFFFFF !important;
        border-radius: var(--radius);
        padding: 1.35rem;
        text-align: center;
        margin-bottom: 1.25rem;
        box-shadow: 0 4px 15px rgba(2,132,199,0.2);
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
        font-size: 0.84rem;
        cursor: pointer;
        transition: var(--transition);
      }
      .category-list a:hover {
        background: var(--primary);
        color: #FFFFFF;
        border-color: var(--primary);
      }

      /* Footer */
      footer {
        background: var(--bg-surface);
        border-top: 1px solid var(--border-color);
        padding: 2rem 1rem;
        text-align: center;
        font-size: 0.85rem;
        color: var(--text-secondary);
      }
      footer a { color: var(--primary); text-decoration: none; font-weight: 700; }
    ]]></b:skin>
  </head>
  <body>
    <!-- Top Header -->
    <header>
      <div class='header-wrap'>
        <a class='site-logo' href='javascript:void(0)' onclick='showAllJobsView()'>
          <i class='fas fa-briefcase'/> <data:blog.title/> <span>LIVE <span class='dyn-year'>2026</span></span>
        </a>
        <div style='display:flex; align-items:center; gap:8px;'>
          <nav class='nav-links'>
            <a class='active' href='javascript:void(0)' onclick='showAllJobsView()'>Home</a>
            <a href='javascript:void(0)' onclick='filterTodayJobs()'>⚡ Added Today</a>
            <a href='javascript:void(0)' onclick='switchPortalType("notification")'>📢 Notifications</a>
            <a href='javascript:void(0)' onclick='switchPortalType("admit_card")'>🎫 Admit Cards</a>
            <a href='javascript:void(0)' onclick='switchPortalType("result")'>🏆 Results</a>
            <a href='javascript:void(0)' onclick='switchPortalType("saved")' style='color:#F59E0B;'>⭐ Saved (<span id='navSavedCount'>0</span>)</a>
          </nav>
          <button class='theme-btn' onclick='toggleDark()' title='Toggle Theme' type='button'>
            <i class='fas fa-moon' id='themeIcon'/>
          </button>
        </div>
      </div>
    </header>

    <!-- Breaking Live Alerts Marquee Ribbon -->
    <div class='breaking-ticker-ribbon'>
      <div class='ticker-inner'>
        <div class='ticker-badge'>
          <span class='ticker-dot'/> ⚡ LIVE FLASH:
        </div>
        <div class='ticker-scroll-track' id='tickerTrack'>
          <a class='ticker-item' href='javascript:void(0)' onclick='quickSearch("Kerala PSC LDC")'>📢 Kerala PSC LDC Ranked List &amp; Cutoff Marks Published</a>
          <a class='ticker-item' href='javascript:void(0)' onclick='quickSearch("SBI Clerk")'>🎫 SBI Junior Associates Prelims Hall Ticket 2026 Live</a>
          <a class='ticker-item' href='javascript:void(0)' onclick='quickSearch("Railway RRB")'>🚆 RRB NTPC CBT-1 Exam City Slip &amp; Date Out</a>
          <a class='ticker-item' href='javascript:void(0)' onclick='quickSearch("SSC CGL")'>📝 SSC CGL 2026 Tier-1 Official Provisional Answer Key Live</a>
          <a class='ticker-item' href='javascript:void(0)' onclick='quickSearch("Indian Army Agniveer")'>🎖️ Indian Army Agniveer Rally 2026 Admit Card Released</a>
          <a class='ticker-item' href='javascript:void(0)' onclick='quickSearch("UPSC Civil Services")'>🏆 UPSC Civil Services CSE Final Selection Result PDF</a>
        </div>
      </div>
    </div>

    <!-- Hero Search -->
    <div id='heroSearchSection'>
      <div class='job-hero'>
        <!-- Luminous Live Pulse Badge -->
        <div class='hero-live-badge'>
          <span class='live-pulse-dot'/> LIVE UPDATES <span class='dyn-year'>2026</span> • <span id='heroActiveCount'>150+</span> ACTIVE POSTS
        </div>

        <h1 class='job-hero-title'>
          Government Job Notifications <span class='highlight-year dyn-year'>2026</span>
        </h1>
        <p class='job-hero-sub'>
          Daily verified Kerala PSC, Central Govt, Banking, Railway, SSC &amp; Police recruitment updates.
        </p>

        <!-- Glassmorphic Search Box with Clear Button -->
        <div class='hero-search-box'>
          <i class='fas fa-search search-icon'/>
          <input id='jobSearch' oninput='liveFilterJobs(this.value)' placeholder='Search Kerala PSC, Bank, Railway, SSC, 10th Pass, Degree...' type='text'/>
          <button class='clear-btn' id='searchClearBtn' onclick='clearSearch()' title='Clear Search' type='button'>
            <i class='fas fa-times-circle'/>
          </button>
        </div>

        <!-- Quick Trending Search Tags -->
        <div class='hero-popular-tags'>
          <span class='label'>🔥 Popular:</span>
          <a class='pop-tag' href='javascript:void(0)' onclick='filterTodayJobs()'>⚡ Added Today</a>
          <a class='pop-tag' href='javascript:void(0)' onclick='quickSearch("Kerala PSC")'>🌴 Kerala PSC</a>
          <a class='pop-tag' href='javascript:void(0)' onclick='quickSearch("SBI")'>🏦 SBI PO &amp; Clerk</a>
          <a class='pop-tag' href='javascript:void(0)' onclick='quickSearch("Railway")'>🚆 RRB NTPC</a>
          <a class='pop-tag' href='javascript:void(0)' onclick='quickSearch("SSC")'>📋 SSC CGL</a>
          <a class='pop-tag' href='javascript:void(0)' onclick='quickSearch("10th Pass")'>🎓 10th Pass</a>
          <a class='pop-tag' href='javascript:void(0)' onclick='quickSearch("Defence")'>🎖️ Defence</a>
        </div>
      </div>

      <!-- Single Unified Fast Channels & Category Filter Bar (Second Position) -->
      <div class='job-cat-bar'>
        <div class='job-cat-track' id='categoryPillsTrack'>
          <a class='job-cat-pill active' data-channel='all' href='javascript:void(0)' onclick='switchPortalType("all")'>⚡ All Updates <span class='pill-count' id='cnt-all'>0</span></a>
          <a class='job-cat-pill' data-channel='notification' href='javascript:void(0)' onclick='switchPortalType("notification")'>📢 Notifications <span class='pill-count' id='cnt-notif'>0</span></a>
          <a class='job-cat-pill' data-channel='admit_card' href='javascript:void(0)' onclick='switchPortalType("admit_card")'>🎫 Admit Cards <span class='pill-count' id='cnt-admit'>0</span></a>
          <a class='job-cat-pill' data-channel='result' href='javascript:void(0)' onclick='switchPortalType("result")'>🏆 Results <span class='pill-count' id='cnt-res'>0</span></a>
          <a class='job-cat-pill' data-channel='answer_key' href='javascript:void(0)' onclick='switchPortalType("answer_key")'>📝 Answer Keys <span class='pill-count' id='cnt-ans'>0</span></a>
          <a class='job-cat-pill' data-channel='syllabus' href='javascript:void(0)' onclick='switchPortalType("syllabus")'>📚 Syllabus <span class='pill-count' id='cnt-syl'>0</span></a>
          <a class='job-cat-pill pill-saved' data-channel='saved' href='javascript:void(0)' onclick='switchPortalType("saved")'>⭐ Saved (<span id='cnt-saved'>0</span>)</a>
          <a class='job-cat-pill pill-today' data-filter='today' href='javascript:void(0)' onclick='filterTodayJobs()'>🆕 Added Today <span class='pill-count' id='cnt-today'>0</span></a>
          <a class='job-cat-pill' data-filter='Kerala Govt Jobs' href='javascript:void(0)' onclick='filterByLabel("Kerala Govt Jobs")'>🌴 Kerala Govt <span class='pill-count' id='cnt-kerala'>0</span></a>
          <a class='job-cat-pill' data-filter='Kerala PSC' href='javascript:void(0)' onclick='filterByLabel("Kerala PSC")'>📜 Kerala PSC <span class='pill-count' id='cnt-kpsc'>0</span></a>
          <a class='job-cat-pill' data-filter='Bank Jobs' href='javascript:void(0)' onclick='filterByLabel("Bank Jobs")'>🏦 Banking <span class='pill-count' id='cnt-bank'>0</span></a>
          <a class='job-cat-pill' data-filter='Railway Jobs' href='javascript:void(0)' onclick='filterByLabel("Railway Jobs")'>🚆 Railway <span class='pill-count' id='cnt-railway'>0</span></a>
          <a class='job-cat-pill' data-filter='SSC CGL' href='javascript:void(0)' onclick='filterByLabel("SSC CGL")'>📋 SSC &amp; UPSC <span class='pill-count' id='cnt-ssc'>0</span></a>
          <a class='job-cat-pill' data-filter='Defence Jobs' href='javascript:void(0)' onclick='filterByLabel("Defence Jobs")'>🎖️ Defence <span class='pill-count' id='cnt-defence'>0</span></a>
          <a class='job-cat-pill' data-filter='Police Jobs' href='javascript:void(0)' onclick='filterByLabel("Police Jobs")'>👮 Police <span class='pill-count' id='cnt-police'>0</span></a>
          <a class='job-cat-pill' data-filter='PSU Jobs' href='javascript:void(0)' onclick='filterByLabel("PSU Jobs")'>⚙️ PSU Jobs <span class='pill-count' id='cnt-psu'>0</span></a>
          <a class='job-cat-pill' data-filter='Central Govt Jobs' href='javascript:void(0)' onclick='filterByLabel("Central Govt Jobs")'>📮 India Post <span class='pill-count' id='cnt-post'>0</span></a>
          <a class='job-cat-pill' data-filter='10th Pass' href='javascript:void(0)' onclick='filterByLabel("10th Pass")'>🎓 10th Pass <span class='pill-count' id='cnt-10th'>0</span></a>
          <a class='job-cat-pill' data-filter='12th Pass' href='javascript:void(0)' onclick='filterByLabel("12th Pass")'>🎓 12th Pass <span class='pill-count' id='cnt-12th'>0</span></a>
          <a class='job-cat-pill' data-filter='Degree Jobs' href='javascript:void(0)' onclick='filterByLabel("Degree Jobs")'>🎓 Any Degree <span class='pill-count' id='cnt-degree'>0</span></a>
          <a class='job-cat-pill' data-filter='Teaching Jobs' href='javascript:void(0)' onclick='filterByLabel("Teaching Jobs")'>👩‍🏫 Teaching <span class='pill-count' id='cnt-teaching'>0</span></a>
          <a class='job-cat-pill' data-filter='Medical Jobs' href='javascript:void(0)' onclick='filterByLabel("Medical Jobs")'>🏥 Medical <span class='pill-count' id='cnt-medical'>0</span></a>
          <a class='job-cat-pill' data-filter='Engineering Jobs' href='javascript:void(0)' onclick='filterByLabel("Engineering Jobs")'>⚙️ Engineering <span class='pill-count' id='cnt-eng'>0</span></a>
          <a class='job-cat-pill' href='javascript:void(0)' onclick='toggleEligibilityWidget()' style='border-color:var(--primary); color:var(--primary); background:var(--primary-light); font-weight:800;'>🎯 Match My Eligibility</a>
        </div>
      </div>
    </div>

    <!-- Main Layout Container (Feed & Dedicated Article Pages) -->
    <div class='portal-layout'>
      <!-- Feed / Main Content -->
      <main>
        <!-- 1. Dedicated Full Job Article View -->
        <article class='full-job-article' id='fullJobArticleView'>
          <button class='back-nav-bar' onclick='showFeedView()' type='button'>
            <i class='fas fa-arrow-left'/> Back to All Latest Jobs Feed
          </button>
          <div id='jobArticleContent'/>
          
          <!-- Related Jobs Under the Post -->
          <div class='related-jobs-box'>
            <h3 class='related-jobs-title'><i class='fas fa-layer-group'/> More Similar Job Openings</h3>
            <div class='related-jobs-list' id='relatedJobsContainer'/>
          </div>

          <div style='margin-top:2rem; text-align:center;'>
            <button class='back-nav-bar' onclick='showFeedView()' style='background:var(--primary); color:#FFFFFF; border-color:var(--primary);' type='button'>
              <i class='fas fa-arrow-left'/> Back to All Latest Notifications
            </button>
          </div>
        </article>

        <!-- 2. Interactive Instant Job Eligibility & Age Matcher (Hidden By Default) -->
        <div class='eligibility-calculator-card' id='eligibilityWidget' style='display:none;'>
          <div class='calc-header' onclick='toggleEligibilityWidget()'>
            <div style='display:flex; align-items:center; gap:8px;'>
              <i class='fas fa-calculator' style='color:var(--primary); font-size:1.15rem;'/>
              <h3 style='margin:0; font-size:0.98rem; font-weight:900;'>⚡ Instant Job Eligibility &amp; Age Matcher</h3>
            </div>
            <button class='calc-toggle-btn' id='calcToggleBtn' title='Close Matcher' type='button'>
              <i class='fas fa-times' id='calcToggleIcon'/>
            </button>
          </div>
          <div class='calc-body' id='calcBody'>
            <p style='margin:0.5rem 0 0.75rem; font-size:0.82rem; color:var(--text-secondary);'>Select your education and age to instantly match with all verified Government vacancies.</p>
            <div class='calc-grid'>
              <div class='calc-field'>
                <label>🎓 Qualification:</label>
                <select id='calcQual' onchange='applyEligibilityMatch()'>
                  <option value=''>All Qualifications</option>
                  <option value='10th Pass'>10th Pass (SSLC / Matric)</option>
                  <option value='12th Pass'>12th Pass (+2 / Higher Sec)</option>
                  <option value='ITI'>ITI Pass (Any Trade)</option>
                  <option value='Diploma'>Diploma in Engineering</option>
                  <option value='Degree'>Any Bachelor Degree (Graduate)</option>
                  <option value='B.Tech'>B.Tech / B.E (Engineering)</option>
                  <option value='Nursing'>Nursing / MBBS / Medical</option>
                  <option value='PG'>Post Graduate (PG / Master / MBA)</option>
                  <option value='Teaching'>B.Ed / Teacher / NET</option>
                </select>
              </div>
              <div class='calc-field'>
                <label>🎂 Your Age (Years):</label>
                <input id='calcAge' max='60' min='16' oninput='applyEligibilityMatch()' placeholder='e.g. 24' type='number'/>
              </div>
              <div class='calc-field'>
                <label>💰 Min Monthly Salary:</label>
                <select id='calcSalary' onchange='applyEligibilityMatch()'>
                  <option value='0'>Any Salary</option>
                  <option value='25000'>₹25,000+ / month</option>
                  <option value='35000'>₹35,000+ / month</option>
                  <option value='50000'>₹50,000+ / month</option>
                  <option value='80000'>₹80,000+ / month</option>
                </select>
              </div>
            </div>
            <div class='calc-actions'>
              <button class='calc-btn-find' onclick='applyEligibilityMatch()' type='button'><i class='fas fa-search'/> Find Matching Jobs</button>
              <button class='calc-btn-reset' onclick='resetEligibilityMatch()' type='button'><i class='fas fa-redo'/> Reset</button>
              <span id='calcMatchedCount' style='font-size:0.84rem; font-weight:800; color:var(--primary); margin-left:auto;'/>
            </div>
          </div>
        </div>

        <!-- 3. Native Blogger Post Content Container (Rendered on Direct Post Pages) -->
        <b:section id='main' showaddelement='yes'>
          <b:widget id='Blog1' locked='true' title='Blog Posts' type='Blog'>
            <b:includable id='main' var='top'>
              <b:if cond='data:blog.pageType == "item"'>
                <div class='native-post-view' id='nativePostContainer'>
                  <a class='back-nav-bar' href='/' style='text-decoration:none; display:inline-flex; align-items:center; gap:8px; margin-bottom:1.25rem; font-weight:800;'>
                    <i class='fas fa-arrow-left'/> Back to All 167+ Latest Jobs Feed
                  </a>
                  <b:loop values='data:posts' var='post'>
                    <article style='background:var(--bg-card); padding:1.75rem; border-radius:14px; border:1px solid var(--border-color); box-shadow:var(--card-shadow); margin-bottom:1.5rem;'>
                      <div style='margin-bottom:1rem; display:flex; flex-wrap:wrap; gap:8px;'>
                        <span class='type-chip chip-notif'>📢 OFFICIAL NOTIFICATION</span>
                        <b:loop values='data:post.labels' var='label'>
                          <span class='job-org-badge'><i class='fas fa-tag'/> <data:label.name/></span>
                        </b:loop>
                      </div>
                      <h1 style='font-size:1.6rem; font-weight:900; line-height:1.4; color:var(--text-primary); margin-bottom:1.25rem;'><data:post.title/></h1>
                      <div class='post-body-content' style='font-size:0.95rem; line-height:1.8; color:var(--text-primary);'>
                        <data:post.body/>
                      </div>
                    </article>
                  </b:loop>
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

        <!-- 4. Interactive Job Feed Cards List & Pagination (For Homepage Portal) -->
        <div id='jobFeedWrapper'>
          <div class='results-count-bar'>
            <span id='resultsCountText'>Showing latest notifications</span>
            <span id='currentPageIndicator'>Page 1</span>
          </div>

          <!-- Interactive Job Feed Cards List (For Homepage Portal) -->
          <div class='job-feed' id='jobFeedContainer'></div>

          <!-- Page Numbers Navigation -->
          <div class='pagination-container' id='paginationControls'/>
        </div>
      </main>

      <!-- Sidebar: Expanded Top Job Sectors with Live Counts -->
      <aside>
        <!-- Telegram Alerts CTA -->
        <div class='telegram-cta'>
          <i class='fab fa-telegram-plane' style='font-size:2rem; margin-bottom:0.3rem;'/>
          <h3>Daily Job Alerts on Telegram</h3>
          <p>Instant Kerala PSC, SSC, Bank &amp; Railway recruitment updates.</p>
          <a href='https://telegram.org' rel='noopener noreferrer' target='_blank'>Join Telegram Channel ↗</a>
        </div>

        <!-- Top Job Sectors List -->
        <div class='sidebar-card'>
          <h3 class='sidebar-title'><i class='fas fa-th-list'/> Top Job Sectors</h3>
          <ul class='category-list'>
            <li><a href='javascript:void(0)' onclick='filterTodayJobs()' style='background:linear-gradient(135deg,rgba(239,68,68,0.1),rgba(245,158,11,0.1)); border-color:#F59E0B; color:#D97706;'><span>⚡ Added Today (Fresh Updates)</span> <span class='pill-count' id='side-today'>0</span></a></li>
            <li><a href='javascript:void(0)' onclick='filterByLabel("Kerala Govt Jobs")'><span>🌴 Kerala Govt Jobs</span> <span class='pill-count' id='side-kerala'>0</span></a></li>
            <li><a href='javascript:void(0)' onclick='filterByLabel("Kerala PSC")'><span>📜 Kerala PSC Notifications</span> <span class='pill-count' id='side-kpsc'>0</span></a></li>
            <li><a href='javascript:void(0)' onclick='filterByLabel("Bank Jobs")'><span>🏦 Banking (SBI / IBPS / RBI)</span> <span class='pill-count' id='side-bank'>0</span></a></li>
            <li><a href='javascript:void(0)' onclick='filterByLabel("Railway Jobs")'><span>🚆 Indian Railways (RRB / RPF)</span> <span class='pill-count' id='side-railway'>0</span></a></li>
            <li><a href='javascript:void(0)' onclick='filterByLabel("SSC CGL")'><span>📋 SSC &amp; UPSC (CGL/CHSL)</span> <span class='pill-count' id='side-ssc'>0</span></a></li>
            <li><a href='javascript:void(0)' onclick='filterByLabel("Defence Jobs")'><span>🎖️ Defence &amp; Armed Forces</span> <span class='pill-count' id='side-defence'>0</span></a></li>
            <li><a href='javascript:void(0)' onclick='filterByLabel("Police Jobs")'><span>👮 Police &amp; Paramilitary</span> <span class='pill-count' id='side-police'>0</span></a></li>
            <li><a href='javascript:void(0)' onclick='filterByLabel("PSU Jobs")'><span>⚙️ PSU Jobs (ISRO / DRDO)</span> <span class='pill-count' id='side-psu'>0</span></a></li>
            <li><a href='javascript:void(0)' onclick='filterByLabel("Central Govt Jobs")'><span>📮 India Post &amp; GDS</span> <span class='pill-count' id='side-post'>0</span></a></li>
            <li><a href='javascript:void(0)' onclick='filterByLabel("Medical Jobs")'><span>🏥 Medical &amp; Nursing (AIIMS)</span> <span class='pill-count' id='side-medical'>0</span></a></li>
            <li><a href='javascript:void(0)' onclick='filterByLabel("Teaching Jobs")'><span>👩‍🏫 Teaching &amp; Faculty</span> <span class='pill-count' id='side-teaching'>0</span></a></li>
            <li><a href='javascript:void(0)' onclick='filterByLabel("Clerk Jobs")'><span>⚖️ Courts &amp; High Court Clerks</span> <span class='pill-count' id='side-clerk'>0</span></a></li>
            <li><a href='javascript:void(0)' onclick='filterByLabel("10th Pass")'><span>🎓 10th Pass (SSLC) Jobs</span> <span class='pill-count' id='side-10th'>0</span></a></li>
            <li><a href='javascript:void(0)' onclick='filterByLabel("Degree Jobs")'><span>🎓 Graduate / Degree Jobs</span> <span class='pill-count' id='side-degree'>0</span></a></li>
            <li><a href='javascript:void(0)' onclick='filterByLabel("Engineering Jobs")'><span>⚙️ Engineering &amp; Diploma</span> <span class='pill-count' id='side-eng'>0</span></a></li>
          </ul>
        </div>
      </aside>
    </div>

    <!-- Bank & Financial Institution Directory (All Major Apex, PSU, Private & Insurance) -->
    <div class='bank-cards-section' id='banksDirectorySection'>
      <div class='bank-section-card'>
        <div class='section-heading-sm'>
          <span><i class='fas fa-university' style='color:var(--primary);'/> Filter by Bank &amp; Financial Institution</span>
        </div>
        
        <!-- Primary Top 10 Major Banks Grid -->
        <div class='bank-grid' id='bankGridTrack'>
          <a class='bank-card' data-bank='State Bank of India' href='javascript:void(0)' onclick='filterByLabel("State Bank of India")'><span>🏛️ SBI (State Bank)</span> <span class='bank-count' id='bk-sbi'>0</span></a>
          <a class='bank-card' data-bank='IBPS' href='javascript:void(0)' onclick='filterByLabel("IBPS")'><span>🏦 IBPS PO/Clerk</span> <span class='bank-count' id='bk-ibps'>0</span></a>
          <a class='bank-card' data-bank='Reserve Bank of India' href='javascript:void(0)' onclick='filterByLabel("Reserve Bank of India")'><span>🏛️ RBI (Apex Bank)</span> <span class='bank-count' id='bk-rbi'>0</span></a>
          <a class='bank-card' data-bank='NABARD' href='javascript:void(0)' onclick='filterByLabel("NABARD")'><span>🌾 NABARD</span> <span class='bank-count' id='bk-nabard'>0</span></a>
          <a class='bank-card' data-bank='Punjab National Bank' href='javascript:void(0)' onclick='filterByLabel("Punjab National Bank")'><span>🏦 PNB Bank</span> <span class='bank-count' id='bk-pnb'>0</span></a>
          <a class='bank-card' data-bank='Bank of Baroda' href='javascript:void(0)' onclick='filterByLabel("Bank of Baroda")'><span>🏦 Bank of Baroda</span> <span class='bank-count' id='bk-bob'>0</span></a>
          <a class='bank-card' data-bank='Canara Bank' href='javascript:void(0)' onclick='filterByLabel("Canara Bank")'><span>🏦 Canara Bank</span> <span class='bank-count' id='bk-canara'>0</span></a>
          <a class='bank-card' data-bank='Union Bank of India' href='javascript:void(0)' onclick='filterByLabel("Union Bank of India")'><span>🏦 Union Bank</span> <span class='bank-count' id='bk-union'>0</span></a>
          <a class='bank-card' data-bank='IBPS RRB' href='javascript:void(0)' onclick='filterByLabel("IBPS RRB")'><span>🌾 RRB Gramin Bank</span> <span class='bank-count' id='bk-rrb'>0</span></a>
          <a class='bank-card' data-bank='LIC India' href='javascript:void(0)' onclick='filterByLabel("LIC India")'><span>🛡️ LIC of India</span> <span class='bank-count' id='bk-lic'>0</span></a>
        </div>

        <!-- Extended 20+ Banks & Institutions (Hidden by Default) -->
        <div class='bank-grid' id='extraBanksGrid' style='display:none; margin-top:8px;'>
          <a class='bank-card' data-bank='SEBI' href='javascript:void(0)' onclick='filterByLabel("SEBI")'><span>📈 SEBI</span> <span class='bank-count' id='bk-sebi'>0</span></a>
          <a class='bank-card' data-bank='SIDBI' href='javascript:void(0)' onclick='filterByLabel("SIDBI")'><span>🏭 SIDBI</span> <span class='bank-count' id='bk-sidbi'>0</span></a>
          <a class='bank-card' data-bank='EXIM Bank' href='javascript:void(0)' onclick='filterByLabel("EXIM Bank")'><span>🚢 EXIM Bank</span> <span class='bank-count' id='bk-exim'>0</span></a>
          <a class='bank-card' data-bank='Central Bank of India' href='javascript:void(0)' onclick='filterByLabel("Central Bank of India")'><span>🏦 Central Bank</span> <span class='bank-count' id='bk-central'>0</span></a>
          <a class='bank-card' data-bank='Bank of Maharashtra' href='javascript:void(0)' onclick='filterByLabel("Bank of Maharashtra")'><span>🏦 Bank of Maha</span> <span class='bank-count' id='bk-bom'>0</span></a>
          <a class='bank-card' data-bank='Indian Overseas Bank' href='javascript:void(0)' onclick='filterByLabel("Indian Overseas Bank")'><span>🏦 IOB Bank</span> <span class='bank-count' id='bk-iob'>0</span></a>
          <a class='bank-card' data-bank='UCO Bank' href='javascript:void(0)' onclick='filterByLabel("UCO Bank")'><span>🏦 UCO Bank</span> <span class='bank-count' id='bk-uco'>0</span></a>
          <a class='bank-card' data-bank='Punjab &amp; Sind Bank' href='javascript:void(0)' onclick='filterByLabel("Punjab &amp; Sind Bank")'><span>🏦 Punjab &amp; Sind</span> <span class='bank-count' id='bk-psb'>0</span></a>
          <a class='bank-card' data-bank='IDBI Bank' href='javascript:void(0)' onclick='filterByLabel("IDBI Bank")'><span>🏦 IDBI Bank</span> <span class='bank-count' id='bk-idbi'>0</span></a>
          <a class='bank-card' data-bank='India Post Payments Bank' href='javascript:void(0)' onclick='filterByLabel("India Post Payments Bank")'><span>📮 IPPB Bank</span> <span class='bank-count' id='bk-ippb'>0</span></a>
          <a class='bank-card' data-bank='Federal Bank' href='javascript:void(0)' onclick='filterByLabel("Federal Bank")'><span>🏛️ Federal Bank</span> <span class='bank-count' id='bk-federal'>0</span></a>
          <a class='bank-card' data-bank='South Indian Bank' href='javascript:void(0)' onclick='filterByLabel("South Indian Bank")'><span>🏛️ South Indian Bank</span> <span class='bank-count' id='bk-sib'>0</span></a>
          <a class='bank-card' data-bank='New India Assurance' href='javascript:void(0)' onclick='filterByLabel("New India Assurance")'><span>🛡️ NIACL Assurance</span> <span class='bank-count' id='bk-niacl'>0</span></a>
          <a class='bank-card' data-bank='HDFC Bank' href='javascript:void(0)' onclick='filterByLabel("HDFC Bank")'><span>🏛️ HDFC Bank</span> <span class='bank-count' id='bk-hdfc'>0</span></a>
          <a class='bank-card' data-bank='ICICI Bank' href='javascript:void(0)' onclick='filterByLabel("ICICI Bank")'><span>🏛️ ICICI Bank</span> <span class='bank-count' id='bk-icici'>0</span></a>
          <a class='bank-card' data-bank='Axis Bank' href='javascript:void(0)' onclick='filterByLabel("Axis Bank")'><span>🏛️ Axis Bank</span> <span class='bank-count' id='bk-axis'>0</span></a>
          <a class='bank-card' data-bank='Kotak' href='javascript:void(0)' onclick='filterByLabel("Kotak")'><span>🏛️ Kotak Bank</span> <span class='bank-count' id='bk-kotak'>0</span></a>
          <a class='bank-card' data-bank='Bank of India' href='javascript:void(0)' onclick='filterByLabel("Bank of India")'><span>🏦 Bank of India</span> <span class='bank-count' id='bk-boi'>0</span></a>
          <a class='bank-card' data-bank='Indian Bank' href='javascript:void(0)' onclick='filterByLabel("Indian Bank")'><span>🏦 Indian Bank</span> <span class='bank-count' id='bk-indian'>0</span></a>
        </div>

        <div style='text-align:center;'>
          <button class='toggle-banks-btn' id='btnToggleBanks' onclick='toggleAllBanks()' type='button'>
            <i class='fas fa-th-large'/> + View All 28+ Banks &amp; Insurance
          </button>
        </div>
      </div>
    </div>

    <!-- State & Territory Section (Cleanly Placed Below Job Feed) -->
    <div class='state-cards-section' id='statesDirectorySection'>
      <div class='state-section-card'>
        <div class='section-heading-sm'>
          <span><i class='fas fa-map-marked-alt' style='color:var(--primary);'/> Filter by State &amp; Territory</span>
        </div>
        
        <!-- Primary Top 10 States Grid -->
        <div class='state-grid' id='stateGridTrack'>
          <a class='state-card active' data-state='' href='javascript:void(0)' onclick='filterByLabel("")'><span>🇮🇳 All India</span> <span class='state-count' id='st-all'>0</span></a>
          <a class='state-card' data-state='Kerala Govt Jobs' href='javascript:void(0)' onclick='filterByLabel("Kerala Govt Jobs")'><span>🌴 Kerala</span> <span class='state-count' id='st-kerala'>0</span></a>
          <a class='state-card' data-state='Tamil Nadu' href='javascript:void(0)' onclick='filterByLabel("Tamil Nadu")'><span>🛕 Tamil Nadu</span> <span class='state-count' id='st-tn'>0</span></a>
          <a class='state-card' data-state='Karnataka' href='javascript:void(0)' onclick='filterByLabel("Karnataka")'><span>🌸 Karnataka</span> <span class='state-count' id='st-ka'>0</span></a>
          <a class='state-card' data-state='Andhra' href='javascript:void(0)' onclick='filterByLabel("Andhra")'><span>🐘 Andhra</span> <span class='state-count' id='st-ap'>0</span></a>
          <a class='state-card' data-state='Telangana' href='javascript:void(0)' onclick='filterByLabel("Telangana")'><span>🏰 Telangana</span> <span class='state-count' id='st-ts'>0</span></a>
          <a class='state-card' data-state='Maharashtra' href='javascript:void(0)' onclick='filterByLabel("Maharashtra")'><span>🏢 Maharashtra</span> <span class='state-count' id='st-mh'>0</span></a>
          <a class='state-card' data-state='Gujarat' href='javascript:void(0)' onclick='filterByLabel("Gujarat")'><span>🦁 Gujarat</span> <span class='state-count' id='st-gj'>0</span></a>
          <a class='state-card' data-state='Delhi' href='javascript:void(0)' onclick='filterByLabel("Delhi")'><span>🕌 Delhi NCR</span> <span class='state-count' id='st-dl'>0</span></a>
          <a class='state-card' data-state='Uttar Pradesh' href='javascript:void(0)' onclick='filterByLabel("Uttar Pradesh")'><span>🪔 UP</span> <span class='state-count' id='st-up'>0</span></a>
        </div>

        <!-- Extended 26 States & UTs (Hidden by Default) -->
        <div class='state-grid' id='extraStatesGrid' style='display:none; margin-top:8px;'>
          <a class='state-card' data-state='Bihar' href='javascript:void(0)' onclick='filterByLabel("Bihar")'><span>🌾 Bihar</span> <span class='state-count' id='st-br'>0</span></a>
          <a class='state-card' data-state='West Bengal' href='javascript:void(0)' onclick='filterByLabel("West Bengal")'><span>🎨 Bengal</span> <span class='state-count' id='st-wb'>0</span></a>
          <a class='state-card' data-state='Rajasthan' href='javascript:void(0)' onclick='filterByLabel("Rajasthan")'><span>👑 Rajasthan</span> <span class='state-count' id='st-rj'>0</span></a>
          <a class='state-card' data-state='Madhya Pradesh' href='javascript:void(0)' onclick='filterByLabel("Madhya Pradesh")'><span>🐯 MP</span> <span class='state-count' id='st-mp'>0</span></a>
          <a class='state-card' data-state='Odisha' href='javascript:void(0)' onclick='filterByLabel("Odisha")'><span>⛵ Odisha</span> <span class='state-count' id='st-od'>0</span></a>
          <a class='state-card' data-state='Punjab' href='javascript:void(0)' onclick='filterByLabel("Punjab")'><span>🚜 Punjab</span> <span class='state-count' id='st-pb'>0</span></a>
          <a class='state-card' data-state='Haryana' href='javascript:void(0)' onclick='filterByLabel("Haryana")'><span>🌾 Haryana</span> <span class='state-count' id='st-hr'>0</span></a>
          <a class='state-card' data-state='Assam' href='javascript:void(0)' onclick='filterByLabel("Assam")'><span>🦏 Assam</span> <span class='state-count' id='st-as'>0</span></a>
          <a class='state-card' data-state='Jammu' href='javascript:void(0)' onclick='filterByLabel("Jammu")'><span>🏔️ J&amp;K</span> <span class='state-count' id='st-jk'>0</span></a>
          <a class='state-card' data-state='Goa' href='javascript:void(0)' onclick='filterByLabel("Goa")'><span>🏖️ Goa</span> <span class='state-count' id='st-ga'>0</span></a>
          <a class='state-card' data-state='Himachal' href='javascript:void(0)' onclick='filterByLabel("Himachal")'><span>🌲 Himachal</span> <span class='state-count' id='st-hp'>0</span></a>
          <a class='state-card' data-state='Uttarakhand' href='javascript:void(0)' onclick='filterByLabel("Uttarakhand")'><span>🏞️ Uttarakhand</span> <span class='state-count' id='st-uk'>0</span></a>
          <a class='state-card' data-state='Jharkhand' href='javascript:void(0)' onclick='filterByLabel("Jharkhand")'><span>⛏️ Jharkhand</span> <span class='state-count' id='st-jh'>0</span></a>
          <a class='state-card' data-state='Chhattisgarh' href='javascript:void(0)' onclick='filterByLabel("Chhattisgarh")'><span>🌿 Chhattisgarh</span> <span class='state-count' id='st-cg'>0</span></a>
          <a class='state-card' data-state='Meghalaya' href='javascript:void(0)' onclick='filterByLabel("Meghalaya")'><span>🌄 Meghalaya</span> <span class='state-count' id='st-ml'>0</span></a>
          <a class='state-card' data-state='Manipur' href='javascript:void(0)' onclick='filterByLabel("Manipur")'><span>🎋 Manipur</span> <span class='state-count' id='st-mn'>0</span></a>
          <a class='state-card' data-state='Mizoram' href='javascript:void(0)' onclick='filterByLabel("Mizoram")'><span>🍃 Mizoram</span> <span class='state-count' id='st-mz'>0</span></a>
          <a class='state-card' data-state='Nagaland' href='javascript:void(0)' onclick='filterByLabel("Nagaland")'><span>🛡️ Nagaland</span> <span class='state-count' id='st-nl'>0</span></a>
          <a class='state-card' data-state='Tripura' href='javascript:void(0)' onclick='filterByLabel("Tripura")'><span>🌺 Tripura</span> <span class='state-count' id='st-tr'>0</span></a>
          <a class='state-card' data-state='Arunachal' href='javascript:void(0)' onclick='filterByLabel("Arunachal")'><span>☀️ Arunachal</span> <span class='state-count' id='st-ar'>0</span></a>
          <a class='state-card' data-state='Sikkim' href='javascript:void(0)' onclick='filterByLabel("Sikkim")'><span>🏔️ Sikkim</span> <span class='state-count' id='st-sk'>0</span></a>
          <a class='state-card' data-state='Puducherry' href='javascript:void(0)' onclick='filterByLabel("Puducherry")'><span>🌊 Puducherry</span> <span class='state-count' id='st-py'>0</span></a>
          <a class='state-card' data-state='Chandigarh' href='javascript:void(0)' onclick='filterByLabel("Chandigarh")'><span>🏛️ Chandigarh</span> <span class='state-count' id='st-ch'>0</span></a>
          <a class='state-card' data-state='Ladakh' href='javascript:void(0)' onclick='filterByLabel("Ladakh")'><span>❄️ Ladakh</span> <span class='state-count' id='st-la'>0</span></a>
          <a class='state-card' data-state='Andaman' href='javascript:void(0)' onclick='filterByLabel("Andaman")'><span>🏝️ Andaman</span> <span class='state-count' id='st-an'>0</span></a>
          <a class='state-card' data-state='Central Govt Jobs' href='javascript:void(0)' onclick='filterByLabel("Central Govt Jobs")'><span>🏛️ Central Govt</span> <span class='state-count' id='st-central'>0</span></a>
        </div>

        <div style='text-align:center;'>
          <button class='toggle-states-btn' id='btnToggleStates' onclick='toggleAllStates()' type='button'>
            <i class='fas fa-th-large'/> + View All 36 States &amp; UTs
          </button>
        </div>
      </div>
    </div>

    <!-- Quick Browse Directory Hubs (Qualifications & Top Sectors) -->
    <div class='quick-browse-grid' id='browseHubsSection'>
      <!-- Block 1: By Qualification -->
      <div class='browse-block'>
        <div class='browse-header'><span>🎓 Jobs by Qualification</span> <i class='fas fa-graduation-cap' style='color:var(--primary);'/></div>
        <div class='browse-chips'>
          <a class='browse-chip' href='javascript:void(0)' onclick='filterByLabel("10th Pass")'><span>10th Pass (SSLC)</span> <span class='chip-cnt' id='q-10th'>0</span></a>
          <a class='browse-chip' href='javascript:void(0)' onclick='filterByLabel("12th Pass")'><span>12th Pass (+2)</span> <span class='chip-cnt' id='q-12th'>0</span></a>
          <a class='browse-chip' href='javascript:void(0)' onclick='filterByLabel("ITI Jobs")'><span>ITI Pass</span> <span class='chip-cnt' id='q-iti'>0</span></a>
          <a class='browse-chip' href='javascript:void(0)' onclick='filterByLabel("Diploma Jobs")'><span>Diploma</span> <span class='chip-cnt' id='q-diploma'>0</span></a>
          <a class='browse-chip' href='javascript:void(0)' onclick='filterByLabel("Degree Jobs")'><span>Any Graduate / Degree</span> <span class='chip-cnt' id='q-degree'>0</span></a>
          <a class='browse-chip' href='javascript:void(0)' onclick='filterByLabel("Engineering Jobs")'><span>B.Tech / B.E</span> <span class='chip-cnt' id='q-eng'>0</span></a>
          <a class='browse-chip' href='javascript:void(0)' onclick='filterByLabel("Medical Jobs")'><span>Nursing / MBBS</span> <span class='chip-cnt' id='q-med'>0</span></a>
          <a class='browse-chip' href='javascript:void(0)' onclick='filterByLabel("PG Jobs")'><span>Post Graduate (PG)</span> <span class='chip-cnt' id='q-pg'>0</span></a>
          <a class='browse-chip' href='javascript:void(0)' onclick='filterByLabel("Teaching Jobs")'><span>B.Ed / Teacher</span> <span class='chip-cnt' id='q-teach'>0</span></a>
        </div>
      </div>

      <!-- Block 2: By Major Sectors -->
      <div class='browse-block'>
        <div class='browse-header'><span>🏛️ Jobs by Sector</span> <i class='fas fa-building' style='color:var(--primary);'/></div>
        <div class='browse-chips'>
          <a class='browse-chip' href='javascript:void(0)' onclick='filterByLabel("Kerala PSC")'><span>Kerala PSC</span> <span class='chip-cnt' id='sec-kpsc'>0</span></a>
          <a class='browse-chip' href='javascript:void(0)' onclick='filterByLabel("Bank Jobs")'><span>Banking (SBI / IBPS)</span> <span class='chip-cnt' id='sec-bank'>0</span></a>
          <a class='browse-chip' href='javascript:void(0)' onclick='filterByLabel("Railway Jobs")'><span>Indian Railways (RRB)</span> <span class='chip-cnt' id='sec-rail'>0</span></a>
          <a class='browse-chip' href='javascript:void(0)' onclick='filterByLabel("SSC CGL")'><span>SSC (CGL/CHSL/MTS)</span> <span class='chip-cnt' id='sec-ssc'>0</span></a>
          <a class='browse-chip' href='javascript:void(0)' onclick='filterByLabel("UPSC Jobs")'><span>UPSC / Civil Services</span> <span class='chip-cnt' id='sec-upsc'>0</span></a>
          <a class='browse-chip' href='javascript:void(0)' onclick='filterByLabel("Defence Jobs")'><span>Army / Navy / Airforce</span> <span class='chip-cnt' id='sec-defence'>0</span></a>
          <a class='browse-chip' href='javascript:void(0)' onclick='filterByLabel("Police Jobs")'><span>Police / Paramilitary</span> <span class='chip-cnt' id='sec-police'>0</span></a>
          <a class='browse-chip' href='javascript:void(0)' onclick='filterByLabel("PSU Jobs")'><span>PSU (ISRO / DRDO)</span> <span class='chip-cnt' id='sec-psu'>0</span></a>
          <a class='browse-chip' href='javascript:void(0)' onclick='filterByLabel("Central Govt Jobs")'><span>India Post / GDS</span> <span class='chip-cnt' id='sec-post'>0</span></a>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <footer>
      <p style='margin-bottom:0.4rem;'>
        <strong><data:blog.title/></strong> &#169; <span class='dyn-year'>2026</span> - Daily Government Job Notifications, Admit Cards &amp; Results Portal.
      </p>
      <p style='font-size:0.8rem; color:var(--text-muted);'>
        Disclaimer: We provide recruitment updates for informational purposes. Candidates must verify notifications on official government portals.
      </p>
    </footer>

    <!-- Embedded Jobs Database & Portal Engine -->
    <script type='text/javascript'>
      //<![CDATA[
      var ALL_JOBS = __JOBS_JSON__;
      var currentChannel = 'all';
      var currentFilter = '';
      var currentSearch = '';
      var calcQual = '';
      var calcAge = null;
      var calcSalary = 0;
      var currentPage = 1;
      var itemsPerPage = 12;
      var activeFilteredJobs = ALL_JOBS;

      // Automatic Dynamic Year Calculator (Automatically rolls over to 2027, 2028...)
      function updateDynamicYear() {
        var currentYear = new Date().getFullYear();
        var elements = document.querySelectorAll('.dyn-year');
        for (var i = 0; i < elements.length; i++) {
          elements[i].innerText = currentYear;
        }
      }

      function getSavedJobs() {
        try {
          return JSON.parse(localStorage.getItem('savedGovtJobs') || '[]');
        } catch (e) {
          return [];
        }
      }

      function toggleSaveJob(jobId, event) {
        if (event) event.stopPropagation();
        var saved = getSavedJobs();
        var idx = saved.indexOf(jobId);
        var isNowSaved = false;
        if (idx === -1) {
          saved.push(jobId);
          isNowSaved = true;
        } else {
          saved.splice(idx, 1);
          isNowSaved = false;
        }
        localStorage.setItem('savedGovtJobs', JSON.stringify(saved));
        updateChannelCounts();
        if (currentChannel === 'saved') {
          filterJobs();
        } else {
          renderJobCards(activeFilteredJobs);
        }

        var artBtn = document.getElementById('articleBookmarkBtn');
        if (artBtn) {
          if (isNowSaved) {
            artBtn.innerHTML = "<i class='fas fa-bookmark' style='color:#F59E0B;'></i> Saved in Bookmarks";
            artBtn.style.background = '#FEF3C7';
            artBtn.style.color = '#D97706';
          } else {
            artBtn.innerHTML = "<i class='far fa-bookmark'></i> ⭐ Save Job";
            artBtn.style.background = 'var(--bg-page)';
            artBtn.style.color = 'var(--text-primary)';
          }
        }
      }

      function switchPortalType(type) {
        showFeedView();
        currentChannel = type || 'all';

        // When switching to saved, reset search and category filter so all saved jobs show immediately
        if (currentChannel === 'saved') {
          currentFilter = '';
          currentSearch = '';
          var input = document.getElementById('jobSearch');
          if (input) input.value = '';
          var clearBtn = document.getElementById('searchClearBtn');
          if (clearBtn) clearBtn.style.display = 'none';
        }

        // Update active class on unified filter track pills
        var pills = document.querySelectorAll('#categoryPillsTrack .job-cat-pill');
        for (var p = 0; p < pills.length; p++) {
          var ch = pills[p].getAttribute('data-channel');
          if (ch) {
            if (ch === currentChannel) {
              pills[p].classList.add('active');
            } else {
              pills[p].classList.remove('active');
            }
          } else {
            pills[p].classList.remove('active');
          }
        }

        // Update nav links active class
        var navLinks = document.querySelectorAll('.nav-links a');
        for (var n = 0; n < navLinks.length; n++) {
          var linkText = navLinks[n].innerText.toLowerCase();
          if (currentChannel === 'all' && linkText.indexOf('home') !== -1) {
            navLinks[n].classList.add('active');
          } else if (currentChannel === 'saved' && linkText.indexOf('saved') !== -1) {
            navLinks[n].classList.add('active');
          } else if (currentChannel === 'notification' && linkText.indexOf('notification') !== -1) {
            navLinks[n].classList.add('active');
          } else if (currentChannel === 'admit_card' && linkText.indexOf('admit') !== -1) {
            navLinks[n].classList.add('active');
          } else if (currentChannel === 'result' && linkText.indexOf('result') !== -1) {
            navLinks[n].classList.add('active');
          } else {
            navLinks[n].classList.remove('active');
          }
        }

        filterJobs();

        var feed = document.getElementById('jobFeedContainer');
        if (feed) {
          feed.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }

      function showAllJobsView() {
        showFeedView();
        currentChannel = 'all';
        currentFilter = '';
        currentSearch = '';
        calcQual = '';
        calcAge = null;
        calcSalary = 0;
        currentPage = 1;

        var input = document.getElementById('jobSearch');
        if (input) input.value = '';
        var clearBtn = document.getElementById('searchClearBtn');
        if (clearBtn) clearBtn.style.display = 'none';

        // Update unified filter pills
        var pills = document.querySelectorAll('#categoryPillsTrack .job-cat-pill');
        for (var p = 0; p < pills.length; p++) {
          if (p === 0) pills[p].classList.add('active');
          else pills[p].classList.remove('active');
        }

        // Update bank cards
        var bankCards = document.querySelectorAll('.bank-card');
        for (var b = 0; b < bankCards.length; b++) {
          bankCards[b].classList.remove('active');
        }

        // Update state cards
        var stateCards = document.querySelectorAll('.state-card');
        for (var k = 0; k < stateCards.length; k++) {
          if (k === 0) stateCards[k].classList.add('active');
          else stateCards[k].classList.remove('active');
        }

        // Update nav links
        var navLinks = document.querySelectorAll('.nav-links a');
        for (var n = 0; n < navLinks.length; n++) {
          if (n === 0) navLinks[n].classList.add('active');
          else navLinks[n].classList.remove('active');
        }

        filterJobs();

        var feed = document.getElementById('jobFeedContainer');
        if (feed) {
          feed.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }

      function toggleEligibilityWidget() {
        var widget = document.getElementById('eligibilityWidget');
        if (!widget) return;
        var isHidden = widget.style.display === 'none' || window.getComputedStyle(widget).display === 'none';
        if (isHidden) {
          widget.style.display = 'block';
          var body = document.getElementById('calcBody');
          if (body) body.style.display = 'block';
          widget.scrollIntoView({ behavior: 'smooth', block: 'start' });
        } else {
          widget.style.display = 'none';
        }
      }

      function applyEligibilityMatch() {
        showFeedView();
        // If on saved, restore to all to match across full database
        if (currentChannel === 'saved') {
          currentChannel = 'all';
          var pills = document.querySelectorAll('#categoryPillsTrack .job-cat-pill');
          for (var p = 0; p < pills.length; p++) {
            if (p === 0) pills[p].classList.add('active');
            else pills[p].classList.remove('active');
          }
        }

        var qualInput = document.getElementById('calcQual');
        var ageInput = document.getElementById('calcAge');
        var salInput = document.getElementById('calcSalary');

        calcQual = qualInput ? qualInput.value : '';
        calcAge = ageInput && ageInput.value ? parseInt(ageInput.value, 10) : null;
        calcSalary = salInput && salInput.value ? parseInt(salInput.value, 10) : 0;

        filterJobs();

        var countBadge = document.getElementById('calcMatchedCount');
        if (countBadge) {
          countBadge.innerText = 'Matched: ' + activeFilteredJobs.length + ' Opportunities';
        }
      }

      function resetEligibilityMatch() {
        var qualInput = document.getElementById('calcQual');
        var ageInput = document.getElementById('calcAge');
        var salInput = document.getElementById('calcSalary');

        if (qualInput) qualInput.value = '';
        if (ageInput) ageInput.value = '';
        if (salInput) salInput.value = '0';

        calcQual = '';
        calcAge = null;
        calcSalary = 0;

        var countBadge = document.getElementById('calcMatchedCount');
        if (countBadge) countBadge.innerText = '';

        filterJobs();
      }

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

      function toggleAllStates() {
        var extra = document.getElementById('extraStatesGrid');
        var btn = document.getElementById('btnToggleStates');
        if (!extra || !btn) return;
        if (extra.style.display === 'none' || extra.style.display === '') {
          extra.style.display = 'grid';
          btn.innerHTML = "<i class='fas fa-chevron-up'></i> - Show Less States";
        } else {
          extra.style.display = 'none';
          btn.innerHTML = "<i class='fas fa-th-large'></i> + View All 36 States & UTs";
        }
      }

      function toggleAllBanks() {
        var extra = document.getElementById('extraBanksGrid');
        var btn = document.getElementById('btnToggleBanks');
        if (!extra || !btn) return;
        if (extra.style.display === 'none' || extra.style.display === '') {
          extra.style.display = 'grid';
          btn.innerHTML = "<i class='fas fa-chevron-up'></i> - Show Less Banks";
        } else {
          extra.style.display = 'none';
          btn.innerHTML = "<i class='fas fa-th-large'></i> + View All 28+ Banks & Insurance";
        }
      }

      // Check if job is newly added (Today / Current Fresh Batch)
      function isJobAddedToday(job) {
        if (!job) return false;
        var today = new Date();
        var jobDate = new Date(job.start_date);
        if (!isNaN(jobDate.getTime())) {
          var diffDays = Math.floor((today.getTime() - jobDate.getTime()) / (1000 * 60 * 60 * 24));
          return diffDays >= 0 && diffDays <= 14;
        }
        return true;
      }

      // Smart Deadline Status Calculator
      // 🟢 Live = Green, 🟠 Closing Soon <= 7 days = Amber, 🔴 Expired = Red
      function getDeadlineStatus(lastDateStr) {
        if (!lastDateStr) return { css: 'status-live', label: '🟢 Active' };
        
        var targetDate = new Date(lastDateStr);
        if (isNaN(targetDate.getTime())) {
          return { css: 'status-live', label: '🟢 Apply by ' + lastDateStr };
        }

        var today = new Date();
        var diffTime = targetDate.getTime() - today.getTime();
        var diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

        if (diffDays < 0) {
          return { css: 'status-closed', label: '🔴 Closed / Expired' };
        } else if (diffDays <= 7) {
          return { css: 'status-closing', label: '⏳ Closing Soon: ' + lastDateStr };
        } else {
          return { css: 'status-live', label: '🟢 Apply by ' + lastDateStr };
        }
      }

      function extractSalaryNumber(salStr) {
        if (!salStr) return 0;
        var nums = salStr.replace(/,/g, '').match(/\d+/g);
        if (!nums || nums.length === 0) return 0;
        return parseInt(nums[0], 10);
      }

      function matchesAgeLimit(jobAgeStr, candidateAge) {
        if (!candidateAge || !jobAgeStr) return true;
        var nums = jobAgeStr.match(/\d+/g);
        if (!nums || nums.length === 0) return true;
        if (nums.length === 1) {
          return candidateAge <= (parseInt(nums[0], 10) + 3);
        }
        var minAge = parseInt(nums[0], 10);
        var maxAge = parseInt(nums[1], 10) + 3;
        return candidateAge >= minAge && candidateAge <= maxAge;
      }

      function updateChannelCounts() {
        var savedCount = getSavedJobs().length;
        var elSaved = document.getElementById('ch-saved');
        if (elSaved) elSaved.innerText = savedCount;
        var elCntSaved = document.getElementById('cnt-saved');
        if (elCntSaved) elCntSaved.innerText = savedCount;
        var elNavSaved = document.getElementById('navSavedCount');
        if (elNavSaved) elNavSaved.innerText = savedCount;

        var elAll = document.getElementById('ch-all');
        if (elAll) elAll.innerText = ALL_JOBS.length;
        var elCntAll = document.getElementById('cnt-all');
        if (elCntAll) elCntAll.innerText = ALL_JOBS.length;

        var elNotif = document.getElementById('ch-notif');
        if (elNotif) elNotif.innerText = ALL_JOBS.filter(function(j) { return j.item_type === 'notification'; }).length;
        var elCntNotif = document.getElementById('cnt-notif');
        if (elCntNotif) elCntNotif.innerText = ALL_JOBS.filter(function(j) { return j.item_type === 'notification'; }).length;

        var elAdmit = document.getElementById('ch-admit');
        if (elAdmit) elAdmit.innerText = ALL_JOBS.filter(function(j) { return j.item_type === 'admit_card'; }).length;
        var elCntAdmit = document.getElementById('cnt-admit');
        if (elCntAdmit) elCntAdmit.innerText = ALL_JOBS.filter(function(j) { return j.item_type === 'admit_card'; }).length;

        var elRes = document.getElementById('ch-res');
        if (elRes) elRes.innerText = ALL_JOBS.filter(function(j) { return j.item_type === 'result'; }).length;
        var elCntRes = document.getElementById('cnt-res');
        if (elCntRes) elCntRes.innerText = ALL_JOBS.filter(function(j) { return j.item_type === 'result'; }).length;

        var elAns = document.getElementById('ch-ans');
        if (elAns) elAns.innerText = ALL_JOBS.filter(function(j) { return j.item_type === 'answer_key'; }).length;
        var elCntAns = document.getElementById('cnt-ans');
        if (elCntAns) elCntAns.innerText = ALL_JOBS.filter(function(j) { return j.item_type === 'answer_key'; }).length;

        var elSyl = document.getElementById('ch-syl');
        if (elSyl) elSyl.innerText = ALL_JOBS.filter(function(j) { return j.item_type === 'syllabus'; }).length;
        var elCntSyl = document.getElementById('cnt-syl');
        if (elCntSyl) elCntSyl.innerText = ALL_JOBS.filter(function(j) { return j.item_type === 'syllabus'; }).length;
      }

      function updateCategoryCounts() {
        function countMatches(keyword) {
          if (!keyword) return ALL_JOBS.length;
          var kw = keyword.toLowerCase();
          return ALL_JOBS.filter(function(j) {
            var text = (j.title + ' ' + j.category + ' ' + (j.labels ? j.labels.join(' ') : '') + ' ' + j.qualification + ' ' + j.location + ' ' + j.org_name).toLowerCase();
            return text.indexOf(kw) !== -1;
          }).length;
        }

        var todayCount = ALL_JOBS.filter(function(j) { return isJobAddedToday(j); }).length;
        var elToday = document.getElementById('cnt-today');
        if (elToday) elToday.innerText = todayCount;
        var elSideToday = document.getElementById('side-today');
        if (elSideToday) elSideToday.innerText = todayCount;

        var mapping = [
          // Pills
          ['cnt-all', ''],
          ['cnt-kerala', 'Kerala Govt Jobs'],
          ['cnt-kpsc', 'Kerala PSC'],
          ['cnt-bank', 'Bank Jobs'],
          ['cnt-railway', 'Railway Jobs'],
          ['cnt-ssc', 'SSC CGL'],
          ['cnt-defence', 'Defence Jobs'],
          ['cnt-police', 'Police Jobs'],
          ['cnt-psu', 'PSU Jobs'],
          ['cnt-post', 'Central Govt Jobs'],
          ['cnt-10th', '10th Pass'],
          ['cnt-12th', '12th Pass'],
          ['cnt-degree', 'Degree Jobs'],
          ['cnt-teaching', 'Teaching Jobs'],
          ['cnt-medical', 'Medical Jobs'],
          ['cnt-eng', 'Engineering Jobs'],
          
          // Sidebar
          ['side-kerala', 'Kerala Govt Jobs'],
          ['side-kpsc', 'Kerala PSC'],
          ['side-bank', 'Bank Jobs'],
          ['side-railway', 'Railway Jobs'],
          ['side-ssc', 'SSC CGL'],
          ['side-defence', 'Defence Jobs'],
          ['side-police', 'Police Jobs'],
          ['side-psu', 'PSU Jobs'],
          ['side-post', 'Central Govt Jobs'],
          ['side-medical', 'Medical Jobs'],
          ['side-teaching', 'Teaching Jobs'],
          ['side-clerk', 'Clerk Jobs'],
          ['side-10th', '10th Pass'],
          ['side-degree', 'Degree Jobs'],
          ['side-eng', 'Engineering Jobs'],

          // Banks & Financial Institutions
          ['bk-sbi', 'State Bank of India'],
          ['bk-ibps', 'IBPS'],
          ['bk-rbi', 'Reserve Bank of India'],
          ['bk-nabard', 'NABARD'],
          ['bk-pnb', 'Punjab National Bank'],
          ['bk-bob', 'Bank of Baroda'],
          ['bk-canara', 'Canara Bank'],
          ['bk-union', 'Union Bank'],
          ['bk-rrb', 'IBPS RRB'],
          ['bk-lic', 'LIC India'],
          ['bk-sebi', 'SEBI'],
          ['bk-sidbi', 'SIDBI'],
          ['bk-exim', 'EXIM Bank'],
          ['bk-central', 'Central Bank of India'],
          ['bk-bom', 'Bank of Maharashtra'],
          ['bk-iob', 'Indian Overseas Bank'],
          ['bk-uco', 'UCO Bank'],
          ['bk-psb', 'Punjab & Sind Bank'],
          ['bk-idbi', 'IDBI Bank'],
          ['bk-ippb', 'India Post Payments Bank'],
          ['bk-federal', 'Federal Bank'],
          ['bk-sib', 'South Indian Bank'],
          ['bk-niacl', 'New India Assurance'],
          ['bk-hdfc', 'HDFC Bank'],
          ['bk-icici', 'ICICI Bank'],
          ['bk-axis', 'Axis Bank'],
          ['bk-kotak', 'Kotak'],
          ['bk-boi', 'Bank of India'],
          ['bk-indian', 'Indian Bank'],

          // States
          ['st-all', ''],
          ['st-kerala', 'Kerala Govt Jobs'],
          ['st-tn', 'Tamil Nadu'],
          ['st-ka', 'Karnataka'],
          ['st-ap', 'Andhra'],
          ['st-ts', 'Telangana'],
          ['st-mh', 'Maharashtra'],
          ['st-gj', 'Gujarat'],
          ['st-dl', 'Delhi'],
          ['st-up', 'Uttar Pradesh'],
          ['st-br', 'Bihar'],
          ['st-wb', 'West Bengal'],
          ['st-rj', 'Rajasthan'],
          ['st-mp', 'Madhya Pradesh'],
          ['st-od', 'Odisha'],
          ['st-pb', 'Punjab'],
          ['st-hr', 'Haryana'],
          ['st-as', 'Assam'],
          ['st-jk', 'Jammu'],
          ['st-ga', 'Goa'],
          ['st-hp', 'Himachal'],
          ['st-uk', 'Uttarakhand'],
          ['st-jh', 'Jharkhand'],
          ['st-cg', 'Chhattisgarh'],
          ['st-ml', 'Meghalaya'],
          ['st-mn', 'Manipur'],
          ['st-mz', 'Mizoram'],
          ['st-nl', 'Nagaland'],
          ['st-tr', 'Tripura'],
          ['st-ar', 'Arunachal'],
          ['st-sk', 'Sikkim'],
          ['st-py', 'Puducherry'],
          ['st-ch', 'Chandigarh'],
          ['st-la', 'Ladakh'],
          ['st-an', 'Andaman'],
          ['st-central', 'Central Govt Jobs'],

          // Qualifications
          ['q-10th', '10th Pass'],
          ['q-12th', '12th Pass'],
          ['q-iti', 'ITI Jobs'],
          ['q-diploma', 'Diploma Jobs'],
          ['q-degree', 'Degree Jobs'],
          ['q-eng', 'Engineering Jobs'],
          ['q-med', 'Medical Jobs'],
          ['q-pg', 'PG Jobs'],
          ['q-teach', 'Teaching Jobs'],

          // Sectors Hubs
          ['sec-kpsc', 'Kerala PSC'],
          ['sec-bank', 'Bank Jobs'],
          ['sec-rail', 'Railway Jobs'],
          ['sec-ssc', 'SSC CGL'],
          ['sec-upsc', 'UPSC Jobs'],
          ['sec-defence', 'Defence Jobs'],
          ['sec-police', 'Police Jobs'],
          ['sec-psu', 'PSU Jobs'],
          ['sec-post', 'Central Govt Jobs']
        ];

        for (var m = 0; m < mapping.length; m++) {
          var el = document.getElementById(mapping[m][0]);
          if (el) {
            el.innerText = countMatches(mapping[m][1]);
          }
        }
      }

      function renderJobCards(jobs) {
        var container = document.getElementById('jobFeedContainer');
        if (!container) return;

        var savedList = getSavedJobs();

        // Dedicated Separation Page View for Saved / Favorite Jobs
        if (currentChannel === 'saved') {
          if (!jobs || jobs.length === 0) {
            container.innerHTML = "<div style='text-align:center; padding:3.5rem 1.5rem; background:var(--bg-card); border-radius:14px; border:2px dashed #F59E0B; margin-bottom:1.5rem;'>" +
              "<div style='width:68px; height:68px; background:#FEF3C7; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 1.25rem;'>" +
                "<i class='fas fa-bookmark' style='font-size:2.2rem; color:#D97706;'></i>" +
              "</div>" +
              "<h3 style='font-size:1.35rem; font-weight:900; margin-bottom:0.5rem; color:var(--text-primary);'>No Bookmarked / Saved Jobs Yet</h3>" +
              "<p style='color:var(--text-secondary); max-width:480px; margin:0 auto 1.5rem; font-size:0.92rem; line-height:1.6;'>Tap the <strong>⭐ Save</strong> bookmark button on any recruitment card to save it here for fast one-tap access.</p>" +
              "<button onclick='showAllJobsView()' class='calc-btn-find' style='font-size:0.95rem; padding:10px 24px; border-radius:50px; background:linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);' type='button'><i class='fas fa-th-large'></i> Explore All 167+ Latest Openings</button>" +
            "</div>";
            var countZero = document.getElementById('resultsCountText');
            if (countZero) countZero.innerText = "⭐ 0 Bookmarked Jobs Saved";
            var pageZero = document.getElementById('currentPageIndicator');
            if (pageZero) pageZero.innerText = "";
            renderPagination(0);
            return;
          }
        } else {
          if (!jobs || jobs.length === 0) {
            container.innerHTML = "<div style='text-align:center; padding:3rem 1rem; background:var(--bg-card); border-radius:12px; border:1px solid var(--border-color);'><i class='fas fa-search' style='font-size:2.2rem; color:var(--text-muted); margin-bottom:0.75rem;'></i><h3>No notifications found matching your search.</h3><p style='color:var(--text-secondary); font-size:0.9rem;'>Try selecting All Updates or searching with a different qualification.</p><button onclick='showAllJobsView()' class='calc-btn-find' style='margin-top:1rem;' type='button'>Show All Openings</button></div>";
            var countZero = document.getElementById('resultsCountText');
            if (countZero) countZero.innerText = "0 notifications found";
            var pageZero = document.getElementById('currentPageIndicator');
            if (pageZero) pageZero.innerText = "";
            renderPagination(0);
            return;
          }
        }

        var totalItems = jobs.length;
        var totalPages = Math.ceil(totalItems / itemsPerPage);
        if (currentPage > totalPages) currentPage = 1;

        var startIdx = (currentPage - 1) * itemsPerPage;
        var endIdx = Math.min(startIdx + itemsPerPage, totalItems);
        var pageItems = jobs.slice(startIdx, endIdx);

        var countEl = document.getElementById('resultsCountText');
        if (countEl) {
          if (currentChannel === 'saved') {
            countEl.innerText = "⭐ Showing " + (startIdx + 1) + "–" + endIdx + " of " + totalItems + " saved bookmarks";
          } else {
            countEl.innerText = "Showing " + (startIdx + 1) + "–" + endIdx + " of " + totalItems + " notifications";
          }
        }
        var pageEl = document.getElementById('currentPageIndicator');
        if (pageEl) pageEl.innerText = "Page " + currentPage + " of " + totalPages;

        var savedHeaderBanner = "";
        if (currentChannel === 'saved') {
          savedHeaderBanner = "<div class='saved-header-banner'>" +
            "<div style='display:flex; align-items:center; gap:10px;'>" +
              "<div style='width:36px; height:36px; border-radius:50%; background:#FDE68A; display:flex; align-items:center; justify-content:center; flex-shrink:0;'>" +
                "<i class='fas fa-bookmark' style='color:#D97706; font-size:1.15rem;'></i>" +
              "</div>" +
              "<div>" +
                "<h3 style='margin:0; font-size:1rem; font-weight:900; color:#92400E;'>⭐ My Saved &amp; Bookmarked Jobs (" + totalItems + ")</h3>" +
                "<p style='margin:0; font-size:0.78rem; color:#B45309;'>Your bookmarked opportunities stored locally in this browser.</p>" +
              "</div>" +
            "</div>" +
            "<button onclick='showAllJobsView()' style='background:#2563EB; color:#FFF; border:none; padding:7px 16px; border-radius:50px; font-weight:800; font-size:0.82rem; cursor:pointer; display:inline-flex; align-items:center; gap:5px;' type='button'>⬅ Back to All Jobs</button>" +
          "</div>";
        }

        var html = '';
        for (var i = 0; i < pageItems.length; i++) {
          var job = pageItems[i];
          var statusObj = getDeadlineStatus(job.last_date);
          var todayBadge = isJobAddedToday(job) ? "<span class='badge-today'>⚡ TODAY</span>" : "";
          var isSaved = savedList.indexOf(job.id) !== -1;
          var bookmarkIcon = isSaved ? "<i class='fas fa-bookmark saved'></i>" : "<i class='far fa-bookmark'></i>";

          var typeClass = 'chip-notif';
          var typeLabel = '📢 NOTIFICATION';
          if (job.item_type === 'admit_card') { typeClass = 'chip-admit'; typeLabel = '🎫 ADMIT CARD'; }
          else if (job.item_type === 'result') { typeClass = 'chip-result'; typeLabel = '🏆 RESULT'; }
          else if (job.item_type === 'answer_key') { typeClass = 'chip-ans'; typeLabel = '📝 ANSWER KEY'; }
          else if (job.item_type === 'syllabus') { typeClass = 'chip-syl'; typeLabel = '📚 SYLLABUS'; }

          html += "<div class='job-card' data-jobid='" + job.id + "' onclick='openJobFullPage(this.dataset.jobid)'>" +
                    "<div class='job-card-top'>" +
                      "<div class='job-card-badges'>" +
                        "<span class='type-chip " + typeClass + "'>" + typeLabel + "</span>" +
                        "<span class='job-org-badge'><i class='fas fa-building'></i> " + job.org_name + "</span>" +
                        todayBadge +
                      "</div>" +
                      "<div class='job-card-actions'>" +
                        "<span class='status-badge " + statusObj.css + "'>" + statusObj.label + "</span>" +
                        "<button class='bookmark-btn " + (isSaved ? "saved" : "") + "' data-saveid='" + job.id + "' onclick='toggleSaveJob(this.dataset.saveid, event)' title='Save Job' type='button'>" + bookmarkIcon + "</button>" +
                      "</div>" +
                    "</div>" +
                    "<h2 class='job-card-title'>" + job.title + "</h2>" +
                    "<div class='job-card-bottom'>" +
                      "<span class='job-qual-chip'><i class='fas fa-graduation-cap'></i> " + job.qualification + "</span>" +
                      "<span class='job-read-link'>Details &amp; Apply ➔</span>" +
                    "</div>" +
                  "</div>";
        }
        container.innerHTML = savedHeaderBanner + html;
        renderPagination(totalPages);
      }

      function renderPagination(totalPages) {
        var container = document.getElementById('paginationControls');
        if (!container) return;

        if (totalPages <= 1) {
          container.innerHTML = '';
          return;
        }

        var html = '';
        var prevDisabled = currentPage === 1 ? 'disabled' : '';
        html += "<button class='page-btn " + prevDisabled + "' onclick='changePage(" + (currentPage - 1) + ")' type='button'>« Prev</button>";

        for (var p = 1; p <= totalPages; p++) {
          if (p === 1 || p === totalPages || (p >= currentPage - 2 && p <= currentPage + 2)) {
            var activeClass = p === currentPage ? 'active' : '';
            html += "<button class='page-btn " + activeClass + "' onclick='changePage(" + p + ")' type='button'>" + p + "</button>";
          } else if (p === currentPage - 3 || p === currentPage + 3) {
            html += "<span style='padding:4px 6px; color:var(--text-muted); font-weight:800;'>...</span>";
          }
        }

        var nextDisabled = currentPage === totalPages ? 'disabled' : '';
        html += "<button class='page-btn " + nextDisabled + "' onclick='changePage(" + (currentPage + 1) + ")' type='button'>Next »</button>";

        container.innerHTML = html;
      }

      function changePage(page) {
        currentPage = page;
        renderJobCards(activeFilteredJobs);
        var feedWrapper = document.getElementById('jobFeedWrapper');
        if (feedWrapper) {
          feedWrapper.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }

      function liveFilterJobs(query) {
        showFeedView();
        // If we were on saved tab, restore to all updates when user searches
        if (currentChannel === 'saved') {
          currentChannel = 'all';
          var tabs = document.querySelectorAll('.channel-tab');
          for (var t = 0; t < tabs.length; t++) {
            if (tabs[t].getAttribute('data-type') === 'all') tabs[t].classList.add('active');
            else tabs[t].classList.remove('active');
          }
        }

        currentSearch = (query || '').trim();
        var clearBtn = document.getElementById('searchClearBtn');
        if (clearBtn) {
          clearBtn.style.display = currentSearch ? 'block' : 'none';
        }
        filterJobs();
      }

      function quickSearch(kw) {
        var input = document.getElementById('jobSearch');
        if (input) {
          input.value = kw;
          liveFilterJobs(kw);
          input.focus();
        }
      }

      function clearSearch() {
        var input = document.getElementById('jobSearch');
        if (input) {
          input.value = '';
          liveFilterJobs('');
          input.focus();
        }
      }

      function filterJobs() {
        var savedList = getSavedJobs();

        activeFilteredJobs = ALL_JOBS.filter(function(job) {
          // Channel filter
          if (currentChannel === 'saved') {
            if (savedList.indexOf(job.id) === -1) return false;
          } else if (currentChannel !== 'all') {
            if (job.item_type !== currentChannel) return false;
          }

          // Category pill filter
          if (currentFilter === '__TODAY__') {
            if (!isJobAddedToday(job)) return false;
          } else if (currentFilter) {
            var allText = (job.title + ' ' + job.category + ' ' + (job.labels ? job.labels.join(' ') : '') + ' ' + job.qualification + ' ' + job.location + ' ' + job.org_name).toLowerCase();
            if (allText.indexOf(currentFilter.toLowerCase()) === -1) return false;
          }

          // Search query
          if (currentSearch) {
            var searchable = (job.title + ' ' + job.org_name + ' ' + job.qualification + ' ' + job.post_name + ' ' + job.location + ' ' + (job.labels ? job.labels.join(' ') : '')).toLowerCase();
            if (searchable.indexOf(currentSearch.toLowerCase()) === -1) return false;
          }

          // Eligibility calculator qualification
          if (calcQual) {
            var qualText = (job.qualification + ' ' + job.title + ' ' + (job.labels ? job.labels.join(' ') : '')).toLowerCase();
            if (qualText.indexOf(calcQual.toLowerCase()) === -1) return false;
          }

          // Eligibility calculator age
          if (calcAge !== null) {
            if (!matchesAgeLimit(job.age_limit, calcAge)) return false;
          }

          // Eligibility calculator salary
          if (calcSalary > 0) {
            if (extractSalaryNumber(job.salary) < calcSalary) return false;
          }

          return true;
        });

        currentPage = 1;
        renderJobCards(activeFilteredJobs);
      }

      function filterTodayJobs() {
        showFeedView();
        // If we were on saved tab, restore to all updates when user selects today
        if (currentChannel === 'saved') {
          currentChannel = 'all';
          var tabs = document.querySelectorAll('.channel-tab');
          for (var t = 0; t < tabs.length; t++) {
            if (tabs[t].getAttribute('data-type') === 'all') tabs[t].classList.add('active');
            else tabs[t].classList.remove('active');
          }
        }

        currentFilter = '__TODAY__';
        
        // Update active class on category pills
        var pills = document.querySelectorAll('#categoryPillsTrack .job-cat-pill');
        for (var i = 0; i < pills.length; i++) {
          if (pills[i].getAttribute('data-filter') === 'today') {
            pills[i].classList.add('active');
          } else {
            pills[i].classList.remove('active');
          }
        }

        var feed = document.getElementById('jobFeedContainer');
        if (feed) {
          feed.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }

        filterJobs();
      }

      function filterByLabel(label) {
        showFeedView();
        // If we were on saved tab, restore to all updates when user selects a category
        if (currentChannel === 'saved') {
          currentChannel = 'all';
          var tabs = document.querySelectorAll('.channel-tab');
          for (var t = 0; t < tabs.length; t++) {
            if (tabs[t].getAttribute('data-type') === 'all') tabs[t].classList.add('active');
            else tabs[t].classList.remove('active');
          }
        }

        currentFilter = label || '';
        
        // Update active class on category pills
        var pills = document.querySelectorAll('#categoryPillsTrack .job-cat-pill');
        for (var i = 0; i < pills.length; i++) {
          var pillFilter = pills[i].getAttribute('data-filter') || '';
          if ((!label && i === 0) || (label && pillFilter.toLowerCase() === label.toLowerCase()) || (label && pills[i].innerText.toLowerCase().indexOf(label.toLowerCase()) !== -1)) {
            pills[i].classList.add('active');
          } else {
            pills[i].classList.remove('active');
          }
        }

        // Update active class on bank cards
        var bankCards = document.querySelectorAll('.bank-card');
        for (var b = 0; b < bankCards.length; b++) {
          var bk = bankCards[b].getAttribute('data-bank') || '';
          if (label && (bk.toLowerCase() === label.toLowerCase() || bankCards[b].innerText.toLowerCase().indexOf(label.toLowerCase()) !== -1)) {
            bankCards[b].classList.add('active');
          } else {
            bankCards[b].classList.remove('active');
          }
        }

        // Update active class on state cards
        var stateCards = document.querySelectorAll('.state-card');
        for (var k = 0; k < stateCards.length; k++) {
          var st = stateCards[k].getAttribute('data-state') || '';
          if ((!label && k === 0) || (label && st.toLowerCase() === label.toLowerCase()) || (label && stateCards[k].innerText.toLowerCase().indexOf(label.toLowerCase()) !== -1)) {
            stateCards[k].classList.add('active');
          } else {
            stateCards[k].classList.remove('active');
          }
        }

        var feed = document.getElementById('jobFeedContainer');
        if (feed) {
          feed.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }

        filterJobs();
      }

      function copyJobLink() {
        if (navigator.clipboard) {
          navigator.clipboard.writeText(window.location.href);
          alert('Job Link Copied to Clipboard!');
        }
      }

      // Open Dedicated Full Page View for a Job + Dynamic SEO Schema + Related Jobs
      function openJobFullPage(jobId) {
        var job = ALL_JOBS.find(function(j) { return j.id === jobId; });
        if (!job) return;

        if (window.location.hash !== '#' + jobId) {
          try {
            history.pushState(null, null, '#' + jobId);
          } catch(e) {
            window.location.hash = jobId;
          }
        }

        // Dynamic Document Title for SEO
        var yr = new Date().getFullYear();
        document.title = job.title + " - Official Notification & Apply Online " + yr;

        // Dynamic JobPosting Schema.org JSON-LD for Google Rich Snippets
        var oldSchema = document.getElementById('dynamicJobPostingSchema');
        if (oldSchema) oldSchema.remove();

        var schemaTag = document.createElement('script');
        schemaTag.type = 'application/ld+json';
        schemaTag.id = 'dynamicJobPostingSchema';
        var jobPostingJson = {
          "@context": "https://schema.org/",
          "@type": "JobPosting",
          "title": job.title,
          "description": job.title + " recruitment by " + job.org_name + ". Qualification: " + job.qualification + ", Vacancies: " + job.vacancies + ", Salary: " + job.salary,
          "identifier": {
            "@type": "PropertyValue",
            "name": job.org_name,
            "value": job.id
          },
          "datePosted": job.start_date || new Date().toISOString().split('T')[0],
          "validThrough": job.last_date ? job.last_date + "T23:59:59+05:30" : undefined,
          "employmentType": "FULL_TIME",
          "hiringOrganization": {
            "@type": "Organization",
            "name": job.org_name,
            "sameAs": job.website
          },
          "jobLocation": {
            "@type": "Place",
            "address": {
              "@type": "PostalAddress",
              "addressLocality": job.location,
              "addressCountry": "IN"
            }
          },
          "baseSalary": {
            "@type": "MonetaryAmount",
            "currency": "INR",
            "value": {
              "@type": "QuantitativeValue",
              "value": job.salary,
              "unitText": "MONTH"
            }
          },
          "educationRequirements": job.qualification
        };
        schemaTag.textContent = JSON.stringify(jobPostingJson);
        document.head.appendChild(schemaTag);

        document.getElementById('jobFeedWrapper').style.display = 'none';
        var calcEl = document.getElementById('eligibilityWidget');
        if (calcEl) calcEl.style.display = 'none';

        var articleView = document.getElementById('fullJobArticleView');
        articleView.style.display = 'block';

        var content = document.getElementById('jobArticleContent');
        var shareUrl = encodeURIComponent(window.location.href);
        var shareText = encodeURIComponent(job.title + " - Apply before " + job.last_date);
        var statusObj = getDeadlineStatus(job.last_date);

        var savedList = getSavedJobs();
        var isSaved = savedList.indexOf(job.id) !== -1;
        var saveBtnHtml = isSaved 
          ? "<button onclick='toggleSaveJob(this.dataset.saveid, event)' data-saveid='" + job.id + "' id='articleBookmarkBtn' class='share-btn' style='background:#FEF3C7; color:#D97706; border-color:#F59E0B;' type='button'><i class='fas fa-bookmark'></i> Saved in Bookmarks</button>"
          : "<button onclick='toggleSaveJob(this.dataset.saveid, event)' data-saveid='" + job.id + "' id='articleBookmarkBtn' class='share-btn' type='button'><i class='far fa-bookmark'></i> ⭐ Save Job</button>";

        var typeClass = 'chip-notif';
        var typeLabel = '📢 OFFICIAL NOTIFICATION';
        if (job.item_type === 'admit_card') { typeClass = 'chip-admit'; typeLabel = '🎫 ADMIT CARD / HALL TICKET'; }
        else if (job.item_type === 'result') { typeClass = 'chip-result'; typeLabel = '🏆 RESULT / RANKED LIST'; }
        else if (job.item_type === 'answer_key') { typeClass = 'chip-ans'; typeLabel = '📝 ANSWER KEY & PAPER'; }
        else if (job.item_type === 'syllabus') { typeClass = 'chip-syl'; typeLabel = '📚 EXAM SYLLABUS'; }

        content.innerHTML = "" +
          "<div style='background:linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%); color:#FFFFFF; border-radius:14px; padding:1.75rem; text-align:center; margin-bottom:1.5rem;'>" +
            "<div style='display:flex; justify-content:center; gap:8px; margin-bottom:8px; flex-wrap:wrap;'>" +
              "<span class='type-chip " + typeClass + "' style='font-size:0.75rem;'>" + typeLabel + "</span>" +
              "<span style='background:rgba(255,255,255,0.2); color:#FFF; padding:4px 12px; border-radius:50px; font-weight:800; font-size:0.75rem; text-transform:uppercase;'>🏛️ " + job.org_name + "</span>" +
            "</div>" +
            "<h1 style='font-size:clamp(1.4rem, 3.5vw, 2rem); font-weight:900; margin:0.5rem 0; color:#FFFFFF; line-height:1.3;'>" + job.title + "</h1>" +
            "<p style='margin:0; font-size:0.92rem; opacity:0.92;'>Official Recruitment Notification <span class='dyn-year'>" + yr + "</span> | Verified Eligibility &amp; Direct Application Portal</p>" +
          "</div>" +

          "<div style='padding:0.9rem 1.2rem; border-radius:10px; font-weight:700; margin-bottom:1.5rem; font-size:0.95rem;' class='" + statusObj.css + "'>" +
            "📅 <strong>Application Status:</strong> " + statusObj.label + " | Submit online before the closing date." +
          "</div>" +

          "<div class='share-bar'>" +
            "<span style='font-weight:800; font-size:0.85rem; color:var(--text-primary);'><i class='fas fa-share-alt'></i> Actions:</span>" +
            saveBtnHtml +
            "<a href='https://api.whatsapp.com/send?text=" + shareText + "%20" + shareUrl + "' target='_blank' rel='noopener' class='share-btn btn-whatsapp'><i class='fab fa-whatsapp'></i> WhatsApp</a>" +
            "<a href='https://t.me/share/url?url=" + shareUrl + "&text=" + shareText + "' target='_blank' rel='noopener' class='share-btn btn-telegram'><i class='fab fa-telegram-plane'></i> Telegram</a>" +
            "<button onclick='copyJobLink()' class='share-btn btn-copy' type='button'><i class='fas fa-copy'></i> Copy Link</button>" +
          "</div>" +

          "<h2 style='font-size:1.25rem; font-weight:900; color:var(--primary); margin:1.5rem 0 0.5rem; border-bottom:2px solid var(--border-color); padding-bottom:0.4rem;'>📋 Complete Recruitment Overview <span class='dyn-year'>" + yr + "</span></h2>" +
          "<table class='article-table'>" +
            "<tr><td>Hiring Authority</td><td>" + job.org_name + "</td></tr>" +
            "<tr><td>Post Name</td><td>" + job.post_name + "</td></tr>" +
            "<tr><td>Total Vacancies</td><td style='color:#059669; font-size:1.05rem;'>" + job.vacancies + "</td></tr>" +
            "<tr><td>Monthly Salary / Pay Scale</td><td style='color:#2563EB; font-size:1.05rem;'>" + job.salary + "</td></tr>" +
            "<tr><td>Educational Qualification</td><td>" + job.qualification + "</td></tr>" +
            "<tr><td>Age Limit</td><td>" + job.age_limit + "</td></tr>" +
            "<tr><td>Application Fee</td><td>" + job.fee + "</td></tr>" +
            "<tr><td>Job Location</td><td>" + job.location + "</td></tr>" +
            "<tr><td>Application Window</td><td>" + job.start_date + " to " + job.last_date + "</td></tr>" +
            "<tr><td>Official Website</td><td><a href='" + job.apply_url + "' target='_blank' rel='noopener noreferrer' style='color:var(--primary); font-weight:800;'>" + job.website + " ↗</a></td></tr>" +
          "</table>" +

          "<h2 style='font-size:1.25rem; font-weight:900; color:var(--primary); margin:1.5rem 0 0.5rem; border-bottom:2px solid var(--border-color); padding-bottom:0.4rem;'>🔗 Official Application &amp; Notification Links</h2>" +
          "<div style='display:flex; flex-wrap:wrap; gap:12px; justify-content:center; margin:1.25rem 0;'>" +
            "<a href='" + job.apply_url + "' target='_blank' rel='noopener noreferrer' style='flex:1; min-width:240px; text-align:center; padding:13px 20px; background:#059669; color:#FFFFFF; border-radius:50px; font-weight:900; text-decoration:none; font-size:0.98rem; box-shadow:0 4px 14px rgba(5,150,105,0.3);'>📝 Apply Online Portal ↗</a>" +
            "<a href='" + job.pdf_url + "' target='_blank' rel='noopener noreferrer' style='flex:1; min-width:240px; text-align:center; padding:13px 20px; background:#2563EB; color:#FFFFFF; border-radius:50px; font-weight:900; text-decoration:none; font-size:0.98rem; box-shadow:0 4px 14px rgba(37,99,235,0.3);'>📄 Download Official PDF ↗</a>" +
          "</div>" +

          "<h2 style='font-size:1.25rem; font-weight:900; color:var(--primary); margin:1.75rem 0 0.5rem; border-bottom:2px solid var(--border-color); padding-bottom:0.4rem;'>✍️ Step-by-Step Application Instructions</h2>" +
          "<ol style='padding-left:1.25rem; line-height:1.9; margin:1rem 0; font-size:0.92rem;'>" +
            "<li>Visit the official government portal: <strong>" + job.website + "</strong>.</li>" +
            "<li>Look for <strong>Recruitment / Career Notifications " + yr + "</strong>.</li>" +
            "<li>Select the notification for <strong>" + job.post_name + "</strong>.</li>" +
            "<li>Register for One-Time Registration (OTR) or login with your registration ID.</li>" +
            "<li>Fill in your educational qualification, age, and reservation details accurately.</li>" +
            "<li>Upload scanned copies of required certificates, photo, and signature.</li>" +
            "<li>Submit application fees online and print your final acknowledgment confirmation.</li>" +
          "</ol>";



        // Render Related Job Cards Under Post
        var related = ALL_JOBS.filter(function(other) {
          return other.id !== job.id && (other.category === job.category || (other.labels && other.labels.some(function(l) { return job.labels && job.labels.indexOf(l) !== -1; })));
        }).slice(0, 4);

        var relatedContainer = document.getElementById('relatedJobsContainer');
        if (relatedContainer) {
          if (related.length === 0) {
            related = ALL_JOBS.filter(function(o) { return o.id !== job.id; }).slice(0, 4);
          }
          var rHtml = '';
          for (var r = 0; r < related.length; r++) {
            var rJob = related[r];
            var rStatus = getDeadlineStatus(rJob.last_date);
            rHtml += "<div class='job-card' data-jobid='" + rJob.id + "' onclick='openJobFullPage(this.dataset.jobid)'>" +
                       "<div class='job-card-top'>" +
                         "<span class='job-org-badge'><i class='fas fa-building'></i> " + rJob.org_name + "</span>" +
                         "<span class='status-badge " + rStatus.css + "'>" + rStatus.label + "</span>" +
                       "</div>" +
                       "<h4 class='job-card-title' style='font-size:0.96rem;'>" + rJob.title + "</h4>" +
                       "<div class='job-card-bottom'>" +
                         "<span class='job-qual-chip'><i class='fas fa-graduation-cap'></i> " + rJob.qualification + "</span>" +
                         "<span class='job-read-link'>View ➔</span>" +
                       "</div>" +
                     "</div>";
          }
          relatedContainer.innerHTML = rHtml;
        }

        updateDynamicYear();
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }

      function showFeedView() {
        if (window.location.hash) {
          try {
            history.pushState('', document.title, window.location.pathname + window.location.search);
          } catch(e) {
            window.location.hash = '';
          }
        }
        var yr = new Date().getFullYear();
        document.title = "Government Job Notifications " + yr + " | Kerala PSC, Central Govt, Banking, Railway, SSC Updates";
        
        var oldSchema = document.getElementById('dynamicJobPostingSchema');
        if (oldSchema) oldSchema.remove();

        var articleView = document.getElementById('fullJobArticleView');
        if (articleView) articleView.style.display = 'none';

        var calcEl = document.getElementById('eligibilityWidget');
        if (calcEl) calcEl.style.display = 'none';

        var feedWrapper = document.getElementById('jobFeedWrapper');
        if (feedWrapper) feedWrapper.style.display = 'block';

        window.scrollTo({ top: 0, behavior: 'smooth' });
      }

      function checkHashRoute() {
        var hash = (window.location.hash || '').replace('#', '');
        if (hash) {
          var job = ALL_JOBS.find(function(j) { return j.id === hash; });
          if (job) {
            openJobFullPage(hash);
            return;
          }
        }
        showFeedView();
      }

      window.addEventListener('hashchange', checkHashRoute);

      function onBloggerLiveFeedLoaded(data) {
        if (!data || !data.feed || !data.feed.entry || data.feed.entry.length === 0) return;
        var entries = data.feed.entry;
        var newlyAdded = [];
        for (var i = 0; i < entries.length; i++) {
          var entry = entries[i];
          var title = entry.title ? (entry.title.$t || '') : '';
          var contentHtml = entry.content ? (entry.content.$t || '') : (entry.summary ? entry.summary.$t : '');
          var published = entry.published ? entry.published.$t.split('T')[0] : new Date().toISOString().split('T')[0];
          
          var labels = [];
          if (entry.category) {
            for (var c = 0; c < entry.category.length; c++) {
              if (entry.category[c].term) labels.push(entry.category[c].term);
            }
          }

          var link = '';
          if (entry.link) {
            for (var l = 0; l < entry.link.length; l++) {
              if (entry.link[l].rel === 'alternate') {
                link = entry.link[l].href;
                break;
              }
            }
          }

          var postId = 'live-post-' + (entry.id ? entry.id.$t.replace(/[^a-zA-Z0-9]/g, '-').slice(-20) : i);

          var exists = ALL_JOBS.some(function(j) {
            return j.title.toLowerCase().trim() === title.toLowerCase().trim();
          });

          if (!exists && title) {
            var cleanTitle = title.replace(/\s*#[a-zA-Z0-9_\s,#]+$/, '').trim();
            if (!cleanTitle) cleanTitle = title;

            function extractTableCell(html, labelPattern) {
              var re = new RegExp('<td[^>]*>[^<]*' + labelPattern + '[^<]*<\\/td>\\s*<td[^>]*>([\\s\\S]*?)<\\/td>', 'i');
              var m = html.match(re);
              if (m && m[1]) {
                return m[1].replace(/<[^>]+>/g, '').trim();
              }
              return '';
            }

            var cellOrg = extractTableCell(contentHtml, '(?:Recruiting Authority|Hiring Authority|Authority)');
            var cellPost = extractTableCell(contentHtml, '(?:Post Name|Designation|Role)');
            var cellVac = extractTableCell(contentHtml, '(?:Total Vacancies|Vacancies|Total Posts)');
            var cellSal = extractTableCell(contentHtml, '(?:Salary|Pay Scale)');
            var cellQual = extractTableCell(contentHtml, '(?:Qualification|Eligibility|Education)');
            var cellAge = extractTableCell(contentHtml, '(?:Age Limit|Age)');
            var cellLoc = extractTableCell(contentHtml, '(?:Job Location|Location)');
            var cellFee = extractTableCell(contentHtml, '(?:Application Fee|Fee)');
            var cellLastDate = extractTableCell(contentHtml, '(?:Last Date|Closing Date|Apply By)');
            var cellStartDate = extractTableCell(contentHtml, '(?:Online Application Starts|Start Date)');

            // Find qualification from labels if cell is empty or 'Required'
            var qualFromLabels = '';
            for (var lb = 0; lb < labels.length; lb++) {
              var lLower = labels[lb].toLowerCase();
              if (lLower.indexOf('pass') !== -1 || lLower.indexOf('degree') !== -1 || lLower.indexOf('diploma') !== -1 || lLower.indexOf('iti') !== -1 || lLower.indexOf('graduate') !== -1 || lLower.indexOf('b.sc') !== -1 || lLower.indexOf('b.tech') !== -1 || lLower.indexOf('nursing') !== -1 || lLower.indexOf('clerk') !== -1) {
                qualFromLabels = labels[lb];
                break;
              }
            }

            // Find organization name from labels (skip generic qualification/category labels)
            var orgFromLabels = '';
            for (var ol = 0; ol < labels.length; ol++) {
              var oLower = labels[ol].toLowerCase();
              if (oLower.indexOf('pass') === -1 && oLower.indexOf('govt jobs') === -1 && oLower.indexOf('job alerts') === -1 && oLower.indexOf('degree') === -1 && oLower.indexOf('diploma') === -1 && oLower.indexOf('iti') === -1 && oLower.indexOf('central govt') === -1) {
                orgFromLabels = labels[ol];
                break;
              }
            }

            var qual = cellQual;
            if (!qual || qual.toLowerCase() === 'required' || qual.length < 3) {
              qual = qualFromLabels || 'Any Degree / 12th / 10th Pass';
            }

            var orgName = cellOrg;
            if (!orgName || orgName.toLowerCase().indexOf('pass') !== -1 || orgName.toLowerCase().indexOf('degree') !== -1) {
              orgName = orgFromLabels || (labels.length > 0 ? labels[0] : 'Govt Recruitment');
            }

            var postName = cellPost || cleanTitle;
            var vacancies = cellVac || 'Various Posts';
            var salary = cellSal || 'As per Govt Norms';
            var ageLimit = cellAge || '18-40 Years';
            var location = cellLoc || ((labels.indexOf('Kerala Govt Jobs') !== -1 || labels.indexOf('Kerala PSC') !== -1) ? 'Kerala' : 'All India');
            var fee = cellFee || 'Refer Notification';
            var lastDate = cellLastDate || published;
            var startDate = cellStartDate || published;

            // Extract genuine external official application and PDF links from post content
            var linkMatches = contentHtml.match(/href=['"](https?:\/\/[^'"]+)['"]/gi) || [];
            var externalLinks = [];
            for (var m = 0; m < linkMatches.length; m++) {
              var cleanHref = linkMatches[m].replace(/^href=['"]|['"]$/gi, '');
              if (cleanHref.indexOf('blogger.com') === -1 && cleanHref.indexOf('blogspot.com') === -1 && cleanHref.indexOf('google.com') === -1) {
                externalLinks.push(cleanHref);
              }
            }

            var applyUrl = externalLinks.length > 0 ? externalLinks[0] : (link || 'https://www.google.com');
            var pdfUrl = '';
            for (var p = 0; p < externalLinks.length; p++) {
              if (externalLinks[p].toLowerCase().indexOf('.pdf') !== -1) {
                pdfUrl = externalLinks[p];
                break;
              }
            }
            if (!pdfUrl) {
              pdfUrl = externalLinks.length > 1 ? externalLinks[1] : applyUrl;
            }

            var websiteDomain = 'Official Portal';
            if (applyUrl && applyUrl.indexOf('http') === 0) {
              websiteDomain = applyUrl.replace(/^https?:\/\//, '').split('/')[0];
            }

            var itemType = 'notification';
            if (title.toLowerCase().indexOf('admit') !== -1 || title.toLowerCase().indexOf('hall ticket') !== -1) itemType = 'admit_card';
            else if (title.toLowerCase().indexOf('result') !== -1 || title.toLowerCase().indexOf('ranked list') !== -1) itemType = 'result';
            else if (title.toLowerCase().indexOf('answer key') !== -1) itemType = 'answer_key';
            else if (title.toLowerCase().indexOf('syllabus') !== -1) itemType = 'syllabus';

            newlyAdded.push({
              id: postId,
              title: cleanTitle,
              org_name: orgName,
              post_name: cleanTitle,
              vacancies: vacancies,
              salary: salary,
              qualification: qual,
              age_limit: ageLimit,
              location: (labels.indexOf('Kerala Govt Jobs') !== -1 || labels.indexOf('Kerala PSC') !== -1) ? 'Kerala' : 'All India',
              fee: 'Refer Notification',
              category: labels.length > 0 ? labels[0] : 'Central Govt Jobs',
              labels: labels,
              start_date: published,
              last_date: lastDate,
              apply_url: applyUrl,
              pdf_url: pdfUrl,
              website: websiteDomain,
              item_type: itemType,
              content_html: contentHtml
            });
          }
        }

        if (newlyAdded.length > 0) {
          ALL_JOBS = newlyAdded.concat(ALL_JOBS);
          activeFilteredJobs = ALL_JOBS;
          var heroCount = document.getElementById('heroActiveCount');
          if (heroCount) heroCount.innerText = ALL_JOBS.length + '+';
          updateChannelCounts();
          updateCategoryCounts();
          filterJobs();
        }
      }
      window.onBloggerLiveFeedLoaded = onBloggerLiveFeedLoaded;

      function syncLiveBloggerPosts() {
        try {
          var script = document.createElement('script');
          script.src = '/feeds/posts/default?alt=json-in-script&callback=onBloggerLiveFeedLoaded&max-results=50';
          script.async = true;
          document.body.appendChild(script);
        } catch (e) {}
      }

      var isNativePostPage = (window.location.pathname.indexOf('.html') !== -1) || (document.getElementById('nativePostContainer') !== null);

      function initPortal() {
        updateDynamicYear();
        var heroCount = document.getElementById('heroActiveCount');
        if (heroCount) heroCount.innerText = ALL_JOBS.length + '+';
        updateChannelCounts();
        updateCategoryCounts();

        if (isNativePostPage) {
          var hero = document.getElementById('heroSearchSection');
          if (hero) hero.style.display = 'none';
          var feedWrapper = document.getElementById('jobFeedWrapper');
          if (feedWrapper) feedWrapper.style.display = 'none';
          var articleView = document.getElementById('fullJobArticleView');
          if (articleView) articleView.style.display = 'none';
        } else {
          renderJobCards(ALL_JOBS);
          checkHashRoute();
        }
        syncLiveBloggerPosts();
      }

      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initPortal);
      } else {
        initPortal();
      }
      //]]>
    </script>
  </body>
</html>"""

def generate_theme():
    jobs_json_str = json.dumps(JOBS_150, ensure_ascii=False).replace("</script>", "<\\/script>")
    final_theme = THEME_TEMPLATE.replace("__JOBS_JSON__", jobs_json_str)

    out_file = os.path.join(os.path.dirname(__file__), "job_theme.xml")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(final_theme.strip())

    # Strict SAX Validation
    xml.sax.parseString(final_theme.encode('utf-8'), xml.sax.ContentHandler())
    print("SUCCESS: 'job_theme.xml' (Version 5.0) with Clean State Placement, Big Mobile Titles & Full Category Counts validated with 0 errors!")

if __name__ == "__main__":
    generate_theme()
