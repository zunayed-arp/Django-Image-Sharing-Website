from django.urls import path
from .views import (
    PostListView,
    UserPostListView,
    post_detail, create_post, post_delete, PostUpdateView, like, search_posts,
)


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/new/', create_post, name='post_create'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('like/', like, name='post_like'),
    path('post/<int:id>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:id>/delete/', post_delete, name='post_delete'),
    path('search_posts/', post_delete, name='search_posts'),
    path('user_posts/<str:username>/',UserPostListView.as_view(), name='user_posts'),


]
