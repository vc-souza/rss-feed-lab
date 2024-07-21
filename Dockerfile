ARG BASE_IMAGE=python:3.12-slim

FROM ${BASE_IMAGE} AS builder

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY . .

RUN pip install .

FROM ${BASE_IMAGE} AS final

COPY --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

CMD ["python"]
