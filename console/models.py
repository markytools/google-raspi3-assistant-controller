from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MessageLog(models.Model):
    message = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return "message: %s, pub_date: %s" % (self.message,  self.pub_date)
