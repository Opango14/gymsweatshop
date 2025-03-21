from django.db import models

# Create your models here.
# this file we creates database tables

class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=12)
    description=models.TextField()
    def __str__(self):
        return self.email