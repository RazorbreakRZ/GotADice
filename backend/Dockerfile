FROM python:3-alpine

WORKDIR /application

COPY requirements.txt /application/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY app.py /application/

EXPOSE 5000

ENTRYPOINT [ "flask", "run", "--host", "0.0.0.0", "--port", "5000" ]