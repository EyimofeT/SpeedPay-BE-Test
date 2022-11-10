from django.urls import path
from . import views

urlpatterns = [
    
    path('login/', views.userLogin , name = "user-login"),
    path('logout/',views.logout, name="logout"),
   
]