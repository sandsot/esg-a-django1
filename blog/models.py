from email import contentmanager
from turtle import title
from unittest.util import _MAX_LENGTH
from venv import create
from django.db import models

# Post Model
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        # TODO : 장고의 URL Reverse 기능을 사용하기
        return f"/blog/{self.pk}/"

    def __str__(self):
        return f"[{self.pk}] {self.title}"