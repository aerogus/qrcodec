FROM python:3.9.6-slim-buster

RUN apt-get update && apt-get install -y \
  libzbar0 \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY /app .

CMD ["python3", "server.py"]
