import os


environment = os.environ.get('DJANGO_ENVIRONMENT', 'development')

print(environment)

if environment == 'production':
    from .production import *
elif environment == 'staging':
    from .staging import *
elif environment == 'testing':
    from .testing import *
else:
    from .development import *
