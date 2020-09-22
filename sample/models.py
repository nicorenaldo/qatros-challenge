from django.db import models
from django.utils.crypto import get_random_string
import string

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    code = models.SlugField(unique=True, blank=True , null=True)
    
    def save(self, *args , **kwargs):
        if not self.code :
            self.code = get_random_string(length=12, allowed_chars = string.ascii_lowercase)
        super(Items , self).save(*args , **kwargs)

    def __str__(self):
        return self.name