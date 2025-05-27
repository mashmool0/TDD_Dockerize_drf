import os

# تشخیص محیط از متغیر محیطی
ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT', 'development')

if ENVIRONMENT == 'production':
    from .production import *
elif ENVIRONMENT == 'development':
    from .development import *
else:
    from .development import *  # default
