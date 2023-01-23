from django.urls import path,include
from . import views
from . import dashboard
urlpatterns = [
    path('',views.index,name="Index" ),
    path('login/',views.admin_login,name="Login" ),
    path('logout/',views.user_logout,name='logout'),
    path('NotFound/',views.NotFound,name='Not-Found'),

    path('Dashboard/home/',dashboard.Home,name="Dashboard-Home"),
    path('Dashboard/view/',dashboard.viewmember,name="Dashboard-view"),
    path('Dashboard/ragister/',dashboard.ragister,name="Dashboard-Ragister"),
    path('Dashboard/update/',dashboard.update,name="Dashboard-Update"),
    path('Dashboard/delete/<int:id>',dashboard.delete,name="Dashboard-Delete"),
    path('Dashboard/choose/',dashboard.chooseMember,name="Dashboard-choose-Member"),
    path('Dashboard/selectedmember/view/',dashboard.selectedmemberview,name="Dashboard-Selected-Member"),
    path('Dashboard/selectedmember/delete/<int:id>',dashboard.selectedMemberDelete,name="Dashboard-Selected-Member"),
]
