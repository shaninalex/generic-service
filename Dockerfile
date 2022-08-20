FROM python:3.10.5-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    apk add python3-dev

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x /usr/src/app/entrypoint.sh
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]