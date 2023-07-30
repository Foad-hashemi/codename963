from django.urls import path
from . import views

app_name = "Accounts"
urlpatterns = [
    path('register', views.Register.as_view(), name="register"),
    path('login', views.Login.as_view(), name='login'),
    path('address', views.AddAddress.as_view(), name='addAddress'),

]
