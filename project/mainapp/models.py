from django.db import models

class MemberInfo(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False,db_column="Member_Name")
    email = models.EmailField(max_length=254,null=False,blank=False,unique=True,db_column="Member_Email")
    selectedStatus = models.BooleanField(default=False,db_column="Status")

class SelectedMember(models.Model):
    memberId = models.ForeignKey(MemberInfo, on_delete=models.CASCADE, db_column="Member_Id")
    topicName = models.CharField(max_length=255,unique=True,blank=True,null=True,db_column="Topic_Name")
    seminarDate = models.DateField(blank=False,null=False,db_column="Seminar_Date")
    activeStatus = models.BooleanField(default=True,db_column="Active_Status")

class DeleteSelectedMember(models.Model):
    deletedMemberObj = models.ForeignKey(SelectedMember,on_delete=models.CASCADE,db_column="SelectedMember_Id")
    dataTime = models.DateTimeField(auto_now=True,db_column="Data_Time")


class History(models.Model):
    memberName = models.CharField(max_length=255,null=True,blank=True,db_column="Member_Name")
    memberEmail = models.EmailField(max_length=254,null=True,blank=True,db_column="Member_Email")
    seminarDate = models.DateField(blank=True,null=True,db_column="Seminar_Date")
    topicName = models.CharField(max_length=255,unique=True,blank=True,null=True,db_column="Topic_Name")