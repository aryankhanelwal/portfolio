from django import forms
from .models import contact_me


class insertdata(forms.ModelForm):
    class Meta():
        model = contact_me
        fields ='__all__'