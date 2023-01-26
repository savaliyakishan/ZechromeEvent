from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(MemberInfo)
admin.site.register(SelectedMember)
admin.site.register(DeleteSelectedMember)
admin.site.register(History)
