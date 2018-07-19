from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserSettings(models.Model):
    name = models.CharField(max_length=100)
    linphone_sip_acct = models.CharField(max_length=200)
    linphone_sip_pwd = models.CharField(max_length=200)
    speech_source = models.IntegerField()
    volume  = models.IntegerField()
    
    def __str__(self):
        return "UserSettings(name=%s, linphone_sip_acct=%s, linphone_sip_pwd=%s, speech_source=%d, volume=%d)" % (self.name,  self.linphone_sip_acct,  self.linphone_sip_pwd,  self.speech_source,  self.volume)

#class ScheduledTask(models.Model):
#    name = models.CharField(max_length=200)
#    repetitions = models.CharField(max_length=200)
#    
#    def __str__(self):
#        return "ScheduledTask(name=%s)" % (self.name)
#
#class DurationTask(ScheduledTask):
#    name = models.CharField(max_length=200)
#    
#    def __str__(self):
#        return "ScheduledTask(name=%s)" % (self.name)
