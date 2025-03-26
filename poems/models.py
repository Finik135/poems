from django.db import models
from django.contrib.auth.models import User
from django.db import models
import datetime

class Poem(models.Model):
    title = models.CharField(max_length=255, default="Без назви")
    text = models.TextField()
    image = models.ImageField(upload_to='poems_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(
        max_length=250,
    )
    text = models.CharField(
        max_length=10000,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )


    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.CharField(max_length=10000)
    poem = models.ManyToManyField(
        "Poem",
        related_name="review",
        null=True
    )
    author_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.text[:10]
