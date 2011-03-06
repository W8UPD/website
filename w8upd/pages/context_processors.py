import sys,os,django
from page.models import Page

def versioninfo(request):
    python = sys.version.split()[0]
    osversion = os.uname()
    djangoversion = "%s.%s.%s" % (django.VERSION[0], django.VERSION[1], django.VERSION[2])
    versions = "Django %s / Python %s / %s / %s %s %s" % \
        (djangoversion, python, osversion[1].split('.')[0], osversion[0], osversion[2], osversion[4])
    return {'versions': versions}
