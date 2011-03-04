from logbook.models import *

def recent_contacts(request):
    return {'contacts': Contact.objects.all().order_by('-id')[:5]}
