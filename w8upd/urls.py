from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic import list_detail
from logbook.models import *

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'testapp.views.testview'),
    (r'^admin/', include(admin.site.urls)),
    (r'^template/', 'testapp.views.testview'),
    (r'^p/(.*)/', 'pages.views.viewpage'),
    (r'^portal/', 'pages.views.memberportal'),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    (r'^links/$', 'links.views.all_links'),
    (r'^contacts/$', list_detail.object_list, {"queryset" : Contact.objects.all()}),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
