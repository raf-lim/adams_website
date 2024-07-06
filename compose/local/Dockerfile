FROM python:3.12.4-slim AS builder
WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc
COPY compose/local/requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /code/wheels -r requirements.txt


FROM builder AS develop
COPY --from=builder /code/wheels /wheels
COPY --from=builder /code/requirements.txt .
RUN pip install --no-cache /wheels/*
COPY mysite/ .
COPY compose/local/entrypoint.sh /.
RUN chmod +x /entrypoint.sh
CMD [ "sh", "/entrypoint.sh" ]
