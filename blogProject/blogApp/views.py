from django.shortcuts import render, redirect
from django.contrib import messages


from .models import Blogpost


# Create your views here.


def home(request):
    all_blogs = Blogpost.objects.all()
    src = request.GET.get('searchname')

    if src:
        all_blogs = Blogpost.objects.filter(title__icontains=src)
        
    context = {
        'allBlogs': all_blogs,
        'src':src,        
    }
    return render(request, 'home/home.html', context)


def createBlog(request):
    if request.method =='POST':
        title = request.POST['titles']
        description = request.POST['descriptions']
        image = request.FILES.get('image')

        obj = Blogpost.objects.create(
            title = title, description=description, image=image
        )
        obj.save()
        messages.success(request, 'Profile Created')
        return redirect('home')

    return render(request, 'home/createblog.html')



def updateBlog(request,title):
    return render(request,'home/updateblog.html')



def blogDetails(request,title):
    details = Blogpost.objects.get(title=title)

    context = {
        'bDetails': details,
    }
    return  render(request, 'home/blog_details.html', context)
