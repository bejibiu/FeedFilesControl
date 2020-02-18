from django.urls import path

from manufacturers_feed import views

urlpatterns = [
    path('', views.index, name='index')
]
