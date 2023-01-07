from django.shortcuts import render, get_object_or_404

from .models import Blogpost


def all_blogs(request):
    posts = Blogpost.objects.order_by('-created_at')
    return render(request, 'blog/all_blogs.html', {'posts': posts})


def detail(request, blog_id):
    blog = get_object_or_404(Blogpost, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
