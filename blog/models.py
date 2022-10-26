from email import contentmanager
from turtle import title
from unittest.util import _MAX_LENGTH
from venv import create
from django.db import models

# Post Model
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    create_at = models.DateTimeField()

