from django.urls import path
from . import views
from Shopsy.views import*

urlpatterns=[
    path('',views.home,name='home')

]