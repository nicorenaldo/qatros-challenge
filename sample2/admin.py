from django.contrib import admin

# Register your models here.
from .models import Bus,Schedule,Station
admin.site.register(Bus)
admin.site.register(Schedule)
admin.site.register(Station)