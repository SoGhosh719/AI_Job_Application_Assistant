FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r backend/requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "webapp/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
