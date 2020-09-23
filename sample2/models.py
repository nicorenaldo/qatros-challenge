from django.db import models
from django.utils.crypto import get_random_string
import string

import datetime
DAY_CHOICES = [
    ('SU', 'Sunday'),
    ('MO', 'Monday'),
    ('TH', 'Thursday'),
    ('WE', 'Wednesday'),
    ('TU', 'Tuesday'),
    ('FR', 'Friday'),
    ('SA', 'Saturday'),
]
# Create your models here.
class Bus(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='bus/' , blank=True , null=True)
    code = models.SlugField(unique=True, blank=True , null=True)
    
    def save(self, *args , **kwargs):
        if not self.code :
            self.code = get_random_string(length=12, allowed_chars = string.ascii_lowercase)
        super(Bus , self).save(*args , **kwargs)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    bus = models.ForeignKey('Bus', on_delete=models.CASCADE, null=True)
    
    origin = models.ForeignKey('Station', on_delete=models.CASCADE, null=True, related_name='origin')
    destination = models.ForeignKey('Station', on_delete=models.CASCADE, null=True, related_name='destination')
    time_depart = models.TimeField(auto_now=False, auto_now_add=False)
    time_arrival = models.TimeField(auto_now=False, auto_now_add=False,)
    day = models.CharField(max_length=2,choices=DAY_CHOICES,default='SU')
    code = models.SlugField(unique=True, blank=True , null=True)
    
    def save(self, *args , **kwargs):
        if not self.code :
            self.code = get_random_string(length=12, allowed_chars = string.ascii_lowercase)
        super(Schedule , self).save(*args , **kwargs)

    def __str__(self):
        return self.bus.name
    
    @property
    def travel_time(self):
        date = datetime.date(1, 1, 1)
        datetime1 = datetime.datetime.combine(date, self.time_arrival)
        datetime2 = datetime.datetime.combine(date, self.time_depart)
        result = datetime1 - datetime2
        # result = time2-time1
        # result = datetime.timedelta(self.time_arrival , self.time_depart)
        return result

class Station(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name