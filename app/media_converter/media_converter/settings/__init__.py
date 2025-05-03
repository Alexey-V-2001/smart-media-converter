import os

# Import settings depending on the environment
if os.getenv('DJANGO_ENVIRONMENT') == 'development':
    from .development import *
else:
    from .production import *

# Apply local settings if they exist
try:
    from .local import *
except ImportError:
    pass
