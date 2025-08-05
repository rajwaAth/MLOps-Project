FROM python:3.10-slim-buster

# install awscli (optional)
# RUN apt update -y && apt install -y awscli

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]