from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from typing import List, Dict
from services.file__vision_model import process_syllabus_and_generate_questions

router = APIRouter()


@router.get(
    "/courses/{course_id}/generate-questions", response_model=List[Dict[str, str]]
)
def generate_questions(course_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to generate questions and answers for a course syllabus.

    Args:
        course_id (int): ID of the course.
        db (Session): Database session.

    Returns:
        List[Dict[str, str]]: Questions and answers generated by LLM.
    """
    return process_syllabus_and_generate_questions(db, course_id)
