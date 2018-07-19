from __future__ import unicode_literals

from django.db import models

# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.
class Audio(models.Model):
    name = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='/home/pi/Documents/typiremote/audiofiles/')
    
    def __str__(self):
        return "Audio(name=%s, file=%s)" % (self.name,  self.audio_file)

@receiver(pre_delete, sender=Audio)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.audio_file.delete(False)

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    audiolist = models.ManyToManyField(Audio)
    
    def __str__(self):
        return "Playlist(name=%s,\n  audiolist=%s)" % (self.name, self.audiolist.all())
