from fastapi import APIRouter
from pydantic import BaseModel

from src.vector_store.manager import VectorStoreManager
from src.rag.qa_chain import QAChain

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)

vector_store = VectorStoreManager()
qa_chain = QAChain()

class SearchRequest(BaseModel):
    query: str
    top_k: int = 4


class QuestionRequest(BaseModel):
    question: str

@router.post("/semantic")
async def semantic_search(
    request: SearchRequest
):

    results = vector_store.semantic_search(
        request.query,
        request.top_k
    )

    return {
        "query": request.query,
        "results": results
    }

@router.post("/question")
async def answer_question(
    request: QuestionRequest
):

    result = qa_chain.ask(
        request.question
    )

    return result