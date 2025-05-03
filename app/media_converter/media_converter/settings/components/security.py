import os

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# Preventing MIME sniffing and XSS
SECURE_CONTENT_TYPE_NOSNIFF = True  # SecurityMiddleware
SECURE_BROWSER_XSS_FILTER   = True  # SecurityMiddleware

# Safe cookies
SESSION_COOKIE_HTTPONLY = True      # SessionMiddleware
SESSION_COOKIE_SAMESITE = 'Lax'     # SessionMiddleware

# Clickjacking protection
X_FRAME_OPTIONS = 'SAMEORIGIN'      # SecurityMiddleware

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
