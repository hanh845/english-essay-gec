from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.database import get_db
from app.services.pdf_parser_service import extract_text_from_pdf
from app.services.sentence_service import split_sentences
from app.models.document import Document
from app.models.sentence import Sentence
import uuid
import os
from datetime import datetime

router = APIRouter()

UPLOAD_DIR = "data/uploads"


@router.post("/documents/upload")
async def upload_document(
        title: str,
        file: UploadFile = File(...),
        db: Session = Depends(get_db)
):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    extracted_text = extract_text_from_pdf(file_path)

    raw_sentences = split_sentences(extracted_text)

    document_id = str(uuid.uuid4())
    version_id = str(uuid.uuid4())

    document = Document(
        document_id=document_id,
        title=title,
        file_type="pdf",
        file_path=file_path,
        created_at=datetime.now()
    )


    db.add(document)
    db.commit()
    db.refresh(document)

    from app.models.document_version import DocumentVersion

    version = DocumentVersion(
        version_id=version_id,
        document_id=document_id,
        extracted_text=extracted_text,
        extraction_method="PyPDF2"
    )

    db.add(version)
    db.commit()

    db.refresh(version)

    for idx, sentence in enumerate(raw_sentences):
        sentence_obj = Sentence(
            sentence_id=str(uuid.uuid4()),
            document_id=document_id,
            version_id=version_id,
            content=sentence,
            position=idx + 1,
            is_clean=True
        )

        db.add(sentence_obj)

    db.commit()

    return {
        "document_id": document_id,
        "total_sentences": len(raw_sentences)
    }


@router.post("/documents/{document_id}/detect")
def detect_document_errors(
        document_id: str,
        db: Session = Depends(get_db)
):
    from app.models.document_version import DocumentVersion

    from app.services.prediction_service import predict_sentence

    versions = db.query(DocumentVersion).filter(
        DocumentVersion.document_id == document_id
    ).all()

    if len(versions) == 0:
        return {"message": "No version found"}

    version_id = versions[0].version_id

    sentences = db.query(Sentence).filter(
        Sentence.version_id == version_id
    ).all()

    predictions = []

    model_id = str(uuid.uuid4())

    for sentence in sentences:
        prediction = predict_sentence(
            db,
            sentence.sentence_id,
            sentence.content,
            model_id
        )

        predictions.append({
            "sentence": sentence.content,
            "corrected": prediction.corrected_text,
            "label": prediction.label,
            "confidence": prediction.confidence
        })

    return predictions


@router.get("/documents/{document_id}/errors")
def get_document_errors(
        document_id: str,
        db: Session = Depends(get_db)
):
    query = """
    SELECT
        p.prediction_id,
        s.content,
        p.corrected_text,
        p.error_type,
        p.confidence
    FROM predictions p 
    JOIN sentences s
        ON p.sentence_id = s.sentence_id
    JOIN document_versions dv
        ON s.version_id = dv.version_id
    WHERE dv.document_id = :document_id
        AND p.label = 1
    """

    result = db.execute(
        text(query),
        {"document_id": document_id}
    )

    rows = result.fetchall()

    return [dict(r._mapping) for r in rows]
