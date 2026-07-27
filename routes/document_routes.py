from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from src.document_processing.pdf_parser import PDFParser
from src.document_processing.chunker import Chunker
from src.vector_store.manager import VectorStoreManager
from src.ml.predictor import DocumentPredictor
from sqlalchemy.orm import Session
import os
import uuid

from src.database.base import get_db
from src.database.models import Document

router = APIRouter(
    prefix="/documents",
    tags=["Document Management"]
)

UPLOAD_DIR = "data/raw_documents"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    existing_document = db.query(Document).filter(
    Document.file_name == file.filename
    ).first()

    if existing_document:
        return {
            "message": "Document already exists.",
            "doc_id": existing_document.id
        }

    doc_id = str(uuid.uuid4())

    file_path = os.path.join(
        UPLOAD_DIR,
        f"{doc_id}_{file.filename}"
    )

    with open(file_path, "wb") as pdf:
        pdf.write(await file.read())

    document = Document(
        doc_id=doc_id,
        file_name=file.filename,
        file_path=file_path,
        processing_status="PROCEED"
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    # Parse PDF
    parser = PDFParser()
    
    pages = parser.extract_text(
        file_path,
        doc_id
    )
    document_text = "\n".join(
    page["text"] for page in pages
    )
    predictor = DocumentPredictor()
    prediction = predictor.predict(
    document_text
    )    
    document.category = prediction["category"]
    predictor = DocumentPredictor()
    prediction = predictor.predict(
        document_text
    )
    document.category = prediction["category"]
    processor = Chunker()
    chunks = processor.create_chunks(
        pages
    )
    vector_store = VectorStoreManager()

    vector_store.index_chunks(
        chunks,
        file.filename
    )

    # Update Metadata
    document.total_pages = len(pages)
    document.total_chunks = len(chunks)
    document.processing_status = "PROCESSED"

    db.commit()
    db.refresh(document)

    return {
        "message": "Document uploaded successfully",
        "doc_id": doc_id,
        "category": document.category,
        "status": "PROCESSED"
    }