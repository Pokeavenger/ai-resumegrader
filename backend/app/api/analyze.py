from fastapi import APIRouter, UploadFile, Form
from app.utils.pdf_parser import extract_text_from_pdf
from app.utils.text_utils import clean_text
from app.model.scorer import score_resume

router = APIRouter()

@router.post("/analyze-resume")
async def analyze_resume(
    resume: UploadFile,
    job_description: str = Form(...)
):
    resume_text = extract_text_from_pdf(resume)
    resume_text = clean_text(resume_text)
    job_description = clean_text(job_description)

    score, r_skills, jd_skills = score_resume(resume_text, job_description)

    return {
        "score": score,
        "matched_skills": list(set(r_skills)&set(jd_skills)),
        "missing_skills": list(set(jd_skills)-set(r_skills))
    }
