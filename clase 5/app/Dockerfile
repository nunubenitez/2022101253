FROM python:3.9

WORKDIR /app

COPY requeriments.txt .

RUN pip install --no-cache-dir -r requeriments.txt

COPY . .

CMD ["python", "main.py"]