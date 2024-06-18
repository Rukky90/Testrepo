FROM python:3.12
WORKDIR /app
COPY . /app
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]