import spacy
import os
from sentence_transformers import SentenceTransformer, util

# ✅ Load spaCy Model (Stored Locally)
spacy_model_path = os.path.join(os.path.dirname(__file__), "models/en_core_web_sm")

try:
    nlp = spacy.load(spacy_model_path)
    print("✅ spaCy model loaded successfully!")
except OSError:
    raise RuntimeError(f"❌ spaCy model not found in {spacy_model_path}. Ensure it's inside the repository.")

# ✅ Load Sentence Transformer Model (For Resume Matching)
model = SentenceTransformer("all-MiniLM-L6-v2")

# ✅ Extract Keywords from Job Description
def extract_keywords(job_desc):
    """
    Extracts important keywords from the job description using spaCy NLP.
    """
    doc = nlp(job_desc.lower())
    return list(set(token.lemma_ for token in doc if token.pos_ in ['NOUN', 'PROPN', 'VERB', 'ADJ'] and not token.is_stop))

# ✅ Match Job Descriptions with Resume
def match_job(resume_text, job_desc):
    """
    Uses Sentence Transformers to compare job description and resume similarity.
    Returns a match score between 0 and 100%.
    """
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_desc, convert_to_tensor=True)
    similarity_score = util.pytorch_cos_sim(resume_embedding, job_embedding).item()
    
    return round(similarity_score * 100, 2)  # Convert to percentage

# ✅ Suggest Resume Improvements Based on Missing Skills
def suggest_resume_improvements(resume_text, job_desc):
    """
    Suggests missing skills that should be added to the resume for better matching.
    """
    job_keywords = extract_keywords(job_desc)
    resume_keywords = extract_keywords(resume_text)

    missing_skills = list(set(job_keywords) - set(resume_keywords))

    return missing_skills

# ✅ Define Allowed Imports for Streamlit Cloud
__all__ = ["match_job", "suggest_resume_improvements"]
