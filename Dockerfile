FROM python:latest
WORKDIR /app
COPY requirements.txt .
EXPOSE 5001
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "index.py" ]
