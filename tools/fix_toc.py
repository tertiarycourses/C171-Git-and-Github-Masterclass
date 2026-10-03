"""Rewrite tab-separated static TOC page numbers from the rendered PDF."""
import subprocess, sys
from docx import Document
docx, pdf = sys.argv[1], sys.argv[2]
n = int([l for l in subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout.splitlines() if l.startswith("Pages")][0].split()[1])
pages = [subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), "-layout", pdf, "-"], capture_output=True, text=True).stdout for i in range(1, n + 1)]
d = Document(docx)
toc = [p for p in d.paragraphs if "\t" in p.text and p.text.rsplit("\t", 1)[-1].strip().isdigit()]
start = 1 + max(i + 1 for i in range(n) if "TABLE OF CONTENTS" in pages[i])
changed = 0
for p in toc:
    title = p.text.rsplit("\t", 1)[0].strip()
    found = next((i + 1 for i in range(start - 1, n) if title in " ".join(pages[i].split())), None)
    if found is None:
        print("NOT FOUND:", title); continue
    start = found
    old = p.text.rsplit("\t", 1)[-1].strip()
    if old != str(found):
        for r in reversed(p.runs):
            if r.text.strip() == old: r.text = r.text.replace(old, str(found)); changed += 1; break
            if r.text.endswith(old): r.text = r.text[: -len(old)] + str(found); changed += 1; break
    print(f"{found:>3}  {title}")
d.save(docx)
print("changed", changed)
