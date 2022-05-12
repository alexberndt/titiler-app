# STAC API

The STAC API for Overstory's internal satellite imagery data.

## Overview

STAC is a specification which unifies the way in which spatio-temporal data can be indexed and queried.
The official STAC spec is available [here](https://stacspec.org/).

This repository consists of a STAC API built using [FastAPI](https://fastapi.tiangolo.com/) and using the [stac-fastapi](https://github.com/stac-utils/stac-fastapi) package.

## Get Started

```bash
git clone git@github.com:20treeAI/stac-api.git
cd stac-api
```

### Locally with Docker

To host this API locally, use docker compose to build the `stac-api` service

```bash
docker-compose up --build stac-api
```

The API will now be available on [localhost:8082](http://localhost:8082/).

### Include Demo Data with Docker

Some demo data is available in `test/data/demo/`, which can be ingested by running

```bash
docker-compose up --build
```

which will also run the `load-demo-data` service in the `docker-compose.yml` file.

### Dev Environment Setup

To develop this app locally, you will need to have [poetry installed](https://python-poetry.org/docs/). Install the package locally and enable pre-commit hooks as follows

```bash
poetry install
poetry run pre-commit install
```

To test the API locally, you will need the following database specification available on port `5439`:

- Postgres `13`
- [Postgis](https://postgis.net/2020/12/18/postgis-3.1.0/) `3.1`
- [PGstac schema and functions](https://github.com/stac-utils/pgstac) `0.4.3`

This database service can be run using docker by running

```bash
docker-compose up database-postgis
```

Once running, the app uses alembic to run a migration containing pgstac on the database.

Source and export the environment variables form `.env.local` within a poetry shell, and run the app.

```bash
poetry shell
export $(grep -v '^#' .env.local | xargs)
./scripts/startup.sh
```

## Enabled Extensions

Currently, the STAC has the following extensions enabled:

1. TransactionExtension
2. QueryExtension
3. TokenPaginationExtension
4. ContextExtension

Extensions are actively developed, and available extensions and their status (e.g. scope, maturity) are available [here](https://stac-extensions.github.io/).
