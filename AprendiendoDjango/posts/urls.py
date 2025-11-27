"""Posts URLs."""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [
    path('', views.PostsFeedView.as_view(), name='blog'),
    path('posts/<slug:url>/', views.PostDetailView.as_view(), name='detail'),
    path('posts/save_comment/', views.save_comment, name='save_comment'),
]