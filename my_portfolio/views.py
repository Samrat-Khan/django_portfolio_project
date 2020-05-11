from django.shortcuts import render
from .models import MyProjects


def Home(request):
    myproject = MyProjects.objects.all()
    context = {
        "projects": myproject
    }
    return render(request, 'index.html', context)
