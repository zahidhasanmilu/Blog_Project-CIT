from django.shortcuts import render
from .models import Blogpost

# Create your views here.


def home(request):
    all_blogs = Blogpost.objects.all()
    src = request.GET.get('searchname')

    if src:
        all_blogs = Blogpost.objects.filter(title__icontains=src)
        
    context = {
        'allBlogs': all_blogs,        
    }

    return render(request, 'home/home.html', context)



def blogDetails(request,title):
    details = Blogpost.objects.get(title=title)

    context = {
        'bDetails': details,
    }
    return  render(request, 'home/blog_details.html', context)