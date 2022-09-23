from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, UpdateView, DeleteView
from ..models import Post, Comments, Like
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from ..forms import NewPostForm, NewCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def post_delete(request,id):
    post = Post.objects.get(pk=id)
    if request.user == post.user_name:
        Post.objects.get(pk=id).delete()
    return redirect('home')