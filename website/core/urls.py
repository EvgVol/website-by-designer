from django.urls import path

from . import views

app_name = 'core'


urlpatterns = [
    path('', views.main, name='index'),
    path('policy/', views.policy, name='policy'),
]
