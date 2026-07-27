import fitz
from typing import List, Dict


class PDFParser:
    def extract_text(self, pdf_path: str, doc_id: str) -> List[Dict]:
        doc = fitz.open(pdf_path)
        extracted_pages = []
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text("text").strip()
            if text:
                extracted_pages.append({
                    "doc_id": doc_id,
                    "page_number": page_num + 1,
                    "text": text
                })
        doc.close()
        return extracted_pages