import os

if os.environ.get('env') == 'PRODUCTION':
    from .production import *
else:
    from .local import *
