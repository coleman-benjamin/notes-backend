FROM python

WORKDIR /app

ENTRYPOINT []

RUN apt update && pip install poetry

COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false && poetry install

COPY . /app
