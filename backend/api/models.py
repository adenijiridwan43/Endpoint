from django.db import models

# Create your models here.

class personBio (models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=60, unique=True)
    
    def __str__(self):
        return self.name
    