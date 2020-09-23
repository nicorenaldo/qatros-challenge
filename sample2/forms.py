from django import forms
from .models import Bus, Schedule, Station
from django.core.exceptions import ValidationError 
from django.contrib.admin import widgets
class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ('name', 'description','image')
    
    def clean(self):
        super(BusForm, self).clean() 
        namee = self.cleaned_data.get('name')
        if Bus.objects.filter(name__iexact=namee).exists(): 
            self._errors['name'] = self.error_class(['Nama Item sudah terdaftar']) 
        return self.cleaned_data

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('bus', 'origin', 'destination', 'time_depart', 'time_arrival', 'day')
        widgets = {
            'time_arrival':forms.TimeInput(attrs={'type': 'time'}),
            'time_depart': forms.TimeInput(attrs={'type': 'time'}),
        }
    
    def clean(self):
        super(ScheduleForm, self).clean() 
        time_depart2 = self.cleaned_data.get('time_depart')
        time_arrival2 = self.cleaned_data.get('time_arrival')
        busz = self.cleaned_data.get('bus')
        dayz = self.cleaned_data.get('day')

        overlapping_start = Schedule.objects.filter(time_depart__gte=time_depart2, time_depart__lte=time_arrival2,day=dayz,bus=busz).count()
        overlapping_end = Schedule.objects.filter(time_arrival__gte=time_depart2, time_arrival__lte=time_arrival2,day=dayz,bus=busz).count()

        overlapping = overlapping_start > 0 or overlapping_end > 0
        if overlapping:
            self._errors['time_depart'] = self.error_class(['Time overlaps'])
        else:
            return self.cleaned_data
    

class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ('name',)
    
    def clean(self):
        super(StationForm, self).clean() 
        namee = self.cleaned_data.get('name')
        if Station.objects.filter(name__iexact=namee).exists(): 
            self._errors['name'] = self.error_class(['Nama Item sudah terdaftar']) 
        return self.cleaned_data
