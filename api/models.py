from django.contrib.auth.models import AbstractUser
from django.db import models


class Book(models.Model):
    id = models.UUIDField(max_length=25, primary_key=True, unique=True, editable=False)
    author = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=50, blank=False)
    published_year = models.DateField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title

