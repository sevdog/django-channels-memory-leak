FROM python:3.10-alpine
RUN apk add -U -q --no-cache \
        hiredis \
        g++ \
        musl-dev \
        libc-dev \
        cargo \
        git \
        linux-headers \
        # for orjson
        patchelf \
        cargo
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt