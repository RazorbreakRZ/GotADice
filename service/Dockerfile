FROM python:3-alpine

WORKDIR /application

COPY requirements.txt /application/
RUN pip install -r requirements.txt --no-cache-dir

COPY app.py .
COPY static .
COPY templates .

EXPOSE 5000

ENTRYPOINT [ "flask", "run", "--host", "0.0.0.0", "--port", "5000" ]