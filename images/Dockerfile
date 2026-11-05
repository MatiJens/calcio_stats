FROM python:3.12-slim AS build
WORKDIR /app

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.12-slim AS final
WORKDIR /app

RUN groupadd --gid 1001 app && \
    useradd --uid 1001 --gid app --no-create-home --shell /usr/sbin/nologin app

COPY --chown=app:app app ./app
COPY --chown=app:app --from=build /install /usr/local

USER app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
