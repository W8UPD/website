from django import forms
from django.forms import ModelForm
from members.models import *

class UserProfileForm(ModelForm):
    # first_name = forms.CharField(max_length=255)
    # last_name = forms.CharField(max_length=255)

    # def __init__(self, *args, **kw):
    #     super(UserProfileForm, self).__init__(*args, **kw)
    #     self.fields['first_name'].initial = self.instance.user.first_name
    #     self.fields['last_name'].initial = self.instance.user.last_name
    #     self.fields.keyOrder = ['first_name', 'last_name']
    # 
    # def save(self, *args, **kw):
    #     super(UserProfileForm, self).save(*args, **kw)
    #     self.instance.user.first_name = self.cleaned_data.get('first_name')
    #     self.instance.user.last_name = self.cleaned_data.get('last_name')
    #     self.instance.user.save()

    class Meta:
        model = UserProfile
        exclude = ('user',)