FROM python:3.8.0-slim as builder

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get upgrade -y

RUN apt-get -y --no-install-recommends install netcat build-essential cargo libpq-dev

RUN python -m pip install --upgrade pip setuptools \
    && pip install wheel \
    && pip install -r requirements.txt

COPY . /app/

COPY /entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

EXPOSE 5000

CMD [ "/entrypoint.sh" ]