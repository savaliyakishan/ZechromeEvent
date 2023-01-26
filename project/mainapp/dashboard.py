from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate
import random,datetime,calendar
from datetime import date

def home(request):
    if request.user.is_superuser == True:
        return render(request,'Dashboard/home.html',{"class" : "active"})
    else:
        messages.error(request,"Permission Denied,Login Required...")
        return redirect('Login')

def ragister(request):
    if request.user.is_superuser == True:
        if request.method == "POST":
            membername = request.POST['memberName']
            email = request.POST['memberEmail']
            try:
                MemberInfo.objects.create(
                    name = membername,
                    email = email
                )
                messages.success(request,"Add Member Succeed.")
            except Exception as ex:
                messages.error(request,f"{ex}")
            return redirect('Dashboard-view')
        return render(request,'Dashboard/home.html')
    else:
        messages.error(request,"Permission Denied,Login Required...")
        return redirect('Login')
    
def viewmember(request):
    if request.user.is_superuser == True:
        memberdata = MemberInfo.objects.all().order_by('id')
        contex={
            'memberData':memberdata,
        }
        return render(request,'Dashboard/viewmember.html',contex)
    else:
        messages.error(request,"Permission Denied,Login Required...")
        return redirect('Login')
    
def update(request):
    if request.user.is_superuser == True:
        if request.method == "POST":
            id = request.POST['memberid']
            membername = request.POST['memberName']
            email = request.POST['memberEmail']
            memberdata = MemberInfo.objects.get(id=id)
            try:
                memberdata.name = membername
                memberdata.email = email
                memberdata.save()
                messages.success(request,"Update Member Succeed.")
            except Exception as ex:
                messages.error(request,f"{ex}")
            return redirect('Dashboard-view')
        return render(request,'Dashboard/home.html')
    else:
        messages.error(request,"Permission Denied,Login Required...")
        return redirect('Login')

def delete(request, id=None):
    if request.user.is_superuser == True:
        if id is not None:
            try:
                MemberInfo.objects.get(id=id).delete()
                messages.success(request,"Member Delete Succeed.")
            except Exception as ex:
                messages.error(request,"User Dose Not Exist.")
        else:
            messages.error(request,"Pelase Select Member.")
        return redirect('Dashboard-view')
    else:
        messages.error(request,"Permission Denied,Login Required...")
        return redirect('Login')
    
def choosemember(request,id=None):
    if request.user.is_superuser == True:
        dayName = datetime.datetime.today().strftime("%A")
        if request.method == "GET" :
            today = datetime.date.today()
            next_date = today + datetime.timedelta((calendar.SATURDAY-today.weekday()) % 7 )
            selectedmemberdata = SelectedMember.objects.filter(seminarDate=next_date,activeStatus=True)
            if len(selectedmemberdata) >= 5:
                messages.info(request,"No Member Selected")
                return redirect('Dashboard-Selected-Member')
            memberdata = MemberInfo.objects.filter(selectedStatus=False).order_by('id')
            if len(memberdata) == 0:
                messages.info(request,"Not Avilable Member.")
                return redirect('Dashboard-Selected-Member')
            random_member = random.choice(memberdata)
            random_member.selectedStatus = True
            random_member.save()
            SelectedMember.objects.create(
                memberId=random_member,
                seminarDate=next_date
            )
        else:
            messages.info(request,'Only Saturday Run.')
        return redirect('Dashboard-Selected-Member')
    else:
        messages.error(request,"Permission Denied,Login Required...")
        return redirect('Login')
    
def selectedmemberview(request):
    if request.user.is_superuser == True:
        if request.method == "POST":
            try:
                id = request.POST['selectedmemberid']
                topic_name = request.POST['topicName']
                SelectedMember.objects.filter(id=id).update(
                    topicName=topic_name
                )
                messages.success(request,"Topic Add Succeed.")
            except Exception as Ex:
                messages.error(request,"Topic Already Added..")
            return redirect('Dashboard-Selected-Member')
        today = datetime.date.today()
        next_date = today + datetime.timedelta((calendar.SATURDAY-today.weekday()) % 7 )
        selectedmemberdata = SelectedMember.objects.filter(seminarDate=next_date,activeStatus='True').order_by('id')
        user_name = []
        curr_date = date.today()
        day = calendar.day_name[curr_date.weekday()]
        for i in selectedmemberdata:
            user_name.append(i.memberId.name)
        context= {
                "selectedMember":selectedmemberdata,
                "username" : user_name,
                "day" : day
        }
        return render(request,'Dashboard/selectedmember.html',context)
    else:
        messages.error(request,"Permission Denied,Login Required...")
        return redirect('Login')
    
def  selectedmemberdelete(request,id=None):
    if request.user.is_superuser == True:
        if id is not None:
            selectedmemberobj = SelectedMember.objects.filter(id=id)
            if len(selectedmemberobj) == 1:
                selectedmemberobj[0].activeStatus = False
                selectedmemberobj[0].save()
                DeleteSelectedMember.objects.create(deletedMemberObj = selectedmemberobj[0])
                return redirect('Dashboard-Selected-Member')
            else:
                messages.error(request,"Pelase Enter Valid Id.")
                return redirect('Dashboard-Selected-Member')
        else:
            return redirect('Dashboard-Selected-Member')
    else:
        messages.error(request,"Permission Denied,Login Required...")
        return redirect('Login')
    

def selectedmemberdone(request,id=None):
    if request.user.is_superuser == True:
        if id is not None:
            selectedmemberobj = SelectedMember.objects.filter(id=id)
            if len(selectedmemberobj) == 1:
                selectedmemberobj[0].activeStatus = False
                selectedmemberobj[0].save()
                History.objects.create(
                    memberName = selectedmemberobj[0].memberId.name,
                    memberEmail = selectedmemberobj[0].memberId.email,
                    seminarDate = selectedmemberobj[0].seminarDate,
                    topicName = selectedmemberobj[0].topicName,
                )
                return redirect('Dashboard-Selected-Member')
            else:
                messages.error(request,"Pelase Enter Valid Id.")
                return redirect('Dashboard-Selected-Member')
        else:
            return redirect('Dashboard-Selected-Member')
    else:
        messages.error(request,"Permission Denied,Login Required...")
        return redirect('Login')
    
def restartprogram(request):
    if request.user.is_superuser == True:
        if request.method == "POST":
            password = request.POST['checkpassword']
            username = request.user.username
            user=authenticate(username=username,password=password)
            if user is not None:
                selectedmemberobj = SelectedMember.objects.all()
                memberobj = MemberInfo.objects.all()
                if len(selectedmemberobj) > 0:
                    for i in selectedmemberobj:
                        i.delete()
                    for j in memberobj:
                        j.selectedStatus = False
                        j.save()
                    messages.success(request,'Project Restart')
                    return redirect('Dashboard-Home')
                else:
                    messages.error(request,"No Record Found.")
                    return redirect('Dashboard-Home')
            else:
                messages.error(request,"Password Not Match..")
                return redirect('Dashboard-Home')
    else:
        messages.error(request,"Permission Denied,Login Required...")
        return redirect('Login')