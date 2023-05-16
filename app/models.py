from django.db import models

# Create your models here.


class school(models.Model):
    sname=models.CharField(max_length=100)
    sid=models.IntegerField(primary_key=True)
    sadd=models.CharField(max_length=1000)