from google import genai
import os
from dotenv import load_dotenv
from src.vector_store.manager import VectorStoreManager
load_dotenv()

class DocumentSummarizer:

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
    
    def summarize(
    self,
    doc_id: str
):
        context = self.get_document_chunks(
            doc_id
        )
        prompt = f"""
            Summarize the document using ONLY the supplied context.
            Create the response in this format.
            1. Executive Summary
            2. Technical Summary
            3. Bullet Point Breakdown
            4. Key Takeaways
            Context:
            {context}
            """
        response = self.client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
        )
        return {
            "doc_id": doc_id,
            "summary": response.text
        }