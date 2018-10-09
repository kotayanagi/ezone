from django.db import models

# Create your models here.

class Miyagi(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    
