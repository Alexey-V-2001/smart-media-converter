TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',   # Template engine
        'DIRS': [],                                                     # Additional directories for searching templates
        'APP_DIRS': True,                                               # Searching for templates in application directories
        'OPTIONS': {
            'context_processors': [                                     # Context processors add variables to template contexts automatically
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]