from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Momento(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta():
    	ordering = ['created']

    def __unicode__(self):
	    return self.title

    def get_absolute_url(self):
	    return reverse('momentographer.views.index')
