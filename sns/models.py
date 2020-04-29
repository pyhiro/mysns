from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class PostModel(models.Model):
    context = models.TextField(max_length=200)
    post_name = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.context[:10]


