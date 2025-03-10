import streamlit as st
import os
import pandas as pd
from backend.resume_matcher import match_job, suggest_resume_improvements
from backend.job_scraper import scrape_google_jobs
from backend.form_autofill import autofill_linkedin
from backend.database import insert_application, get_applications

# ✅ Streamlit App Title
st.title("AI Job Application Assistant 🚀")

# ✅ Sidebar Navigation
page = st.sidebar.radio("Navigation", ["Upload Resume", "Job Matches", "Applied Jobs"])

# ✅ Resume Upload Page
if page == "Upload Resume":
    st.header("📂 Upload Your Resume")
    uploaded_file = st.file_uploader("Upload a PDF resume", type=["pdf"])

    if uploaded_file:
        resume_text = uploaded_file.read().decode("utf-8")  # Convert to text
        st.session_state["resume"] = resume_text  # Store resume text
        st.success("✅ Resume uploaded successfully!")

# ✅ Job Matching Page
elif page == "Job Matches":
    st.header("🔍 Find the Best Job Matches")

    if "resume" not in st.session_state:
        st.warning("⚠️ Please upload your resume first.")
    else:
        # ✅ Scrape Jobs
        st.write("📡 Fetching jobs...")
        jobs = scrape_google_jobs()

        # ✅ Match Jobs with Resume
        matched_jobs = []
        for job in jobs:
            score = match_job(st.session_state["resume"], job["title"])
            missing_skills = suggest_resume_improvements(st.session_state["resume"], job["title"])
            matched_jobs.append({"Title": job["title"], "Company": job["company"], "Match Score": score, "Missing Skills": ", ".join(missing_skills), "Apply Link": job["link"]})

        # ✅ Display Results
        df = pd.DataFrame(matched_jobs).sort_values(by="Match Score", ascending=False)
        st.dataframe(df)

        # ✅ Allow Users to Apply
        if st.button("Apply for Best Matches"):
            best_match = df.iloc[0]  # Select top job
            insert_application(best_match["Title"], best_match["Company"])  # Store in database
            st.success(f"✅ Application started for {best_match['Title']} at {best_match['Company']}!")

# ✅ Applied Jobs Page
elif page == "Applied Jobs":
    st.header("📌 Your Applied Jobs")

    applied_jobs = get_applications()
    if applied_jobs:
        df = pd.DataFrame(applied_jobs, columns=["ID", "Title", "Company", "Applied On", "Status"])
        st.dataframe(df)
    else:
        st.info("No applications yet.")
