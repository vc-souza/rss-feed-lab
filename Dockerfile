ARG BASE_IMAGE=python:3.12-slim
ARG WEB_PORT=9001

FROM ${BASE_IMAGE} AS builder

RUN apt-get update && \
    apt-get install -y build-essential

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY . .

RUN pip install .

FROM ${BASE_IMAGE} AS final

EXPOSE ${WEB_PORT}

COPY --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

CMD ["python", "-m", "rss_feed_lab"]
