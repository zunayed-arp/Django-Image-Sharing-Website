from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, UpdateView, DeleteView
from ..models import Post, Comments, Like
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from ..forms import NewPostForm, NewCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def search_posts(request):
    query = request.GET.get('p')
    objec_list = Post.objects.filter(tags___icontains=query)
    liked = [i for i in objec_list if Like.objects.filter(
        user=request.user, post=i)]

    context = {
        'posts': objec_list,
        'liked_post': liked
    }
    return render(request, 'feed/search_posts.html', context)
