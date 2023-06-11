from django.urls import path

from .views import FeedView, PostLike, PostUpdate, PostDelete, PostFile, PostView

urlpatterns = [
    path('feed/', FeedView, name='feed'),
    path('feed/post-<int:pk>', PostView, name='post'),
    path('feed/post-<int:pk>/edit/', PostUpdate.as_view(), name='edit-post'),
    path('feed/post-<int:pk>/delete/', PostDelete, name='delete-post'),
    path('feed/post-<int:pk>/file/', PostFile, name='file-post'),
    path('feed/like-post-<int:pk>', PostLike, name='like-post'),
]