from django.db import models

class Members(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=50)
    age = models.IntegerField(max_length=3)
    
#not finished yet
