FROM python:3.9.7-slim as base

WORKDIR /app

COPY src/ /app/
COPY pyproject.toml poetry.lock /app/

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Copy entrypoint script
COPY ./scripts/startup.sh /app/startup.sh
RUN chmod +x startup.sh

CMD exec ./startup.sh
