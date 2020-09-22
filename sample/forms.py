from django import forms
from .models import Items
from django.core.exceptions import ValidationError 
class SubmitForm(forms.ModelForm):

    class Meta:
        model = Items
        fields = ('name', 'description')
    
    def clean(self):
        super(SubmitForm, self).clean() 
        namee = self.cleaned_data.get('name')

        if Items.objects.filter(name__iexact=namee).exists(): 
            self._errors['name'] = self.error_class(['Nama Item sudah terdaftar']) 
        return self.cleaned_data
