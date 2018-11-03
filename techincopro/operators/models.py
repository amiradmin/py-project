from django.db import models

# Create your models here.

class Operator(models.Model):
    name =  models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email  = models.EmailField()

    def __str__(self):
        return self.name
