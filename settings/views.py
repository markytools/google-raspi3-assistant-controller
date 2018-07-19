from django.shortcuts import render

from .models import UserSettings
# Create your views here

def index(request):
    context = {}
    currentAccount = UserSettings.objects.filter(name="current")
    if len(currentAccount) == 0:
        currentAccount = UserSettings(name="current")
        currentAccount.save()
    else:
        currentAccount = currentAccount[0]
    if request.method == 'POST':
        currentAccount.linphone_sip_acct = request.POST["sip_name"]
        currentAccount.linphone_sip_pwd = request.POST["sip_pwd"]
        currentAccount.speech_source = int(request.POST["speech-source-radios"])
        currentAccount.save()
        context['msg_error'] = "0"
        context['result_msg'] = "Settings have been updated"
    context['sip_name'] = currentAccount.linphone_sip_acct
    context['sip_pwd'] = currentAccount.linphone_sip_pwd
    context['speech_source'] = currentAccount.speech_source
    return render(request,  'settings/index.html',  context)
