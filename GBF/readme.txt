
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys
#
# assuming your django settings file is at '/home/o6u2h4n/mysite/mysite/settings.py'
## and your manage.py is is at '/home/o6u2h4n/mysite/manage.py'
path = '/home/o6u2h4n/GBF-MAIN'
if path not in sys.path:
    sys.path.append(path)
#
os.environ['DJANGO_SETTINGS_MODULE'] = 'GBF.settings'
#
 #   then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#import os

django deployment için lazım.