FROM python:3.10-slim

# install python package
COPY pyproject.toml ./
RUN pip install poetry
# --no-root: デフォルトで src をインストールするので、回避する
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

# mount dir
RUN mkdir -p /opt/mnt
WORKDIR /opt/mnt

# expose port
EXPOSE 8888