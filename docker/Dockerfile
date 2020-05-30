FROM alpine

RUN apk add --no-cache python3 make

COPY simple_http_server.py /app/

ENTRYPOINT ["python3", "/app/simple_http_server.py"]

