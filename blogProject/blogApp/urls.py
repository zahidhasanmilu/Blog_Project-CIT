from django.urls import path

from .import views


urlpatterns = [
   path('', views.home, name='home'),
   path('blog_details/<str:title>/', views.blogDetails, name='blogdetails'),
   path('create-blog-from-here/', views.createBlog, name='createblog'),
   path('updateBlog/<id>/', views.updateBlog, name='updateblog')
]