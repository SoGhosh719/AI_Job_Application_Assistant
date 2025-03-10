# ✅ Use Python 3.9 as the base image
FROM python:3.9

# ✅ Set the working directory
WORKDIR /app

# ✅ Copy project files into the container
COPY . .

# ✅ Upgrade pip and install required dependencies
RUN pip install --upgrade pip
RUN pip install -r backend/requirements.txt

# ✅ Expose Streamlit Port
EXPOSE 8501

# ✅ Run Streamlit app
CMD ["streamlit", "run", "webapp/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
