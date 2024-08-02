from django.urls import path
from .import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('profile',views.profile, name='blog-profile'),
    path('logout', views.logout, name='logout'),
    path('profile/update/', views.profile_update, name='profile-update'),
]