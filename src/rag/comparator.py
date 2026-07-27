from google import genai
import os
from dotenv import load_dotenv
from src.vector_store.manager import VectorStoreManager

load_dotenv()


class DocumentComparator:

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GOOGLE_API_KEY")
        )
        self.vector_store = VectorStoreManager()

    def get_document_chunks(
        self,
        doc_id: str
    ):
        results = self.vector_store.collection.get()

        context = ""

        for document, metadata in zip(
            results["documents"],
            results["metadatas"]
        ):
            if metadata["doc_id"] == doc_id:
                context += document + "\n\n"

        return context

    def compare(
        self,
        doc_id_1: str,
        doc_id_2: str
    ):

        context1 = self.get_document_chunks(doc_id_1)
        context2 = self.get_document_chunks(doc_id_2)

        prompt = f"""
Compare ONLY the provided documents.

Document 1
{context1}

Document 2
{context2}

Create the comparison using:

1. Methodologies
2. Advantages
3. Disadvantages
4. Similarities
5. Implementation Approaches

If information is missing, clearly state it.
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return {
            "doc_id_1": doc_id_1,
            "doc_id_2": doc_id_2,
            "comparison": response.text
        }