
from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=250,null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(max_length=250,upload_to ="post/",null=True)