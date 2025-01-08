from django.urls import path
from .views import PostDetailView,PostListView,PostCreateView,PostUpdateView,PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('',PostListView.as_view(),name='blogsite-homepage' ),
     path('user/<str:username>',UserPostListView.as_view(),name='user-post' ),
    path('post/<int:pk>',PostDetailView.as_view(),name='post-detail' ),
    path('post/new',PostCreateView.as_view(),name='post-create' ),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update' ),
     path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete' ),
    path('aboutpage/',views.about,name='blogsite-aboutpage' ),
    path('supportpage/',views.support,name='blogsite-supportpage' ),
]
