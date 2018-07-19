from django.shortcuts import render
from django.http import JsonResponse
from .models import MessageLog

# Create your views here.
def index(request):
    MessageLog.objects.all().delete()
    return render(request, 'console/index.html', {})

def data(request):
    if MessageLog.objects.all().count() >= 100:
        for msg in MessageLog.objects.order_by('pub_date')[:50]: msg.delete()
    latest_id = -1
    previousID = request.GET['previousID']
    latest_messages = MessageLog.objects.order_by('-pub_date')[:50]
    msg_to_display= []
    for msg in latest_messages.reverse():
        if long(previousID) == msg.pk:
            msg_to_display = []
            continue
        msg_to_display.append(msg.message)
    if latest_messages: latest_id = latest_messages.first().pk
    data = {
        'latest_id': latest_id, 
        'msg_do_display': msg_to_display
    }
    return JsonResponse(data)
