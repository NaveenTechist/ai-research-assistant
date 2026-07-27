from fastapi import APIRouter
from src.analytics.metrics import AnalyticsMetrics

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

metrics = AnalyticsMetrics()

@router.get("/metrics")
async def get_metrics():
    return metrics.get_metrics()