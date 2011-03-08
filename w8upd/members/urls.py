from django.conf.urls.defaults import *
urlpatterns = patterns('members.views',
    ('^$', 'memberprofile'),
)