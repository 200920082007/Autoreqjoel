FROM python:3.10-alpine
WORKDIR /TigerShroffv3
COPY requirements.txt .
RUN apk update && \
    apk upgrade && \
    apk add --no-cache git && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3", "bot.py"]
