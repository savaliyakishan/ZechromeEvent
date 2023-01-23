from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import random,datetime,calendar

def Home(request):
    if request.user.is_superuser == True:
        return render(request,'Dashboard/home.html')
    else:
        messages.error(request,"Bed-Request?")
        return redirect('Not-Found')

def ragister(request):
    if request.user.is_superuser == True:
        if request.method == "POST":
            membername = request.POST['memberName']
            email = request.POST['memberEmail']
            try:
                member.objects.create(
                    name = membername,
                    email = email
                )
                messages.success(request,"Add Member")
            except Exception as ex:
                messages.error(request,f"{ex}")
            return redirect('Dashboard-Home')
        return render(request,'Dashboard/home.html')
    else:
        messages.error(request,"Bed-Request?")
        return redirect('Not-Found')
    
def viewmember(request):
    if request.user.is_superuser == True:
        memberData = member.objects.all().order_by('id')
        contex={
            'memberData':memberData
        }
        return render(request,'Dashboard/viewmember.html',contex)
    else:
        messages.error(request,"Bed-Request?")
        return redirect('Not-Found')
    
def update(request):
    if request.user.is_superuser == True:
        if request.method == "POST":
            id = request.POST['memberid']
            membername = request.POST['memberName']
            email = request.POST['memberEmail']
            memberData = member.objects.get(id=id)
            try:
                memberData.name = membername
                memberData.email = email
                memberData.save()
                messages.success(request,"update Member")
            except Exception as ex:
                messages.error(request,f"{ex}")
            return redirect('Dashboard-view')
        return render(request,'Dashboard/home.html')
    else:
        messages.error(request,"Bed-Request?")
        return redirect('Not-Found')

def delete(request, id=None):
    if request.user.is_superuser == True:
        if id is not None:
            try:
                member.objects.get(id=id).delete()
                messages.success(request,"member Delete")
            except Exception as ex:
                messages.error(request,"User Dose Not Exist.")
        else:
            messages.error(request,"pelse select member")
        return redirect('Dashboard-view')
    else:
        messages.error(request,"Bed-Request?")
        return redirect('Not-Found')
    
def chooseMember(request,id=None):
    if request.user.is_superuser == True:
        if id is not None:
            memberobj = member.objects.get(id=id)
            memberobj.selectedstatus = True
            memberobj.save()
            today = datetime.date.today()
            next_date = today + datetime.timedelta((calendar.SATURDAY-today.weekday()) % 7 )
            selectedmember.objects.create(
                memberId=memberobj,
                SeminarDate=next_date
            )
            messages.success(request,"Selected Member")
            return redirect('Dashboard-Home')
        if request.method == "GET":
            today = datetime.date.today()
            next_date = today + datetime.timedelta((calendar.SATURDAY-today.weekday()) % 7 )
            selectedmemberData = selectedmember.objects.filter(SeminarDate=next_date)
            if len(selectedmemberData) >= 5:
                messages.info(request,"No Memberselected")
                return redirect('Dashboard-Home')
            memberData = member.objects.filter(selectedstatus=False).order_by('id')
            random_member = random.choice(memberData)
            context= {
                "selectedMember":random_member
            }
        return render(request,'Dashboard/memberselect.html',context)
    else:
        messages.error(request,"Bed-Request?")
        return redirect('Not-Found')
    
def selectedmemberview(request):
    if request.user.is_superuser == True:
        if request.method == "POST":
            try:
                id = request.POST['selectedmemberid']
                topicName = request.POST['topicName']
                selectedmember.objects.filter(id=id).update(
                    topicname=topicName
                )
                messages.success(request,"Topic  Added..")
            except Exception as Ex:
                messages.error(request,"Topic Already Added..")
            return redirect('Dashboard-Selected-Member')
        today = datetime.date.today()
        next_date = today + datetime.timedelta((calendar.SATURDAY-today.weekday()) % 7 )
        selectedmemberData = selectedmember.objects.filter(SeminarDate=next_date).order_by('id')
        context= {
                "selectedMember":selectedmemberData
            }
        return render(request,'Dashboard/selectedmember.html',context)
    else:
        messages.error(request,"Bed-Request?")
        return redirect('Not-Found')