FROM python:3.8.6-buster

RUN pip install pipenv

RUN mkdir ./app

WORKDIR /app

COPY . .

RUN pipenv install --system --deploy --ignore-pipfile

CMD ["python", "app.py"]

