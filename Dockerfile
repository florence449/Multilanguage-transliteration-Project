FROM ubuntu:latest
LABEL authors="user"

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    espeak-ng \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt --break-system-packages

COPY . .

EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
