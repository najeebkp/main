from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

from django.views import generic
from django.views.generic import TemplateView,ListView
# Create your views here.
from login.models import Profile
from .forms import PostForm
from .models import Post
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def createpost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.userm=Profile.first_name
                post.save()
                return render(request,"blog/index.html",{'content':post.content})
            
                post.save()
                #return render(request, 'blog/success.html')  

        else:
                return render(request,'blog/error.html')
def show(request):
         if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.userm=Profile.first_name
                post.save()
                    
                data = Post.objects.all()
                return redirect('index')
                #return render(request,"blog/index.html")
        #else:
               # return render(request,'blog/error.html')

@login_required
def index(request):
    data = Post.objects.all()
    template = 'blog/index.html'
    return render(request, template,{'entries' : data})

def card(request):
    data = Post.objects.all()
    return render(request, 'blog/card.html',{'Post' : data})



















                
