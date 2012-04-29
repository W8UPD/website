#!/usr/bin/env python
import os
import sys
sys.path.append('/srv/w8upd.org/')
sys.path.append('/srv/w8upd.org/w8upd/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'w8upd.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
