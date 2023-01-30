from django.db import models

# Create your models here.
class FORMAT(models.Model):
    name=models.CharField(max_length=15)
    des=models.TextField()
    dur=models.IntegerField()
    img=models.ImageField(upload_to='photos')