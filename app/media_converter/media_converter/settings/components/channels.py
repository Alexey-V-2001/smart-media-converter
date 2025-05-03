from .redis import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD

# Django Channels settings (for WebSockets)
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [{"address": (REDIS_HOST, REDIS_PORT), "password": REDIS_PASSWORD}],
        },
    },
}
