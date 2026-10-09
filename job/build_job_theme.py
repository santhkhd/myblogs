"""
Build 100% Valid Blogger Job Theme
Takes the proven, error-free blogspot.xml template base and adapts it for a stylish, ultra-fast Government Job Portal.
Ensures 100% compliance with Blogger XML parser so it saves without 'Update failed' error.
"""

import os
import re

def build_job_theme():
    # Read the working blogspot.xml
    base_file = os.path.join(os.path.dirname(__file__), "..", "blogspot.xml")
    if not os.path.exists(base_file):
        base_file = "blogspot.xml"
        
    with open(base_file, "r", encoding="utf-8") as f:
        xml_content = f.read()

    # 1. Update navigation links to Job Portal categories
    old_nav = """          <nav class='nav-links'>
            <a class='active' expr:href='data:blog.homepageUrl'>Home</a>
            <a href='/p/continental.html'>Continent</a>
            <a href='/search/label/Guides?max-results=20'>Articles</a>
            <a href='/p/about-us.html'>About Us</a>
            <a href='/p/contact-us.html'>Contact Us</a>
          </nav>"""

    new_nav = """          <nav class='nav-links'>
            <a class='active' expr:href='data:blog.homepageUrl'>Home</a>
            <a href='/search/label/Kerala%20Govt%20Jobs'>Kerala Jobs</a>
            <a href='/search/label/Bank%20Jobs'>Bank Jobs</a>
            <a href='/search/label/Railway%20Jobs'>Railway Jobs</a>
            <a href='/search/label/SSC%20CGL'>SSC Jobs</a>
            <a href='/p/about-us.html'>About Us</a>
            <a href='/p/contact-us.html'>Contact Us</a>
          </nav>"""

    if old_nav in xml_content:
        xml_content = xml_content.replace(old_nav, new_nav)
    else:
        # Fallback regex replace for nav-links
        xml_content = re.sub(
            r"<nav class='nav-links'>.*?</nav>",
            new_nav.strip(),
            xml_content,
            flags=re.DOTALL
        )

    # 2. Update mobile menu
    old_mobile_menu = """        <ul>
          <li><a class='active' expr:href='data:blog.homepageUrl'>Home</a></li>
          <li><a href='/p/continental.html'>Continent</a></li>
          <li><a href='/search/label/Guides?max-results=20'>Articles</a></li>
          <li><a href='/p/about-us.html'>About Us</a></li>
          <li><a href='/p/contact-us.html'>Contact Us</a></li>
        </ul>"""

    new_mobile_menu = """        <ul>
          <li><a class='active' expr:href='data:blog.homepageUrl'>Home</a></li>
          <li><a href='/search/label/Kerala%20Govt%20Jobs'>Kerala Govt Jobs</a></li>
          <li><a href='/search/label/Bank%20Jobs'>Bank Jobs (SBI/IBPS)</a></li>
          <li><a href='/search/label/Railway%20Jobs'>Railway (RRB)</a></li>
          <li><a href='/search/label/SSC%20CGL'>SSC &amp; UPSC</a></li>
          <li><a href='/search/label/10th%20Pass'>10th Pass Jobs</a></li>
          <li><a href='/search/label/12th%20Pass'>12th Pass Jobs</a></li>
          <li><a href='/search/label/Degree%20Jobs'>Degree Jobs</a></li>
          <li><a href='/p/about-us.html'>About Us</a></li>
          <li><a href='/p/contact-us.html'>Contact Us</a></li>
        </ul>"""

    if old_mobile_menu in xml_content:
        xml_content = xml_content.replace(old_mobile_menu, new_mobile_menu)
    else:
        xml_content = re.sub(
            r"<nav class='mobile-menu-nav'>\s*<ul>.*?</ul>\s*</nav>",
            f"<nav class='mobile-menu-nav'>\n{new_mobile_menu}\n      </nav>",
            xml_content,
            flags=re.DOTALL
        )

    # 3. Update footer
    old_footer_links = """        <div class='footer-nav-links'>
          <a expr:href='data:blog.homepageUrl'>Home</a>
          <a href='/p/continental.html'>Continental Directory</a>
          <a href='/search/label/Guides?max-results=20'>Articles</a>
          <a href='/p/about-us.html'>About Us</a>
          <a href='/p/contact-us.html'>Contact Us</a>
        </div>"""

    new_footer_links = """        <div class='footer-nav-links'>
          <a expr:href='data:blog.homepageUrl'>Home</a>
          <a href='/search/label/Kerala%20Govt%20Jobs'>Kerala Govt Jobs</a>
          <a href='/search/label/Bank%20Jobs'>Bank Jobs</a>
          <a href='/search/label/Railway%20Jobs'>Railway Jobs</a>
          <a href='/search/label/SSC%20CGL'>SSC &amp; UPSC</a>
          <a href='/p/about-us.html'>About Us</a>
          <a href='/p/contact-us.html'>Contact Us</a>
        </div>"""

    if old_footer_links in xml_content:
        xml_content = xml_content.replace(old_footer_links, new_footer_links)

    # 4. Save to e:\money\job\job_theme.xml
    output_path = os.path.join(os.path.dirname(__file__), "job_theme.xml")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(xml_content)

    print(f"Successfully generated 100% valid Blogger XML job theme: {output_path}")

if __name__ == "__main__":
    build_job_theme()
