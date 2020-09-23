from django.db import models
from django.utils.crypto import get_random_string
import string
from django.urls import reverse
import datetime
DAY_CHOICES = [
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Thursday', 'Thursday'),
    ('Wednesday', 'Wednesday'),
    ('Tuesday', 'Tuesday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
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
    
    def get_absolute_url(self):
        return reverse('detail_bus', kwargs={'pk': self.pk})

class Schedule(models.Model):
    bus = models.ForeignKey('Bus', on_delete=models.CASCADE, null=True)
    
    origin = models.ForeignKey('Station', on_delete=models.CASCADE, null=True, related_name='origin')
    destination = models.ForeignKey('Station', on_delete=models.CASCADE, null=True, related_name='destination')
    time_depart = models.TimeField(auto_now=False, auto_now_add=False)
    time_arrival = models.TimeField(auto_now=False, auto_now_add=False,)
    day = models.CharField(max_length=15,choices=DAY_CHOICES,default='Sunday')
    code = models.SlugField(unique=True, blank=True , null=True)
    
    def save(self, *args , **kwargs):
        if not self.code :
            self.code = get_random_string(length=12, allowed_chars = string.ascii_lowercase)
        super(Schedule , self).save(*args , **kwargs)

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse('detail_schedule', kwargs={'pk': self.pk})
    
    @property
    def travel_time(self):
        date = datetime.date(1, 1, 1)
        datetime1 = datetime.datetime.combine(date, self.time_arrival)
        datetime2 = datetime.datetime.combine(date, self.time_depart)
        result = datetime1 - datetime2
        # result = time2-time1
        # result = datetime.timedelta(self.time_arrival , self.time_depart)
        return result.seconds/3600

class Station(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_station', kwargs={'pk': self.pk})