from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, UpdateView, DeleteView
from ..models import Post, Comments, Like
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from ..forms import NewPostForm, NewCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def create_post(request):
    username = request.user
    if request.method == 'POST':
        data = request.POST,
        files = request.FILES
        form = NewPostForm(data=data, files=files)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_name = username
            data.save()
            messages.successs(request, f'Posted Successfullly')
            return redirect('home')
    else:
        form = NewPostForm
    return render(request, 'feed/create_post.html', {'form': form})
