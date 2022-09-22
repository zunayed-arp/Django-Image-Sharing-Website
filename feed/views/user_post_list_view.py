
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, UpdateView, DeleteView
from ..models import Post, Comments, Like
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth import get_user_model


User = get_user_model()


class UserPostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name: str = 'feed/user_posts.html'
    context_object_name = 'posts'
    paginate_by: int = 2
    
    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User,username= self.kwargs.get('username'))
        for i in Post.objects.filter(user_name=user):
            if Like.objects.filter(user=self.request.user,post=i):
                liked = i
                context['liked_post'] = liked
        return context
    def get_queryset(self):
        print(self.kwargs)
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(user_name=user).order_by('-created_at')
        