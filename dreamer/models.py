from django.db import models

# Create your models here.
class Dreamer(models.Model):
    page = models.CharField(max_length=255)
    content = models.TextField()

    def __unicode__(self):
	    return self.page

