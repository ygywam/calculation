with open('3. 적분 5. 속도와 거리.html', encoding='utf-8') as f:
    c = f.read()

import re

# Find navigation links in sidebar
navs = re.findall(r'<a\b[^>]*href=["\']#(sec-[^"\']*)["\'][^>]*>(.*?)</a>', c, re.DOTALL)
print("=== SIDEBAR NAV LINKS ===")
for href, text in navs:
    clean_text = ' '.join(re.sub(r'<[^>]*>', '', text).split())
    print(f"#{href} : {clean_text}")

# Find key interactive components
print("\n=== KEY COMPONENTS ===")
print("scratchpad-canvas count:", c.count('scratchpad-canvas'))
print("solution-toggle or details:", c.count('toggleSolution') + c.count('<details'))
print("quiz or check items:", c.count('check-answer') + c.count('data-answer'))

# Check outline of main content
main_match = re.search(r'<main\b[^>]*>(.*?)</main>', c, re.DOTALL)
if main_match:
    main_c = main_match.group(1)
    headings = re.findall(r'<h[23]\b[^>]*>(.*?)</h[23]>', main_c, re.DOTALL)
    print("\n=== HEADINGS IN MAIN ===")
    for h in headings[:15]:
        print(" -", ' '.join(re.sub(r'<[^>]*>', '', h).split()))
