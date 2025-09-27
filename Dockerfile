FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY scripts/ ./scripts/

CMD ["python", "scripts/ingesta1.py"]
