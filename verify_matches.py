import glob
import os

html_files = sorted([f for f in glob.glob('*.html') if f != 'index.html'])
pdf_files = sorted(glob.glob('*.pdf'))

print(f"HTML Count: {len(html_files)}, PDF Count: {len(pdf_files)}")

for h in html_files:
    base = h[:-5]
    pdf = base + ".pdf"
    exists = os.path.exists(pdf)
    print(f"[{'O' if exists else 'X'}] HTML: {h} -> PDF: {pdf}")
