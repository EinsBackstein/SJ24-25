from django.db import models

# Create your models here.

class Person(models.Model):
    SEX_CHOICES = [('M','Male'), ('F', 'Female')]
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    sex = models.CharField(choices=SEX_CHOICES, max_length=1)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname
