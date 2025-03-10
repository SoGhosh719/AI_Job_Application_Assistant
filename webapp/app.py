import streamlit as st
import os
import pandas as pd
import sys

# ✅ Ensure Streamlit Can Find the `backend` Module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.resume_matcher import match_job, suggest_resume_improvements
from backend.job_scraper import scrape_google_jobs
from backend.form_autofill import autofill_linkedin
from backend.database import insert_application, get_applications

# ✅ Streamlit Page Configuration
st.set_page_config(page_title="AI Job Assistant", layout="wide")

# ✅ Sidebar Navigation
st.sidebar.title("🔍 AI Job Assistant")
page = st.sidebar.radio("Navigation", ["🏠 Home", "📂 Upload Resume", "💼 Job Matches", "📌 Applied Jobs"])

# ✅ Home Page
if page == "🏠 Home":
    st.title("🚀 Welcome to AI Job Assistant")
    st.markdown("Upload your resume, find the best job matches, and apply automatically!")
    st.image("https://source.unsplash.com/800x400/?technology,work", use_column_width=True)

# ✅ Resume Upload Page
elif page == "📂 Upload Resume":
    st.title("📂 Upload Your Resume")
    
    if "resume_text" not in st.session_state:
        st.session_state["resume_text"] = None

    uploaded_file = st.file_uploader("Upload a PDF resume", type=["pdf"])

    if uploaded_file:
        st.session_state["resume_text"] = uploaded_file.read().decode("utf-8")  # Convert to text
        st.success("✅ Resume uploaded successfully!")

# ✅ Job Matching Page
elif page == "💼 Job Matches":
    st.title("🔍 Find the Best Job Matches")

    if "resume_text" not in st.session_state or not st.session_state["resume_text"]:
        st.warning("⚠️ Please upload your resume first.")
    else:
        # ✅ Scrape Jobs
        st.write("📡 Fetching job listings...")
        try:
            jobs = scrape_google_jobs()
        except Exception as e:
            st.error(f"❌ Failed to scrape jobs: {e}")
            jobs = []

        # ✅ Match Jobs with Resume
        matched_jobs = []
        for job in jobs:
            try:
                score = match_job(st.session_state["resume_text"], job["title"])
                missing_skills = suggest_resume_improvements(st.session_state["resume_text"], job["title"])
                matched_jobs.append({"Title": job["title"], "Company": job["company"], "Match Score": score, "Missing Skills": ", ".join(missing_skills), "Apply Link": job["link"]})
            except Exception as e:
                st.error(f"❌ Error processing job: {e}")

        # ✅ Convert to DataFrame & Display
        if matched_jobs:
            df = pd.DataFrame(matched_jobs).sort_values(by="Match Score", ascending=False)
            st.dataframe(df.style.highlight_max(axis=0))

            # ✅ Allow Users to Apply
            st.subheader("✅ Auto-Apply to Top Match")
            best_match = df.iloc[0]  # Select top job
            st.markdown(f"**Best Match:** {best_match['Title']} at {best_match['Company']}")

            email = st.text_input("Enter LinkedIn Email")
            password = st.text_input("Enter LinkedIn Password", type="password")
            resume_file = st.text_input("Resume Path (e.g., /path/to/resume.pdf)")

            if st.button("📩 Auto-Apply"):
                try:
                    autofill_linkedin(email, password, resume_file)
                    insert_application(best_match["Title"], best_match["Company"])  # Store in database
                    st.success(f"✅ Application started for {best_match['Title']} at {best_match['Company']}!")
                except Exception as e:
                    st.error(f"❌ Auto-apply failed: {e}")
        else:
            st.info("No matching jobs found.")

# ✅ Applied Jobs Page
elif page == "📌 Applied Jobs":
    st.title("📌 Your Applied Jobs")

    try:
        applied_jobs = get_applications()
        if applied_jobs:
            df = pd.DataFrame(applied_jobs, columns=["ID", "Title", "Company", "Applied On", "Status"])
            st.dataframe(df.style.highlight_max(axis=0))
        else:
            st.info("No applications yet.")
    except Exception as e:
        st.error(f"❌ Error retrieving applications: {e}")
