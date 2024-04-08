from django.db import models

# Create your models here.

class Contact(models.Model):
    firstname =models.CharField( max_length=50)
    lastname =models.CharField( max_length=50)
    subject=models.CharField(max_length=50)
    Address =models.CharField(max_length=50)
    
    def __str__(self):
        return self.firstname
