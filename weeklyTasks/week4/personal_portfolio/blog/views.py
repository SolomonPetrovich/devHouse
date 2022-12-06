from django.shortcuts import render
from .models import *

def all_blogs(requests):
    blogs = Blog.objects.order_by('-date')
    context = {
        'blogs': blogs
    }
    return render(requests, template_name='blog/all_blogs.html', context=context)

def blog_detail(request, pk):
    blog = Blog.objects.get(id=pk)
    context = {
        'blog': blog
    }
    return render(request, 'blog/blog_detail.html', context)