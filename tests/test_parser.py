from src.document_processing.pdf_parser import PDFParser

parser = PDFParser()

pages = parser.extract_text(
    document.file_path,
    document.doc_id
)

for page in pages:
    print("=" * 50)
    print(page["page_number"])
    print(page["text"][:300])