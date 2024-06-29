from django.db import models
# Create your models here.

class Feature(models.Model):
   
   name = models.CharField(max_length=255)
   detail = models.CharField(max_length=255)
   
   # now we have no need of this thing as when we use the models.Models
    # id: int
    # name: str
    # detail: str
    # is_true: bool