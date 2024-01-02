from django.db import models
from django.conf import settings

# Create your models here.
class Tag(models.Model):
    value = models.TextField(max_length=100)

    def __str__(self):
        return self.value

class Post(models.Model):
    # Levarage the built-in user model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    # auto_now_add - the creation date and time will automatically be set when post is saved
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now - the modification date and time will automatically be set when post is saved
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    title = models.TextField(max_length=100)
    # slugify the given input
    slug = models.SlugField()
    summary = models.TextField(max_length=500)
    content = models.TextField()
    # Relationship
    tags = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return self.title
