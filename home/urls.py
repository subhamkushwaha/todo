from django.urls import path
from .import views
urlpatterns = [
    path("",views.home, name='home'),
    path("login",views.login,name='login'),
    path("signup",views.signup,name='signup'),
    path("addTODO",views.addTODO,name='addTODO'),
    path("signout",views.signout,name='signout'),
    path("delete/<int:id>",views.delete),
    path("changestatus/<int:id>/<str:status>",views.changestatus),
    path("changetodo/<int:id>/<str:status>",views.changetodo),
]

