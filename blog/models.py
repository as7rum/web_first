from django.db import models
from django.urls import reverse


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    full_text = models.TextField()
    summary = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    # tag = models.CharField(max_length=255, null=True)
    slug = models.CharField(max_length=255, unique=True)
    # is_published = models.BooleanField() #TODO

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_page', kwargs={'slug': self.slug})
