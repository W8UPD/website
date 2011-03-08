from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.template import RequestContext
from logbook.forms import ContactForm
from members.forms import UserProfileForm
from members.models import *

# Helper methods
def profile_object(user):
    profile, created = UserProfile.objects.get_or_create(user=user)
    return profile, created
    

@login_required
def memberprofile(request):
    if request.method == 'POST':
        print "foo"
    else:
        c = {}
        # c['contactform'] = ContactForm()
        c['user'] = request.user
        c['profile'] = request.user.get_profile()
        return render_to_response('profiles/view.html', c, context_instance=RequestContext(request))

@login_required
def editprofile(request):
    user = request.user
    profile, created = profile_object(user)
    if request.method == 'GET':
        c = {}
        c.update(csrf(request))
        c['profile'] = profile
        c['created'] = created
        c['profileform'] = UserProfileForm(instance=profile)
        return render_to_response('profiles/edit.html', c, context_instance=RequestContext(request))
    else:
        form = UserProfileForm(request.POST, instance=profile)
        mform = form.save(commit=False)
        mform.user = request.user # The user can only edit their own profile
        mform.save()
        form.save_m2m()
        return redirect('/profile/')