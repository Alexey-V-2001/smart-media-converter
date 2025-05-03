# Using slim images reduces the size of the final image
FROM python:3.13.3-slim

# Disable Python output buffering so logs appear immediately in the console
ENV PYTHONUNBUFFERED 1
# Prevent Python from writing .pyc bytecode files to avoid cluttering the filesystem
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/app

# Installing system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ffmpeg \
    && rm -rf /var/lib/apt/lists/*
    # Clearing the apt cache reduces the final image size

CMD [ "./start.sh"]