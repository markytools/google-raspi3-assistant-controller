from django.shortcuts import render
from django.db.models import Q
from .models import LinphoneAccount
# Create your views here.

def linphoneapp(request):
    linphone_acct_list = LinphoneAccount.objects.order_by('name')
    context = {'linphone_acct_list': linphone_acct_list}
    
    if "addLinphoneAcctSubmit" in request.POST:
        newacct_name = request.POST["newacct_name"]
        newacct_sip = request.POST["newacct_sip"]
        if not newacct_name:
            context['error_message'] = "Enter a name"
            return render(request,  'linphoneapp/linphoneapp.html',  context)
        if not newacct_sip:
            context['error_message'] = "Enter a SIP account"
            return render(request,  'linphoneapp/linphoneapp.html',  context)
        l = LinphoneAccount.objects.filter(Q(name=newacct_name) | Q(sip_account=newacct_sip))
        if l:
            context['error_message'] = "Account already in the list"
            return render(request,  'linphoneapp/linphoneapp.html',  context)
        l = LinphoneAccount(name=newacct_name, sip_account=newacct_sip)
        l.save()
    
    if "editLinphoneAcctSubmit" in request.POST:
        editacct_id = request.POST["editacct_id"]
        editacct_name = request.POST["editacct_name"]
        editacct_sip = request.POST["editacct_sip"]
        l = LinphoneAccount.objects.get(pk=editacct_id)
        l.name = editacct_name
        l.sip_account = editacct_sip
        l.save()
        
    if "deleteLinphoneAcctSubmit" in request.POST:
        deleteacct_id = request.POST["deleteacct_id"]
        l = LinphoneAccount.objects.get(pk=deleteacct_id)
        l.delete()
    
    return render(request,  'linphoneapp/linphoneapp.html',  context)
