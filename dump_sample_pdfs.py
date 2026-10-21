import pymupdf, sys

def dump_pdf(filename, max_pages=10):
    doc = pymupdf.open(filename)
    print(f"=== {filename} (Total {len(doc)} pages) ===")
    for i in range(min(len(doc), max_pages)):
        text = doc[i].get_text()
        print(f"--- Page {i+1} ---")
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        for l in lines[:15]:
            print("  ", l)

if __name__ == '__main__':
    for fname in [
        '1. 함수의 극한과 연속 1. 함수의 극한.pdf',
        '1. 함수의 극한과 연속 2. 함수의 극한에 대한 성질.pdf',
        '1. 함수의 극한과 연속 3. 함수의 연속.pdf',
        '1. 함수의 극한과 연속 4. 연속함수의 성질.pdf',
        '1. 함수의 극한과 연속 대단원마무리.pdf'
    ]:
        dump_pdf(fname, max_pages=3)
