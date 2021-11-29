#!/bin/bash

pip install fastapi-users[mongodb] \
            fastapi-mail \
            pydantic[dotenv] \
            gunicorn[gthread] \
            uvicorn[standard] \
            python-multipart \
            stripe \
            pandas \
            orjson \
            motor \