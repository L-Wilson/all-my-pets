FROM python:3.9-slim


WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade pip && \
  pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

EXPOSE 8000

# Run the application
CMD ["python", "src/main.py"]
