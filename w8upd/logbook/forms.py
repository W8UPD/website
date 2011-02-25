from django.forms import ModelForm
from logbook.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('operator',) # Will be added in the view.
