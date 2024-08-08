FROM python:3.11.9 as dependencies

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Основной образ
FROM python:3.11.9 as build

RUN mkdir /app
COPY --from=dependencies /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=dependencies /usr/local/bin /usr/local/bin

FROM scratch

WORKDIR /app
COPY . .
COPY --from=build / /
