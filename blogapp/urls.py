from django.urls import path
from .import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
urlpatterns = [
    path('',PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>',PostDetailView.as_view(),name='blog-detail'),
    path('new/',PostCreateView.as_view(),name ='blog-new'),
    path('update/<int:pk>',PostUpdateView.as_view(),name='blog-update'),
    path('delete/<int:pk>',PostDeleteView.as_view(),name='blog-delete'),
    path('about/',views.about,name='blog-about')
]