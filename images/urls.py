from django.urls import path

from . import views


app_name='images'

urlpatterns = [
    path('', views.upload, name='upload'),
    path('image/<slug:slug>/', views.detail, name='detail'),
]
