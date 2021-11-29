FROM python:3.9-slim

ENV APP_HOME /app

WORKDIR $APP_HOME

RUN apt-get update \
    && apt-get install -y gcc g++ openssl libxml2-dev libxslt-dev musl-dev libxslt1-dev libffi-dev zlib1g-dev libssl-dev \
    && apt-get install -y build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 shared-mime-info
# WEASYPRINT dependancies
# sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

COPY . .

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
RUN pip install -vvv uvloop


RUN find /usr/local/lib/python3.9 -name '*.c' -delete \
    && find /usr/local/lib/python3.9 -name '*.pxd' -delete \
    && find /usr/local/lib/python3.9 -name '*.pyd' -delete \
    && find /usr/local/lib/python3.9 -name '__pycache__' | xargs rm -r

CMD gunicorn -c gunicorn_config.py backend.main:app