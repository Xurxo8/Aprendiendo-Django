"""Users URLs."""

# Django
from django.urls import path
from django.views.generic import TemplateView
# View
from users import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('registro', views.SignupView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('registro_completado/', TemplateView.as_view(template_name='users/registerok.html'), name='registerok'),
]