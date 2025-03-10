import requests
from bs4 import BeautifulSoup

# ✅ Extract Jobs from Google Careers
def scrape_google_jobs():
    url = "https://careers.google.com/jobs/results/"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    
    for job_listing in soup.find_all("section", class_="gc-card"):
        title = job_listing.find("h2")
        company = "Google"
        link = job_listing.find("a")["href"] if job_listing.find("a") else "No Link"

        if title:
            jobs.append({
                "title": title.text.strip(),
                "company": company,
                "link": f"https://careers.google.com{link}"
            })
    
    return jobs

# ✅ Run Scraper & Display Results
if __name__ == "__main__":
    google_jobs = scrape_google_jobs()
    
    print("🔍 Extracted Google Jobs:")
    for job in google_jobs:
        print(f"{job['title']} - {job['company']} ({job['link']})")
