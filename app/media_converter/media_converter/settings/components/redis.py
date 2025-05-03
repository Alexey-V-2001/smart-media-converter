import os

# Redis connection settings
REDIS_HOST      = os.getenv('REDIS_HOST')
REDIS_PORT      = int(os.getenv('REDIS_PORT'))
REDIS_DB        = int(os.getenv('REDIS_DB'))
REDIS_PASSWORD  = os.getenv('REDIS_PASSWORD')

# Redis connection string
REDIS_URL = f"redis://{':' + REDIS_PASSWORD + '@' if REDIS_PASSWORD else ''}{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

# Redis-related constants
FILE_TTL = 24 * 60 * 60  # TTL for files in seconds (24 hours)
REDIS_CONVERSION_PREFIX = 'media_converter:'  # Prefix for Redis keys related to conversion
