from django.shortcuts import render_to_response
from links.models import *

def all_links(request):
    links = Link.objects.all()
    return render_to_response('links.html', {'links': links})
