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
options.add_argument("--window-size=1920,1080")  # Ensures LinkedIn loads properly
options.add_argument("--disable-blink-features=AutomationControlled")  # Prevents detection
driver = webdriver.Chrome(options=options)

# ✅ LinkedIn Auto-Apply Function
def autofill_linkedin(email, password, resume_path):
    """
    Logs into LinkedIn and applies for jobs using Easy Apply.
    """
    driver.get("https://www.linkedin.com/login")

    try:
        # ✅ Enter Email
        email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        email_field.send_keys(email)

        # ✅ Enter Password
        password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        time.sleep(3)  # Wait for login

        # ✅ Verify Successful Login
        if "checkpoint" in driver.current_url:
            print("❌ Login failed! Check credentials or captcha requirement.")
            driver.quit()
            return

        # ✅ Navigate to Jobs Page
        driver.get("https://www.linkedin.com/jobs/search/")
        time.sleep(3)

        # ✅ Find Easy Apply Jobs
        job_posts = driver.find_elements(By.XPATH, "//div[contains(@class, 'job-card-container')]")

        if not job_posts:
            print("❌ No Easy Apply jobs found.")
            driver.quit()
            return

        applied_jobs = 0

        for job in job_posts:
            try:
                job.click()
                time.sleep(2)

                # ✅ Click Easy Apply Button
                easy_apply_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'jobs-apply-button')]"))
                )
                easy_apply_button.click()
                time.sleep(2)

                # ✅ Upload Resume
                try:
                    upload_button = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
                    )
                    upload_button.send_keys(resume_path)
                except:
                    print("⚠️ Resume upload not required.")

                # ✅ Click Submit Button
                try:
                    submit_button = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit application')]"))
                    )
                    submit_button.click()
                    print("✅ Application Submitted!")
                    applied_jobs += 1
                except:
                    print("❌ Could not submit application.")

                time.sleep(2)  # Wait before next job
            except Exception as e:
                print(f"⚠️ Skipping job due to error: {str(e)}")

        print(f"✅ Successfully applied to {applied_jobs} jobs!")

    except Exception as e:
        print(f"❌ Error during LinkedIn Auto-Apply: {e}")

    driver.quit()

# ✅ Example Usage
if __name__ == "__main__":
    user_email = "your_email@example.com"
    user_password = "your_password"
    resume_file = "/path/to/resume.pdf"

    autofill_linkedin(user_email, user_password, resume_file)
