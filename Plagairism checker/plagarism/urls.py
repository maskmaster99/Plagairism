from django.urls import path
from . import views

urlpatterns = [
path("",views.Register,name = "Register"),
path('login/' , views.Login , name= "Login"),
path('reg/',views.RegisterUser , name = 'RegisterUser'),
path('check/', views.Check,name = 'Check'),
path('authenticate/' , views.AuthenticateUser, name="AuthenticateUser"),
path('checkplag/',views.CheckPlag , name = "CheckPlag")

]
