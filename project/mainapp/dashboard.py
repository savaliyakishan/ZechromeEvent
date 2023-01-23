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
        return redirect('Login')

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
        return redirect('Login')
    
def viewmember(request):
    if request.user.is_superuser == True:
        memberData = member.objects.all().order_by('id')
        contex={
            'memberData':memberData
        }
        return render(request,'Dashboard/viewmember.html',contex)
    else:
        messages.error(request,"Bed-Request?")
        return redirect('Login')
    
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
        return redirect('Login')

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
        return redirect('Login')
    
def chooseMember(request,id=None):
    if request.user.is_superuser == True:
        if request.method == "GET":
            today = datetime.date.today()
            next_date = today + datetime.timedelta((calendar.SATURDAY-today.weekday()) % 7 )
            selectedmemberData = selectedmember.objects.filter(SeminarDate=next_date)
            if len(selectedmemberData) >= 5:
                messages.info(request,"No Member selected")
                return redirect('Dashboard-Selected-Member')
            memberData = member.objects.filter(selectedstatus=False).order_by('id')
            random_member = random.choice(memberData)
            random_member.selectedstatus = True
            random_member.save()
            selectedmember.objects.create(
                memberId=random_member,
                SeminarDate=next_date
            )
        return redirect('Dashboard-Selected-Member')
    else:
        messages.error(request,"Bed-Request?")
        return redirect('Login')
    
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
        return redirect('Login')
    
def selectedMemberDelete(request,id=None):
    if request.user.is_superuser == True:
        if id is not None:
            selectedMemberObj = selectedmember.objects.filter(id=id)
            if len(selectedMemberObj) == 1:
                member.objects.filter(id=selectedMemberObj[0].memberId.id).update(
                    selectedstatus=False
                )
                selectedMemberObj[0].delete()
                return redirect('Dashboard-Selected-Member')
            else:
                messages.error(request,"Pelase Enter Valid Id")
                return redirect('Dashboard-Selected-Member')
        else:
            return redirect('Dashboard-Selected-Member')
    else:
        messages.error(request,"Bed-Request?")
        return redirect('Login')
