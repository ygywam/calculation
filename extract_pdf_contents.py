import pymupdf, glob, json, os

pdf_list = [
    '1. 함수의 극한과 연속 1. 함수의 극한.pdf',
    '1. 함수의 극한과 연속 2. 함수의 극한에 대한 성질.pdf',
    '1. 함수의 극한과 연속 3. 함수의 연속.pdf',
    '1. 함수의 극한과 연속 4. 연속함수의 성질.pdf',
    '1. 함수의 극한과 연속 대단원마무리.pdf',
    '2. 미분 1. 미분계수.pdf',
    '2. 미분 2. 미분가능성과 연속성.pdf',
    '2. 미분 3. 도함수.pdf',
    '2. 미분 4. 접선의 방정식.pdf',
    '2. 미분 5. 평균값정리.pdf',
    '2. 미분 6. 함수의 증가와 감소, 극대와 극소.pdf',
    '2. 미분 7. 함수의 그래프.pdf'
]

summary = {}
for p in pdf_list:
    if not os.path.exists(p):
        print("Missing:", p)
        continue
    doc = pymupdf.open(p)
    pages = []
    for i in range(len(doc)):
        text = doc[i].get_text().strip()
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        pages.append({
            'page': i + 1,
            'line_count': len(lines),
            'header': lines[:4] if lines else [],
            'sample': '\n'.join(lines[:12]) if lines else ''
        })
    summary[p] = {
        'page_count': len(doc),
        'pages': pages
    }
    print(f"Extracted: {p} ({len(doc)} pages)")

with open('new_12_pdf_summary.json', 'w', encoding='utf-8') as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print("Saved to new_12_pdf_summary.json")
