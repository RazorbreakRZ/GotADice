FROM python:3.10.12-alpine

WORKDIR /application

COPY requirements.txt /application/
RUN pip install -r requirements.txt --no-cache-dir

COPY app.py /application/

EXPOSE 5000

ENTRYPOINT [ "flask", "run", "--host", "0.0.0.0", "--port", "5000" ]