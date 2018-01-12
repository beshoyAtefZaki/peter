from django import forms

from .models import item



class Itemform(forms.ModelForm):
     class Meta:
         model = item
         fields =['fi']
