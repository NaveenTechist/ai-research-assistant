from fastapi import APIRouter
from pydantic import BaseModel
from src.rag.summarizer import DocumentSummarizer
from src.rag.comparator import DocumentComparator

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)

summarizer = DocumentSummarizer()
comparator = DocumentComparator()

class SummaryRequest(BaseModel):
    doc_id: str

class CompareRequest(BaseModel):
    doc_id_1: str
    doc_id_2: str

@router.post("/summarize")
async def summarize_document(request: SummaryRequest):
    return summarizer.summarize(request.doc_id)

@router.post("/compare")
async def compare_documents(request: CompareRequest):
    return comparator.compare(
        request.doc_id_1,
        request.doc_id_2
    )