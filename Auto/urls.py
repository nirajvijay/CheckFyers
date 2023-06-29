from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('generate-auth-code/', views.generate_auth_code, name='generate_auth_code'),
    
]
