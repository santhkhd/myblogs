"""
Job Publisher Module
Converts formatted job posts into a valid Blogger Atom XML import file or sends directly via Blogger API.
"""

import os
import datetime
from xml.sax.saxutils import escape
from job_formatter import format_job_html

def generate_blogger_xml(jobs_list, output_filename="daily_jobs_export.xml"):
    """
    Generates a full Blogger Atom XML feed containing all given jobs.
    """
    xml_entries = []
    base_time = datetime.datetime.now(datetime.timezone.utc)
    
    for i, job in enumerate(jobs_list):
        post_time = (base_time - datetime.timedelta(minutes=i*15)).isoformat()
        content_html = format_job_html(job)
        
        categories_xml = "\n".join([
            f'    <category scheme="http://www.google.com/buzz/labels" term="{escape(lbl)}"/>'
            for lbl in job.get("labels", ["Govt Jobs", "Job Alerts"])
        ])
        
        entry = f"""  <entry>
    <id>tag:blogger.com,1999:blog-1.post-{job['id']}</id>
    <published>{post_time}</published>
    <updated>{post_time}</updated>
    <title type='text'>{escape(job['title'])}</title>
    <content type='html'>{escape(content_html)}</content>
    <author>
      <name>Daily Govt Job Alerts</name>
      <email>noreply@blogger.com</email>
    </author>
    <category scheme="http://schemas.google.com/g/2005#kind" term="http://schemas.google.com/blogger/2008/kind#post"/>
{categories_xml}
  </entry>"""
        xml_entries.append(entry)
        
    full_xml = f"""<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns='http://www.w3.org/2005/Atom' xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/' xmlns:blogger='http://schemas.google.com/blogger/2008' xmlns:georss='http://www.georss.org/georss' xmlns:gd='http://schemas.google.com/g/2005' xmlns:thr='http://purl.org/syndication/thread/1.0'>
  <id>tag:blogger.com,1999:blog-1</id>
  <updated>{datetime.datetime.now(datetime.timezone.utc).isoformat()}</updated>
  <title type='text'>Daily Government Job Alerts</title>
  <subtitle type='html'>Daily Kerala &amp; Central Government Job Notifications</subtitle>
  <generator version='7.00' uri='http://www.blogger.com'>Blogger</generator>
{"\n".join(xml_entries)}
</feed>"""

    output_path = os.path.join(os.path.dirname(__file__), output_filename)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_xml)
        
    return output_path
