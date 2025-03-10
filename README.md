---

# **AI Job Application Assistant 🚀**
**An AI-powered assistant that helps job seekers find, match, and apply for jobs efficiently using NLP, OCR, and browser automation.**

---

## **🌟 Key Features**
✅ **Extract Job Descriptions** – Supports **OCR (Tesseract) & HTML Scraping (BeautifulSoup, Selenium)**  
✅ **AI-Powered Matching** – Uses **semantic search (spaCy, Sentence Transformers)** to match jobs with resumes  
✅ **Smart Resume Customization** – Suggests **resume improvements** tailored to each job  
✅ **Auto-Fill Job Applications** – Reduces application time by **pre-filling repetitive form fields**  
✅ **Chrome Extension** – Provides **real-time job recommendations** and resume suggestions  

---

## **📌 How It Works**
1️⃣ **Extracts job descriptions** from **LinkedIn, Handshake, company career pages** using **OCR or HTML scraping**  
2️⃣ **Matches job descriptions** with the candidate’s **skills, experience, and keywords**  
3️⃣ **Suggests resume improvements** based on **missing keywords & ATS optimization**  
4️⃣ **Auto-fills job application forms** to reduce manual input  
5️⃣ **Tracks applied jobs** in a **personal job application database**  

---

## **🛠 Tech Stack**
- **Backend:** Python, FastAPI, NLP (`spaCy`, `sentence-transformers`, `transformers`)  
- **Frontend:** Streamlit (for Web App), JavaScript (for Chrome Extension)  
- **Automation:** Selenium, Requests, BeautifulSoup, Tesseract OCR  
- **Data Storage:** SQLite (for tracking applications)  
- **Deployment:** Docker, Railway.app  

---

## **🏗️ Project Structure**
```
AI_Job_Application_Assistant/
│── backend/                 # Backend for AI processing
│   ├── job_scraper.py        # Extracts job postings
│   ├── resume_matcher.py     # Matches resume with jobs
│   ├── form_autofill.py      # Auto-fills job applications
│   ├── database.py           # Tracks applied jobs
│   ├── models/               # Local AI models
│   └── requirements.txt      # Dependencies
│
│── extension/                # Chrome Extension for real-time job suggestions
│   ├── content.js            # Extracts job descriptions
│   ├── popup.html            # Displays resume suggestions
│   ├── popup.js              # Handles extension UI logic
│   ├── manifest.json         # Chrome extension config
│   ├── styles.css            # UI styling
│   └── icon.png              # Extension Icon
│
│── webapp/                   # Streamlit UI for job applications
│   ├── app.py                # Streamlit web interface
│   ├── templates/            # HTML templates
│   ├── static/               # CSS/JS assets
│   ├── config.py             # API keys & settings
│   └── Dockerfile            # Deployment setup
│
│── README.md                 # Documentation
│── LICENSE                   # Open-source license
│── .gitignore                # Ignore unnecessary files
```

---

## **🚀 How to Set Up & Run Locally**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/SoGhosh719/AI_Job_Application_Assistant.git
cd AI_Job_Application_Assistant
```

### **2️⃣ Install Dependencies**
```bash
pip install -r backend/requirements.txt
python -m spacy download en_core_web_md
```

### **3️⃣ Run the Web App**
```bash
streamlit run webapp/app.py
```

### **4️⃣ Build & Install Chrome Extension**
1. **Go to `chrome://extensions/`**  
2. **Enable Developer Mode**  
3. **Click "Load Unpacked" → Select `extension/` Folder**  
4. **Start Browsing Jobs and Get Resume Suggestions!** 🚀  

---

## **📌 Features in Detail**
### **🔹 1️⃣ Job Description Extraction (OCR + HTML Scraping)**
- **Extracts job descriptions** from **LinkedIn, Handshake, or company career pages**.
- **Uses OCR** if HTML scraping is blocked.

```python
import pytesseract
from PIL import Image

# ✅ Extract Text from Screenshot
image_path = "job_posting_screenshot.png"
image = Image.open(image_path)
extracted_text = pytesseract.image_to_string(image)
print("Extracted Job Description:", extracted_text)
```

---

### **🔹 2️⃣ AI-Powered Resume Matching**
- Uses **Sentence Transformers** to **compare job descriptions with resumes**.

```python
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

# ✅ Match Resume & Job Description
def match_job(resume_text, job_desc):
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_desc, convert_to_tensor=True)
    similarity_score = util.pytorch_cos_sim(resume_embedding, job_embedding)
    return similarity_score.item()
```

---

### **🔹 3️⃣ AI-Driven Resume Customization**
- Suggests **resume edits instead of auto-editing**.

```python
import spacy

nlp = spacy.load("en_core_web_md")

def suggest_resume_improvements(resume_text, job_desc):
    job_doc = nlp(job_desc.lower())
    job_keywords = {token.lemma_ for token in job_doc if token.pos_ in ['NOUN', 'PROPN', 'VERB', 'ADJ'] and not token.is_stop}

    missing_skills = job_keywords - set(resume_text.lower().split())
    return f"Consider adding these missing skills: {', '.join(missing_skills)}"
```

---

### **🔹 4️⃣ Auto-Fill Job Applications**
- **Fills repetitive fields** like name, email, LinkedIn, resume.

```javascript
// ✅ Auto-fill LinkedIn Job Application (Example)
document.querySelector("input[name='full_name']").value = "John Doe";
document.querySelector("input[name='email']").value = "john@example.com";
document.querySelector("textarea[name='resume']").value = "Customized Resume Here";
```

---

### **🔹 5️⃣ Chrome Extension for Job Matching**
- Extracts **job descriptions** when users visit job pages.  
- Displays **real-time AI resume suggestions**.

```javascript
// ✅ Extract Job Description from Page
let jobDescription = document.querySelector(".job-description").innerText;
chrome.runtime.sendMessage({ jobText: jobDescription });
```

---

## **🤝 Contributing**
Want to improve the AI job assistant? Contributions are welcome!  

1. **Fork the repo**  
2. **Create a branch** (`git checkout -b feature-branch`)  
3. **Commit your changes** (`git commit -m "Added feature XYZ"`)  
4. **Push to GitHub** (`git push origin feature-branch`)  
5. **Open a Pull Request** 🚀  

---

## **📜 License**
This project is licensed under the **MIT License**.  

---

## **📞 Contact & Support**
**👤 Author:** [SoGhosh719](https://github.com/SoGhosh719)  
**📧 Email:** `soghosh@clarku.edu`  
**🌍 Website:** [Portfolio](https://soghosh719.github.io/)  

---

## **🔥 Final Outcome**
✅ **Comprehensive README.md with clear setup instructions**  
✅ **Better structure and installation guide**  
✅ **Encourages contributors to join**  
✅ **Clear step-by-step setup instructions**  
