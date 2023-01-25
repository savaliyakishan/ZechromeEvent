from django.urls import path,include
from .views import *
from .dashboard import *
from .deletedmember import *
from .history import *
urlpatterns = [
    path('',index,name="Index" ),
    path('login/',admin_login,name="Login" ),
    path('logout/',user_logout,name='logout'),

    # Dashbord Urls

    path('dashboard/home/',home,name="Dashboard-Home"),
    path('dashboard/view/',viewmember,name="Dashboard-view"),
    path('dashboard/ragister/',ragister,name="Dashboard-Ragister"),
    path('dashboard/update/',update,name="Dashboard-Update"),
    path('dashboard/delete/<int:id>',delete,name="Dashboard-Delete"),
    path('dashboard/choose/',choosemember,name="Dashboard-choose-Member"),
    path('dashboard/selectedmember/view/',selectedmemberview,name="Dashboard-Selected-Member"),
    path('dashboard/selectedmember/clearall/',restartprogram,name="Dashboard-Delete-Member-Restart"),
    path('dashboard/selectedmember/delete/<int:id>',selectedmemberdelete,name="Dashboard-Deleted-Member"),
    path('dashboard/selectedmember/done/<int:id>',selectedmemberdone,name="Dashboard-Done-Member"),
         
    # Member Delete Urls
    path('dashboard/deletedmember/',deletedmemberview,name="Dashboard-Deleted-Member-View"),
    path('dashboard/deletedmember/clearAll/delete/',clearalldeletedata,name="Dashboard-Deleted-Member-Restore"),
    path('dashboard/selectedmember/delete/restore/',restore,name="Dashboard-Deleted-Member-Restore"),
        
         

    path('dashboard/history/',history,name="Dashboard-Member-History"),
    path('dashboard/history/clearall/',historyclear,name="Dashboard-Member-History-Clear"),
]
