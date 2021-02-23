# Dockerfile, Image, Container
# The dockerfile is the blueprint for building images
# The image is the template for running containers
# The container is the actual process running the project
FROM python:3.8

MAINTAINER Grant Culp "culpgrant21@gmail.com"

COPY ./App/flask_api_file.py /App/flask_api_file.py
COPY ./App/text_similarity.py /App/text_similarity.py

RUN pip install flask

CMD ["python", "./App/flask_api_file.py", "./App/text_similarity.py"]