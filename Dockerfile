# Dockerfile, Image, Container
# The dockerfile is the blueprint for building images
# The image is the template for running containers
# The container is the actual process running the project
FROM python:3.8

ADD text_similarity.py .
ADD flask_api_file.py .

RUN pip install flask

CMD ["python", "./flask_api_file"]