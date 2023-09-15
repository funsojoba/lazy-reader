FROM python:3.8.0-slim as builder

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get upgrade -y

RUN python -m pip install --upgrade pip setuptools \
    && pip install wheel \
    && pip install -r requirements.txt

COPY . /app/

COPY /entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

EXPOSE 5001

CMD [ "/entrypoint.sh" ]