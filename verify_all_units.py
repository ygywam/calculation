import glob
import os

files = sorted([f for f in glob.glob('*.html') if f != 'index.html'])
print(f"Total lesson HTMLs: {len(files)}")
for i, f in enumerate(files):
    size = os.path.getsize(f)
    content = open(f, encoding='utf-8').read()
    has_canvas = "wb-canvas" in content
    has_toolbar = "wb-toolbar" in content
    has_scratchpad = "scratchpad-canvas" in content
    print(f"[{i+1:02d}] {f} | {size:,} bytes | wb-canvas: {has_canvas} | wb-toolbar: {has_toolbar} | scratchpad: {has_scratchpad}")
