FROM python:3.12
WORKDIR /band_website
COPY requirements.txt .
RUN pip install -r requirements.txt
