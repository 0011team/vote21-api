import os
import sys
from django.core.wsgi import get_wsgi_application
from os.path import dirname, abspath

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.vote21.development")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
application = get_wsgi_application()
