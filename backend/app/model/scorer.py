from sklearn.metrics.pairwise import cosine_similarity
from app.model.embeddings import get_embedding

SKILLS = [
    "python",
    "machine learning",
    "deep learning",
    "nlp",
    "pytorch",
    "scikit-learn",
]

def extract_skills(text):
    return [s for s in SKILLS if s in text]

def score_resume(resume, jd):
    emb1 = get_embedding(resume)
    emb2 = get_embedding(jd)

    semantic_score = cosine_similarity([emb1],[emb2])[0][0]

    resume_skills = extract_skills(resume)
    jd_skills = extract_skills(jd)

    skill_score = len(set(resume_skills)&set(jd_skills)) / max(len(jd_skills),1)

    final_score = (0.7*semantic_score + 0.3*skill_score)*100

    return round(final_score,2), resume_skills, jd_skills
