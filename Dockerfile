FROM python:3.12.2-slim-bullseye as prod

# Installing poetry
RUN pip install poetry==1.8.2

# Configuring poetry
RUN poetry config virtualenvs.create false

# Copying requirements of a project
WORKDIR /app/src
COPY pyproject.toml poetry.lock ./

# Installing requirements
RUN poetry install --only main

CMD ["/usr/local/bin/python", "-m", "app"]