from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'zunayed',
        'title': 'Blog Post 1',
        'content':'First post content',
        'date_posted':'December 11,2020'
    },
    {
        'author': 'Am Raul',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'December 12,2020'
    }
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)


def about(request):

    return render(request,'blog/about.html')
    #return HttpResponse('<h1> Blog About</h1>')

# Create your views here.
