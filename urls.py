from django.urls import path
from . import views
from store.views import*

urlpatterns=[
    path('',views.home,name='home')

]