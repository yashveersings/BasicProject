from django.urls import path
from HelloDjangoApp import views

urlpatterns = [
    path('',views.home,name="home"),
    path('MFInfo',views.result,name = "result")
]
