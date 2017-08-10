from __future__ import unicode_literals

from django.db import models
from gallery.fields import ThumbnailImageField

class Categories(models.Model):
    name = models.CharField(max_length=250)
    
    class Meta:
        ordering=['name']
        
    def __str__(self):
        return self.name

    
class Photo(models.Model):
    item = models.ForeignKey(Categories)
    image = ThumbnailImageField(upload_to='photos')
    time_stamp = models.DateTimeField(auto_now_add=True, editable=False)
    
    class Meta:
        ordering=['time_stamp']