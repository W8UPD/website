from django.shortcuts import render_to_response, get_object_or_404
from pages.models import *
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

def viewpage(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render_to_response('page.html', { 'page': page })

@login_required
def memberportal(request):
    c = {}
    c['user'] = request.user
    return render_to_response('portal.html', c, context_instance=RequestContext(request))
