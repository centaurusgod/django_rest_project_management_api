# Base Image (Just Python)
FROM python:3.13.0a2-slim-bookworm as python-base
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app

# dependency installation
FROM python-base as dependencies

RUN apt-get update \
    && apt-get install --no-install-recommends -y curl

# Install uv & create a symbolic link
RUN curl --proto '=https' --tlsv1.2 -LsSf https://github.com/astral-sh/uv/releases/download/0.5.15/uv-installer.sh | sh && \
    ln -s /root/.local/bin/uv /usr/local/bin/uv

COPY uv.lock pyproject.toml ./
RUN uv sync --frozen  

# another stage
FROM python-base as development

WORKDIR /app

# only copy .venv from the dependencies stage (nothing else)
COPY --from=dependencies /app/.venv /app/.venv

# copy all source code
COPY . .

RUN chmod +x /app/entrypoint.sh

ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT ["/app/entrypoint.sh"]
