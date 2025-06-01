FROM python:3.13.3-slim

COPY --from=ghcr.io/astral-sh/uv:0.7.9 /uv /uvx /bin/

WORKDIR /app

COPY . .

ENV UV_PROJECT_ENVIRONMENT=.venv

RUN uv sync --locked

ENV PATH="/app/.venv/bin:$PATH"

CMD ["uv", "run", "main.py"]