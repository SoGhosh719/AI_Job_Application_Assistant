from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ✅ Configure Selenium WebDriver
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
    try:
        email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        email_field.send_keys(email)
    except:
        print("❌ Could not find email field.")
        driver.quit()
        return

    # ✅ Enter Password
    try:
        password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
    except:
        print("❌ Could not find password field.")
        driver.quit()
        return

    time.sleep(3)  # Wait for login

    # ✅ Verify Successful Login
    if "checkpoint" in driver.current_url:
        print("❌ Login failed! Check credentials or captcha requirement.")
        driver.quit()
        return

    # ✅ Navigate to Jobs Page
    driver.get("https://www.linkedin.com/jobs/")
    time.sleep(3)

    # ✅ Handle "Easy Apply" Button Not Found
    try:
        easy_apply_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'jobs-apply-button')]"))
        )
        easy_apply_button.click()
    except:
        print("❌ Could not find the Easy Apply button. Exiting.")
        driver.quit()
        return

    # ✅ Upload Resume
    try:
        upload_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )
        upload_button.send_keys(resume_path)
    except:
        print("❌ Could not upload resume.")
        driver.quit()
        return

    # ✅ Submit Application
    try:
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit application')]"))
        )
        submit_button.click()
    except:
        print("❌ Could not find the submit button.")
        driver.quit()
        return

    print("✅ Job Application Submitted Successfully!")
    driver.quit()

# ✅ Example Usage
if __name__ == "__main__":
    user_email = "your_email@example.com"
    user_password = "your_password"
    resume_file = "/path/to/resume.pdf"

    autofill_linkedin(user_email, user_password, resume_file)
