from django.db import models
from uuid import uuid4


class Review(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, editable=False)
    url_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    review = models.TextField()
    public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
