FROM python:3.13-slim

RUN apt update && apt install -y \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_bot.py", "--server.port=8501", "--server.address=0.0.0.0"]