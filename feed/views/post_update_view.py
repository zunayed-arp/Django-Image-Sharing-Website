from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, UpdateView, DeleteView
from ..models import Post, Comments, Like
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from ..forms import NewPostForm, NewCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['description','pic','tags']
    template_name = 'feed/create_post.html'
    
    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user_name:
            return True
        return False
    
    