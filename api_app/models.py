from django.db import models

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=200)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)

