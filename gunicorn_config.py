"""gunicorn server configuration."""
from os import environ

# set these next
# --graceful-timeout 300000
# --keep-alive 300000
# https://docs.gunicorn.org/en/latest/settings.html#loglevel
# loglevel = 'error'
# https://docs.gunicorn.org/en/latest/settings.html#errorlog
# log_file = ''
# https://docs.gunicorn.org/en/latest/settings.html#capture-output
# capture_output = True
# https://pythonspeed.com/articles/gunicorn-in-docker/
# https://docs.gunicorn.org/en/latest/settings.html#workers
workers = 1
threads = 2
timeout = 300
# timeout is 300 by default

bind = f":{environ.get('PORT', '8080')}"

# https://docs.gunicorn.org/en/latest/faq.html#how-do-i-avoid-gunicorn-excessively-blocking-in-os-fchmod
# DEFAULT: None
worker_temp_dir = '/dev/shm'

# https://docs.gunicorn.org/en/latest/settings.html#worker-class
# DEFAULT: sync
worker_class = 'gthread'
worker_class = "uvicorn.workers.UvicornWorker"

