from django.db import models
from django.urls import reverse

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128, unique=True)
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length=256)
    date_of_birth = models.DateField(max_length=128)
    balance = models.FloatField()

    def __str__(self):
        return self.name

class Transfers(models.Model):
    person1 = models.CharField(max_length=128)
    person2 = models.ForeignKey('Users.Users', on_delete=models.CASCADE)
    amount = models.FloatField() 

    def get_absolute_url(self):
        return reverse("users:transaction")


