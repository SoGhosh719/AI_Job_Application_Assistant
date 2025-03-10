from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ✅ Configure Selenium WebDriver (Headless Mode Recommended)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in background
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

# ✅ Auto-Fill Job Application (Example: LinkedIn Easy Apply)
def autofill_linkedin(email, password, resume_path):
    """
    Logs into LinkedIn and fills an Easy Apply job application.
    """
    driver.get("https://www.linkedin.com/login")
    
    # Enter Email
    email_field = driver.find_element(By.ID, "username")
    email_field.send_keys(email)
    
    # Enter Password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    time.sleep(2)  # Wait for login

    # Navigate to Jobs Page
    driver.get("https://www.linkedin.com/jobs/")
    time.sleep(3)

    # Find and Click "Easy Apply" Button
    easy_apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
    easy_apply_button.click()

    # Upload Resume
    upload_button = driver.find_element(By.CLASS_NAME, "jobs-document-upload__button")
    upload_button.send_keys(resume_path)

    # Submit Application
    submit_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
    submit_button.click()

    print("✅ Job Application Submitted!")

# ✅ Example Usage
if __name__ == "__main__":
    user_email = "your_email@example.com"
    user_password = "your_password"
    resume_file = "/path/to/resume.pdf"

    autofill_linkedin(user_email, user_password, resume_file)

    driver.quit()
