from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    title = models.CharField('TITLE', max_length=100)
    content = models.TextField('CONTENT')
    writer = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    create_date = models.DateTimeField('CREATE_DATE', auto_now_add=True)
    modify_date = models.DateTimeField('MODIFY_DATE', auto_now=True)
    category = models.CharField('CATEGORY', max_length=10)
    status = models.CharField('STATUS', max_length=1, default='Y')

class Comment(models.Model):
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('CREATE_DATE', auto_now_add=True)
    modify_date = models.DateTimeField('MODIFY_DATE', auto_now=True)
    status = models.CharField('STATUS', max_length=1, default='Y')