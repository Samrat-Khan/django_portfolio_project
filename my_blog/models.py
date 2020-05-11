from django.db import models


class MyBlogs(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='my_blog/images')
    url = models.URLField(blank=True)
    date = models.DateField(auto_now=True)
