from __future__ import unicode_literals

from django.db import models

# Create your models here.
class LinphoneAccount(models.Model):
    name = models.CharField(max_length=50)
    sip_account = models.CharField(max_length=200)
    
    def __str__(self):
        return "name: %s, sip_account: %s" % (self.name,  self.sip_account)
    
