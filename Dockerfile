FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY my_ai_nvidia.py .

CMD ["python", "my_ai_nvidia.py"]
