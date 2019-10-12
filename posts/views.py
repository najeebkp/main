from django.shortcuts import render
from blog.models import Post

# Create your views here.
from django.http import HttpResponse

def index(request):
    data = Post.objects.all()
    return render (request,'blog/index.html',{'Post' : data})
    
