FROM python:3.12.3-slim AS builder
WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /code/wheels -r requirements.txt


FROM builder AS develop
COPY --from=builder /code/wheels /wheels
COPY --from=builder /code/requirements.txt .
RUN pip install --no-cache /wheels/*
COPY mysite/ .
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD [ "sh", "/entrypoint.sh" ]

# final stage
#FROM python:3.12.2-slim
#WORKDIR /app
#COPY --from=builder /app/wheels /wheels
#COPY --from=builder /app/requirements.txt .
#RUN pip install --no-cache /wheels/*


#FROM builder AS prod
#RUN poetry install --without dev
#ARG GROUP
#ARG USER
#RUN groupadd ${GROUP} \
 #&& useradd -m -g ${GROUP} ${USER} \
 #&& mv /code /home/${USER}/code \
 #&& chown ${USER}:${GROUP} -R /home/${USER}/code \
 #&& mv /entrypoint.sh /home/${USER}/entrypoint.sh
#WORKDIR /home/${USER}/code
#USER ${USER}
#ENTRYPOINT [ "sh", "/home/app/entrypoint.sh" ]