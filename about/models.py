from django.db import models

# Create your models here.
class About(models.Model):
    page = models.CharField(max_length=255)
    context = models.TextField()

    def __unicode__(self):
	return self.page
