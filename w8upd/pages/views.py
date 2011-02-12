from django.shortcuts import render_to_response, get_object_or_404
from pages.models import *

def viewpage(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render_to_response('page.html', { 'page': page })

