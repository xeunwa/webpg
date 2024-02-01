FROM python:3.11-slim AS app

WORKDIR /var/www/html
COPY requirements.txt . 
RUN pip3 install --no-cache-dir flask

COPY app.py .
COPY templates ./templates

EXPOSE 5000

COPY flag.txt .

CMD ["python3", "app.py"]