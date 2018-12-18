FROM python:3.6-alpine
ADD . /code
WORKDIR /code/
RUN apk add --no-cache postgresql-dev gcc python3 python3-dev musl-dev && pip3 install -r requirements.txt
CMD ["python3", "__init__.py"]