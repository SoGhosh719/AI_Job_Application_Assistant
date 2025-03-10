from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ✅ Configure Selenium WebDriver (Headless Mode Recommended)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in background
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

# ✅ Auto-Fill Job Application (LinkedIn Easy Apply)
def autofill_linkedin(email, password, resume_path):
    """
    Logs into LinkedIn and fills an Easy Apply job application.
    """
    driver.get("https://www.linkedin.com/login")
    
    # ✅ Enter Email
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(email)
    
    # ✅ Enter Password
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(Keys.RETURN)

    time.sleep(2)  # Wait for login

    # ✅ Navigate to Jobs Page
    driver.get("https://www.linkedin.com/jobs/")
    time.sleep(3)

    # ✅ Handle "Easy Apply" Button Not Found
    try:
        easy_apply_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "artdeco-button--primary"))  # Updated selector
        )
        easy_apply_button.click()
    except:
        print("❌ Could not find the Easy Apply button. Exiting.")
        driver.quit()
        exit()

    # ✅ Upload Resume
    upload_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jobs-document-upload__button"))
    )
    upload_button.send_keys(resume_path)

    # ✅ Submit Application
    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "artdeco-button--primary"))
    )
    submit_button.click()

    print("✅ Job Application Submitted!")
    driver.quit()

# ✅ Example Usage
if __name__ == "__main__":
    user_email = "your_email@example.com"
    user_password = "your_password"
    resume_file = "/path/to/resume.pdf"

    autofill_linkedin(user_email, user_password, resume_file)
