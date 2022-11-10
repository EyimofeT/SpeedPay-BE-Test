from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview , name = "api-overview"),
    path('signup/', views.userCreate , name = "user-create"),
    
    # path('login/', views.userLogin , name = "user-login"),
    # path('logout/',views.logout, name="logout"),
    
    path('accountdetails/', views.accountdetails, name="account_details"),
    
    path('deposit/',views.deposit, name="logout"),
    path('withdrawal/',views.withdrawal, name="logout"),
    
    
   
]