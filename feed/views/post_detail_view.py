from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, UpdateView, DeleteView
from ..models import Post, Comments, Like
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from ..forms import NewPostForm, NewCommentForm
from django.contrib.auth.decorators import login_required

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    user = request.user
    is_liked = Like.objects.filter(user=user, post=post)
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.post = post
            data.username = user
            data.save()
            return redirect('post_detail', pk=id)
    else:
        form = NewPostForm()
    return render(request, 'feed/post_detail.html', {'post': post, 'is_liked': is_liked, 'form': form})
