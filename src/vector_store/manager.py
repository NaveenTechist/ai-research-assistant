from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer


class VectorStoreManager:

    def __init__(self):

        self.embedding_model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        self.client = PersistentClient(
            path="data/vector_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

    def index_chunks(self, chunks, file_name):
        for chunk in chunks:
            embedding = self.embedding_model.encode(
                chunk["text"]
            ).tolist()
            self.collection.add(
                ids=[chunk["chunk_id"]],
                embeddings=[embedding],
                documents=[chunk["text"]],
                metadatas=[{
                    "doc_id": chunk["doc_id"],
                    "file_name": file_name,
                    "page_number": chunk["page_number"]
                }]
            )
    def semantic_search(
        self,
        query: str,
        top_k: int = 4
        ):
        query_embedding = self.embedding_model.encode(
            query
        ).tolist()
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        return results
    def keyword_search(
    self,
    keyword: str
):
        results = self.collection.get()
        matched_chunks = []
        for i, document in enumerate(results["documents"]):
            if keyword.lower() in document.lower():
                matched_chunks.append({
                    "id": results["ids"][i],
                    "document": document,
                    "metadata": results["metadatas"][i]
                })
        return matched_chunks
    
    def hybrid_search(
        self,
        query: str,
        top_k: int = 4
        ):
        semantic_results = self.semantic_search(
            query,
            top_k
        )
        keyword_results = self.keyword_search(
            query
        )
        return {
            "semantic": semantic_results,
            "keyword": keyword_results
        }