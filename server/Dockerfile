# FROM python:3.8-alpine

# WORKDIR /app

# COPY requirements.txt .
# # コンテナ内で必要なパッケージをインストール
# RUN apk add --no-cache build-base \
#  && pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt \
#  && apk del build-base

# COPY main.py .
# EXPOSE 8000
# # FastAPIを8000ポートで待機
# CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]





# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
FROM python:3.7-alpine
WORKDIR /app
# COPY ./requirements.txt ./
COPY ./Pipfile ./
COPY ./Pipfile.lock ./
RUN pip install pipenv
RUN pipenv install --system
# RUN pipenv install -r requirements.txt


# RUN apk add --no-cache build-base \
#  && pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt \
#  && apk del build-base
COPY ./ .
ENV HOST 0.0.0.0
EXPOSE 8000
# CMD ["uvicorn", "main:app", "--reload"]