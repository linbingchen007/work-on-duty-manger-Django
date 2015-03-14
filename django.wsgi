import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
path = '/var/www/mysite/'
if path not in sys.path:
    sys.path.append(path)
sys.path.append('/usr/local/lib/python2.7/dist-packages')
sys.path.append('/usr/local/lib/python2.7/dist-packages/django')
os.environ['DJANGO_SETTINGS_MODULE'] = 'registration.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
