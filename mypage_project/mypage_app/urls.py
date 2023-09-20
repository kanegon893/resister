#path関数をインポート
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('formpage', views.FormView.as_view(),name="formpage"),
    path('',views.Login,name='Login'),
    path("logout",views.Logout,name="Logout"),
    path('register',views.AccountRegistration.as_view(), name='register'),
    path("home",views.home,name="home"),
]
