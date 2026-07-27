from fastapi import FastAPI
from src.database.base import Base
from src.database.base import engine
import src.database.models
from routes.document_routes import router as document_router
from routes.search_routes import router as search_router
from routes.analytics_routes import router as analytics_router

Base.metadata.create_all(bind=engine)
app = FastAPI(title="AI Research Assistant")
app.include_router(document_router)
app.include_router(search_router)
app.include_router(analytics_router)


@app.get("/")
def home():
    return {
        "message": "AI Research Assistant Running"
    }