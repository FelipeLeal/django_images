from django.db import models

# Create your models here.
class Photo(models.Model):
    nickname = models.CharField(max_length=255)
    pet_name = models.CharField(max_length=255)
    img_url = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    rank = models.FloatField()

