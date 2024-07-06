FROM python:3.12.4-slim AS builder
WORKDIR /home/app/code
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc
COPY compose/production/requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /home/app/code/wheels -r requirements.txt

FROM builder AS production
COPY --from=builder /home/app/code/wheels /wheels
COPY --from=builder /home/app/code/requirements.txt .
RUN pip install --no-cache /wheels/*
RUN groupadd app \
 && useradd -m -g app app \
 && chown app:app -R /home/app/code
COPY mysite/ .
COPY compose/production/entrypoint.sh /
RUN chmod +x /entrypoint.sh
USER app
CMD [ "sh", "/entrypoint.sh" ]
