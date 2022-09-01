from django.db import models

class Post(models.Model):
    CHOICES_STATUS = (
        ('pub','Publisher'),
        ('drf','Draft'),
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    auther = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modify = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=CHOICES_STATUS, max_length=3)
