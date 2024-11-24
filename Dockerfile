FROM python:3.12-slim

RUN apt-get update && apt-get install -y cron && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV OLLAMA_HOST="0.0.0.0"

CMD ["python", "regen_pdf.py"]