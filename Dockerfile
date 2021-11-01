FROM python:3.8.12-slim-buster

WORKDIR /app

RUN pip install 'pipenv>=2021.5.28,<2022.0.0'

COPY Pipfile Pipfile.lock ./

RUN pipenv install

COPY app ./app

ENTRYPOINT ["pipenv", "run", "start"]
