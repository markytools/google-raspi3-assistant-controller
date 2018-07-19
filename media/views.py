from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import Audio,  Playlist

def index(request):
    return render(request,  'media/index.html',  {})

def musiclib(request):
    audio_list = Audio.objects.order_by('name')
    context = {'audio_list': audio_list}
    
    if request.method == 'POST' and 'id_audio_name' in request.POST:
        a = Audio.objects.filter(name=request.POST['id_audio_name'])
        if a:
            context['error_message'] = "Name already in the list"
            return render(request,  'media/musiclib.html',  context)
        a = Audio(name=request.POST['id_audio_name'], audio_file=request.FILES['file'])
        a.save()
        return HttpResponseRedirect(reverse('media:musiclib'))
        
    if "deleteAudioSubmit" in request.POST:
        deleteaudio_id = Audio.objects.get(pk=request.POST['deleteaudio'])
        deleteaudio_id.delete()
        audio_list = Audio.objects.order_by('name')
        context = {'audio_list': audio_list}
        return HttpResponseRedirect(reverse('media:musiclib'))
    
    return render(request,  'media/musiclib.html',  context)

def playlist(request):
    audio_list = Audio.objects.order_by("name")
    playlist_list = Playlist.objects.order_by("name")
    context = {'playlist_list': playlist_list,  'audio_list': audio_list}
    
    if "createNewPlaylistSubmit" in request.POST:
        p = Playlist(name=request.POST["playlist-name"])
        p.save()
        for audio in audio_list:
            if str('music' + str(audio.id)) in request.POST:
                p.audiolist.add(audio)
    
    if "editPlaylistSubmit" in request.POST:
        p = Playlist.objects.get(pk=request.POST["playlistIDInput"])
        for audio in audio_list:
            if str('music' + str(audio.id)) in request.POST:
                p.audiolist.add(audio)
            else: p.audiolist.remove(audio)
        p.name = request.POST["playlist-name"]
        p.save()
    
    if "deletePlaylistSubmit" in request.POST:
        p = Playlist.objects.get(pk=request.POST["deleteplaylist"])
        p.delete()
    
    return render(request,  'media/playlist.html',  context)
