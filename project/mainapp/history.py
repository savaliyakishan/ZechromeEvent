from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

def history(request):
    if request.user.is_superuser == True:
        historydata=History.objects.all().order_by('id')
        contex={
            "historydata":historydata
        }
        return render(request,"Dashboard/history.html",contex)
    else:
        messages.error(request,"Permission Denied,Login Required...")
        return redirect('Login')
    
def historyclear(request):
    if request.user.is_superuser == True:
        historydata = History.objects.all()
        if len(historydata) > 0:
            historydata.delete()
            messages.info(request,"History Clear!")
        else:
            messages.info(request,"No Record Found.")
        return redirect('Dashboard-Member-History')
    else:
        messages.error(request,"Permission Denied,Login Required...")
        return redirect('Login')