from fastapi import FastAPI
from app.api.routes.documents import router as document_router
from app.api.routes.statistics import router as statistics_router
from app.api.routes.training import router as training_router

app = FastAPI(
    title="English Essay Error Detection API",
    version="1.0.0"
)
app.include_router(document_router)
app.include_router(statistics_router)
app.include_router(training_router)


@app.get("/")
def root():
    return {
        "message": "English Essay Error Detection System"
    }
