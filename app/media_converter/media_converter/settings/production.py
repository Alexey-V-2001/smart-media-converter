from .components.base import *
from .components.security import *
from .components.database import *
from .components.cache import *
from .components.logging import *
from .components.templates import *
from .components.redis import *
from .components.channels import *

DEBUG = False

SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security
SECURE_HSTS_SECONDS = 365 * 24 * 60 * 60    # 1 year in seconds
SECURE_HSTS_INCLUDE_SUBDOMAINS = True       # Apply to all subdomains
SECURE_HSTS_PRELOAD = True                  # Allow inclusion in browser preload list

# Safe cookies
SESSION_COOKIE_SECURE   = True              # SessionMiddleware
CSRF_COOKIE_SECURE      = True              # CsrfViewMiddleware
