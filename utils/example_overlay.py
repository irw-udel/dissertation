# from StackOverflow
# https://stackoverflow.com/questions/69781247/overlay-2-pdf-files-by-each-page-using-pymupdf

import fitz

# Set paths to files
doc_path = r'path\to\dissertation.pdf'
overlay_path = r'path\to\margin-template.pdf'
merge_result_path = r'path\to\dissertation-margin.pdf'

# Open files
doc1 = fitz.open(doc_path)
doc2 = fitz.open(overlay_path)

# Add overlay to each page
for i in range(doc1.page_count):
    page = doc1.load_page(i)
    page_front = fitz.open()
    page_front.insert_pdf(doc2, from_page=i, to_page=i)
    page.show_pdf_page(page.rect, page_front, pno=0, keep_proportion=True, overlay=True, oc=0, rotate=0, clip=None)

# Save output
doc1.save(merge_result_path, encryption=fitz.PDF_ENCRYPT_KEEP)