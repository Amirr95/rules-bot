FROM python:3.10.6-slim

WORKDIR /bot

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "-u", "main.py" ]

