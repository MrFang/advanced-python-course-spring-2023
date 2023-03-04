FROM python:3.10.10-slim-bullseye
WORKDIR /app
RUN apt update && \
    apt install -y texlive-latex-base && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt ./
RUN python -m pip install \
    -i https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.python.org/simple/ \
    --no-cache \
    -r requirements.txt
COPY entrypoint.sh ./
# COPY src ./src
