from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('innerpage/',views.innerpage,name='innerpage'),
    path('portfoliodetails/',views.portfoliodetails,name='portfoliodetails'),
    ]
