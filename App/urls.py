from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="homepage"),
    path('signup',signup,name="signup"),
    path('login',login,name="login"),
    path('order',order,name="order"),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
    path('report',reports,name="report"),
    path('creports',creports,name="creports"),
    path('ordernow/<int:product_id>/',ordernow,name="ordernow"),
    path('alogin',alogin,name="alogin"),
    path('one_product/<int:product_id>/',one_product,name="one_product"),
    path('oreport',oreport,name="oreport")
]