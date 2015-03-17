from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Creator(models.Model):
    title = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    external = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        '''
        if self.external == True:
            return "http://%s" % self.website
        else:
            return reverse('%s.views.index' % self.website)
        '''
        return reverse('creator.views.index')