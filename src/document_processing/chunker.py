from typing import List, Dict

class Chunker:
    def __init__(
        self,
        chunk_size=1000,
        overlap=150
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap
    def create_chunks(
        self,
        pages: List[Dict]
    ):
        chunks = []
        chunk_id = 0
        for page in pages:
            text = page["text"]
            start = 0
            while start < len(text):
                end = start + self.chunk_size
                chunk = text[start:end]
                chunks.append({
                    "chunk_id": f"{page['doc_id']}_c{chunk_id}",
                    "doc_id": page["doc_id"],
                    "page_number": page["page_number"],
                    "text": chunk
                })
                chunk_id += 1
                start += (
                    self.chunk_size
                    - self.overlap
                )
        return chunks