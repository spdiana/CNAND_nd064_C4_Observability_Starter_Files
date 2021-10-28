# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.7-slim

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN apt-get update && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

ENV PROMETHEUS_MULTIPROC_DIR /tmp
ENV prometheus_multiproc_dir /tmp

# CMD ["gunicorn", "--access-logfile", "-", "--error-logfile", "-c", "config.py", "-w", "4", "-b", "0.0.0.0:5001", "app:app"]
CMD gunicorn -c config.py -w 4 -b 0.0.0.0:5001 app:app
# CMD flask run --host=0.0.0.0 --port=5001 # correct syntax
