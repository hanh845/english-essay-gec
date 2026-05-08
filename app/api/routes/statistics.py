from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.core.database import get_db

router = APIRouter()


@router.get("/statistics/user/{author_id}")
def statistics_by_user(
        author_id: str,
        db: Session = Depends(get_db)
):
    query = """
    SELECT
        a.name,
        COUNT(p.prediction_id) AS total_errors,
        COUNT(DISTINCT d.document_id) AS total_documents,
        AVG(p.confidence) AS avg_confidence
    FROM authors a 
    JOIN document_authors da
        ON a.author_id = da.author_id
    JOIN documents d
        ON da.document_id = d.document_id
    JOIN document_versions dv
        ON d.document_id = dv.document_id
    JOIN sentences s
        ON dv.version_id = s.version_id
    JOIN predictions p
        ON s.sentence_id = p.sentence_id
    WHERE a.author_id = :author_id
        AND p.label = 1
    GROUP BY a.name
    """

    result = db.execute(
        text(query),
        {"author_id": author_id}
    )

    rows = result.fetchall()

    return [dict(r._mapping) for r in rows]


@router.get("/statistics/errors/type")
def statistics_error_type(db: Session = Depends(get_db)):
    query = """
    SELECT
        error_type,
        COUNT(*) AS total
    FROM predictions
    WHERE label = 1
    GROUP BY error_type
    ORDER BY total DESC
    """

    result = db.execute(text(query))

    rows = result.fetchall()

    return [dict(r._mapping) for r in rows]

