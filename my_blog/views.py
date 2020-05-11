from django.shortcuts import render, get_object_or_404
from .models import MyBlogs


def Blog(request):
    myblog = MyBlogs.objects.all()
    context = {
        'blogs': myblog
    }

    return render(request, 'blog.html', context)


def Details(request, blog_id):
    details = get_object_or_404(MyBlogs, pk=blog_id)
    context = {
        'detail': details
    }
    return render(request, 'blog_details.html', context)
