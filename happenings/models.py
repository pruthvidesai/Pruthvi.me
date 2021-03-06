from django.db import models
from django.core.urlresolvers import reverse
from os import path

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    image = models.FileField(max_length=100, default="NULL")
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('happenings.views.post', args=[self.slug])
