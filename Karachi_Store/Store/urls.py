from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('contact/',views.contact),
    path('message/',views.Message, name='message'),
]