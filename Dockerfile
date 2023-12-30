FROM python:3.8-alpine3.18 AS builder

WORKDIR /app

RUN apk update && apk add build-base zlib-dev && \
    pip3 install pyinstaller==6.3.0

COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt

COPY ./ ./

RUN pyinstaller main.py -y -F -n fc

FROM python:3.8-alpine3.18

ENV FLASHCARD_BASE_URL http://localhost:5000/api/v1

COPY --from=builder /app/dist/fc /bin/fc

ENTRYPOINT ["fc"]