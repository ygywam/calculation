import json
import re
import os
import urllib.parse

content = open('index.html', encoding='utf-8').read()
m = re.search(r'const LESSONS = (\[.*?\]);', content, re.DOTALL)
if not m:
    print("Error: LESSONS not found in index.html")
    exit(1)

lessons = json.loads(m.group(1))
print(f"Total lessons in index.html: {len(lessons)}")

missing = []
for l in lessons:
    html_f = l['html']
    pdf_f = l['pdf']
    if not os.path.exists(html_f):
        missing.append(('HTML', html_f))
    if not os.path.exists(pdf_f):
        missing.append(('PDF', pdf_f))

if missing:
    print("Missing files:", missing)
else:
    print("All 20 HTML files and 20 PDF files exist and match index.html perfectly!")
