from fastapi import APIRouter, UploadFile, File, HTTPException, Depends, BackgroundTasks
from src.document_processing.pdf_parser import PDFParser
from src.document_processing.chunker import Chunker
from src.vector_store.manager import VectorStoreManager
from src.ml.predictor import DocumentPredictor
from sqlalchemy.orm import Session
import os
import uuid
from sqlalchemy.orm import Session
from src.database.base import get_db
from src.database.models import Document
router = APIRouter(
    prefix="/documents",
    tags=["Document Management"]
)
UPLOAD_DIR = "data/raw_documents"
os.makedirs(UPLOAD_DIR, exist_ok=True)
def process_document(
    doc_id: str,
    file_path: str,
    file_name: str
):
    db = next(get_db())
    try:
        document = db.query(Document).filter(
            Document.doc_id == doc_id
        ).first()
        parser = PDFParser()
        pages = parser.extract_text(
            file_path,
            doc_id
        )
        document_text = "\n".join(
            page["text"] for page in pages
        )[:10000]
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
            file_name
        )
        document.total_pages = len(pages)
        document.total_chunks = len(chunks)
        document.processing_status = "PROCESSED"
        db.commit()
    except Exception as e:
        document.processing_status = "FAILED"
        db.commit()
        print(e)
    finally:
        db.close()

@router.post("/upload")
async def upload_document(
    background_tasks: BackgroundTasks,
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
        processing_status="PROCESSING"
    )
    db.add(document)
    db.commit()
    db.refresh(document)

    background_tasks.add_task(
        process_document,
        doc_id,
        file_path,
        file.filename
    )
    return {
    "message": "Document uploaded successfully.",
    "doc_id": doc_id,
    "status": "PROCESSING"
}