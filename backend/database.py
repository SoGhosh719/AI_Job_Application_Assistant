import sqlite3

# ✅ Create Database Connection
def connect_db():
    return sqlite3.connect("backend/job_applications.db")

# ✅ Create Applications Table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_title TEXT,
        company TEXT,
        applied_on DATE DEFAULT CURRENT_DATE,
        status TEXT DEFAULT 'Applied'
    )
    """)
    
    conn.commit()
    conn.close()

# ✅ Insert a New Job Application
def insert_application(job_title, company, status="Applied"):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO applications (job_title, company, status) VALUES (?, ?, ?)", 
                   (job_title, company, status))
    
    conn.commit()
    conn.close()

# ✅ Retrieve All Applications
def get_applications():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM applications")
    jobs = cursor.fetchall()
    
    conn.close()
    return jobs

# ✅ Test Example
if __name__ == "__main__":
    create_table()
    
    # Add a test job
    insert_application("Data Scientist", "Google")
    
    # Fetch and display jobs
    jobs = get_applications()
    for job in jobs:
        print(job)
