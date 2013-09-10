import os
import sys
sys.path.append('/opt/wwwroot')
sys.path.append('/opt/wwwroot/hello')
path = '/opt/wwwroot'

if path not in sys.path:
    sys.path.insert(0, '/opt/wwwroot')

os.environ['DJANGO_SETTINGS_MODULE'] = 'hello.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
