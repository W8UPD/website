from django.conf.urls.defaults import *
urlpatterns = patterns('members.views',
    (r'^$', 'memberprofile'),
    (r'^edit/$', 'editprofile'),
)