import os
from google import genai
from dotenv import load_dotenv
from src.vector_store.manager import VectorStoreManager
load_dotenv()

class QAChain:
    def __init__(self):
        self.client = genai.Client(
        api_key=os.getenv("GOOGLE_API_KEY")
        )
        self.vector_store = VectorStoreManager()
        self.memory = {}
    
    def get_history(
    self,
    session_id: str
):

        return self.memory.get(session_id, [])
    
    def update_history(
        self,
        session_id: str,
        question: str,
        answer: str
    ):
        if session_id not in self.memory:
            self.memory[session_id] = []
        self.memory[session_id].append({
            "question": question,
            "answer": answer
        })
    
    def retrieve_context(
    self,
    question: str
):

        results = self.vector_store.semantic_search(
            question,
            top_k=4
        )   
        context = ""
        citations = []
        seen = set()
        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        for doc, meta in zip(documents, metadatas):
            context += (
                f"\nSource : {meta['file_name']}"
                f"\nPage : {meta['page_number']}\n"
                f"{doc}\n"
            )
            citations.append({
                "document": meta["file_name"],
                "page": meta["page_number"]
            })
        return context, citations
    def build_prompt(
    self,
    history,
    context,
    question
):
        return f"""
    Answer ONLY using supplied context.
    If answer not found
    say exactly
    "I cannot determine the answer from the provided documents."
    Do not use outside knowledge.
    Provide answer.
    Then
    Sources:
    - filename
    - page
    {history}
    Context
    {context}
    Question
    {question}
    Return a clear answer.
    At the end include citations.
    """       

    def ask(
    self,
    question: str,
    session_id: str = "default"
):

        history = self.get_history(
            session_id
        )
        history_text = ""
        for item in history:
            history_text += (
                f"User : {item['question']}\n"
                f"Assistant : {item['answer']}\n"
            )
        context, citations = self.retrieve_context(
            question
        )
        prompt = self.build_prompt(
            history_text,
            context,
            question
        )
        response = self.client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
        )

        answer = response.text
        self.update_history(
            session_id,
            question,
            answer
        )
        return {
            "answer": answer,
            "citations": citations
        }