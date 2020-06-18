from django.urls import path
from . import views

#url mapping level 2
urlpatterns = [
    path('', views.home, name='overview-default'),
    path('overview/', views.home, name='overview-default'),
    path('overview-activity/', views.activity, name='overview-activity'),
    path('overview-user/', views.user, name='overview-user'),
    path('overview-time/', views.time, name='overview-time'),
    path('overview/test/', views.testPage, name='test')
]