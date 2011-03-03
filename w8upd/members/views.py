from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from logbook.forms import ContactForm

@login_required
def memberportal(request):
    if request.method == 'POST':
        print "foo"
    else:
        c = {}
        c['contactform'] = ContactForm()
        c['user'] = request.user
        return render_to_response('portal.html', c, context_instance=RequestContext(request))

