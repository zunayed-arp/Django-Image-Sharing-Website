from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, UpdateView, DeleteView
from ..models import Post, Comments, Like


class PostListView(ListView):
    model = Post
    template_name: str = 'feed/home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by: int = 2

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            for i in Post.objects.all():
                if Like.objects.filter(user=self.request.user, post=i):
                    liked = i
                    context['liked_post'] = liked
            # liked= [i for i in Post.objects.all() if Like.objects.filter(user=self.request.user,post=i)]
        return context
