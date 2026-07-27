from sqlalchemy import func
from src.database.base import SessionLocal
from src.database.models import Document

class AnalyticsMetrics:

    def __init__(self):
        self.db = SessionLocal()

    def total_documents(self):
        return self.db.query(Document).count()

    def total_chunks(self):
        result = self.db.query(
            func.sum(Document.total_chunks)
        ).scalar()
        return result or 0

    def category_distribution(self):
        results = self.db.query(
            Document.category,
            func.count(Document.id)
        ).group_by(
            Document.category
        ).all()
        distribution = {}
        for category, count in results:
            distribution[category] = count
        return distribution

    def top_documents(self):
        documents = self.db.query(
            Document.file_name,
            Document.total_chunks
        ).order_by(
            Document.total_chunks.desc()
        ).limit(5).all()
        output = []
        for document in documents:
            output.append({
                "file_name": document.file_name,
                "total_chunks": document.total_chunks
            })
        return output

    def get_metrics(self):
        return {
            "total_documents": self.total_documents(),
            "total_chunks": self.total_chunks(),
            "category_distribution": self.category_distribution(),
            "top_documents": self.top_documents()
        }