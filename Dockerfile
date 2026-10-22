FROM python:3.13.16-slim

WORKDIR /app
COPY ./src /app
RUN mkdir -p /var/www/html/list
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
CMD ["fastapi", "run", "main.py", "--port", "80"]
