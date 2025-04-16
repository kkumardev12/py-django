import os

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Enable gzip and cache-busting for static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this at the top
    'django.middleware.security.SecurityMiddleware',
    ...
]