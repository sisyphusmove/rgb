from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField('TYPE', max_length=1)
    email = models.CharField('EMAIL', max_length=100, default='')
    age = models.IntegerField('AGE')
    gender = models.CharField('GENDER', max_length=2)
    create_date = models.DateTimeField('CREATE_DATE', auto_now_add=True)
    status = models.CharField('STATUS', max_length=1, default='Y')