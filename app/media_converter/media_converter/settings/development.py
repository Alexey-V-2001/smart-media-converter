import os

from .components.base import *
from .components.security import *
from .components.database import *
from .components.cache import *
from .components.logging import *
from .components.templates import *
from .components.redis import *
from .components.channels import *

DEBUG = os.getenv("DJANGO_DEBUG")

# Disabling SSL in development mode
SECURE_SSL_REDIRECT             = False
SECURE_HSTS_SECONDS             = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_HSTS_PRELOAD             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
