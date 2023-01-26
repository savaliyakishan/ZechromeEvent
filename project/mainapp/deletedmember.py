from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import datetime
import calendar


def deletedmemberview(request):
    if request.user.is_superuser == True:
        today = datetime.date.today()
        next_date = today + \
            datetime.timedelta((calendar.SATURDAY-today.weekday()) % 7)
        deletememberdata = DeleteSelectedMember.objects.all().order_by('dataTime')
        context = {
            "deleteMemberData": deletememberdata,
        }
        return render(request, 'Dashboard/deletedmember.html', context)
    else:
        messages.error(request, "Permission Denied,Login Required...")
        return redirect('Login')


def restore(request):
    if request.user.is_superuser == True:
        if request.GET['restore']:
            id = request.GET['restore']
            selectedid = request.GET['deletedId']
            today = datetime.date.today()
            next_date = today + \
                datetime.timedelta((calendar.SATURDAY-today.weekday()) % 7)
            selectedmemberdata = SelectedMember.objects.filter(
                seminarDate=next_date, activeStatus='True').order_by('id')
            if len(selectedmemberdata) >= 5:
                messages.info(request, "No Member Selected.")
                return redirect('Dashboard-Selected-Member')
            SelectedMember.objects.filter(id=selectedid).update(
                activeStatus=True
            )
            DeleteSelectedMember.objects.get(id=id).delete()
            return redirect('Dashboard-Selected-Member')
    else:
        messages.error(request, "Permission Denied,Login Required...")
        return redirect('Login')


def clearalldeletedata(request):
    if request.user.is_superuser == True:
        if request.method == 'GET':
            selectedmemberdata = DeleteSelectedMember.objects.all()
            if len(selectedmemberdata) < 1:
                messages.info(request, "No Record Found.")
                return redirect('Dashboard-Deleted-Member-View')
            for i in selectedmemberdata:
                id = i.deletedMemberObj.memberId.id
                MemberInfo.objects.filter(id=id).update(
                    selectedStatus=False
                )
            selectedmemberdata.delete()
            messages.info(request, "All DeleteMembaer Data Clear. ")
            return redirect('Dashboard-Selected-Member')
    else:
        messages.error(request, "Permission Denied,Login Required...")
        return redirect('Login')
