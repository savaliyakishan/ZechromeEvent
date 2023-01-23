from django.db import models
from django.contrib.auth.models import AbstractUser

class member(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False,unique=True,db_column="Member_Name")
    email = models.EmailField(max_length=254,null=False,blank=False,unique=True,db_column="Member_Email")
    selectedstatus = models.BooleanField(default=False,db_column="Status")

    # def __dict__(self):
    #     return{
    #         "name":self.name,
    #         "email":self.email,
    #         "selectedstatus":self.selectedstatus,
    #     }
    
class selectedmember(models.Model):
    memberId = models.ForeignKey(member, on_delete=models.CASCADE, db_column="Member_Id")
    topicname = models.CharField(max_length=255,unique=True,blank=True,null=True,db_column="Topic_Name")
    SeminarDate = models.DateField(blank=False,null=False,db_column="Seminar_Date")