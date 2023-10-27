FROM python:3

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt

CMD ["python3", "./app.py"]
