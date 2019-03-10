FROM python:3.6-alpine

RUN pip install --upgrade pip
RUN pip install tornado

RUN mkdir -p /workspace/python-web-service
WORKDIR /workspace/python-web-service
COPY . .

EXPOSE 8888

CMD ["python", "app.py"]