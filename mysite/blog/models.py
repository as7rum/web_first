from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    full_text = models.TextField()
    summary = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    # tag = models.CharField(max_length=255, null=True)
    # slug = ... #TODO
    # is_published = models.BooleanField() #TODO
