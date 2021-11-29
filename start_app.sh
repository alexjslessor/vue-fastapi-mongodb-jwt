#!/bin/bash


# user credentials
export USERNAME_TEST=<test user creds>
export PASSWORD_TEST=<test user creds>

#email provider api keys
export MAIL_USERNAME=<mailjet or sendgripe api keys>
export MAIL_PASSWORD=<mailjet or sendgripe api keys>

# Stripe api keys
export STRIPE_PUBLIC_ALEXJSLESSOR=<stripe key>
export STRIPE_SECRET_ALEXJSLESSOR=<stripe key>

# encryption hash
export SECRET=<sha256 hash here>

# mongodb atlas uri
export DATABASE_URL=""


uvicorn backend.main:app --port 5000 --reload