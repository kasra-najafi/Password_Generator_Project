from django.urls import path
from generator import views

app_name = 'generator'

urlpatterns = [
    path('home/', views.home, name='generator'),
    path('generatedpassword/', views.password, name='password'),
    path('about/', views.about, name='about'),
]