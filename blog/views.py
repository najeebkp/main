from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from .models import Post,Category
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def post_list(request):
    template='blog/post_list.html'
    
    objects_list=Post.objects.filter(status='Published')
    paginator=Paginator(objects_list,6)
    page=request.GET.get('page')
    try:
        items=paginator.page(page)
    except PageNotAnInteger:
        items=paginator.page(1)
    except EmptyPage:
        items=paginator.page(paginator.num_pages)
    
    context={
        'objects_list':objects_list,
        'items':items,
        
        }
    return render(request,template,context)

def post_detail(request,slug):
    template='blog/post_detail.html'

    post=get_object_or_404(Post,slug=slug)
    objects_list=Post.objects.all()
    context={
        'post':post,
        }
    return render(request,template,context)
def category_detail(request,slug):
    template='blog/category_detail.html'
    category=get_object_or_404(Category,slug=slug)
    post=Post.objects.filter(category=category,status='Published')

    context={
        'category':category,
        'post':post,
        }
    return render(request,template,context)

def new_post(request):
    template='blog/new_post.html'
    form=PostForm(request.POST or None)
    
    try:
        if form.is_valid():
            form.save()
            messages.success(request,'posted successfully!!!')
    except Exception as e:
        form=PostForm()
        messages.warning(request,"posted failed!!!. Error:{}".format(e))
    context={
        'form':form,
        
        }
    return render(request,template,context)

def post_list_admin(request):
    template='blog/post_list_admin.html'
    

    post=Post.objects.all()

    paginator=Paginator(post,5)
    page=request.GET.get('page')
    try:
        items=paginator.page(page)
    except PageNotAnInteger:
        items=paginator.page(1)
    except EmptyPage:
        items=paginator.page(paginator.num_pages)
        
    context={
        'post':post,
        'items':items,
            }
    return render(request,template,context)    






def edit_post(request,pk):
    template='blog/new_post.html'

    post=get_object_or_404(Post,pk=pk)

    if request.method == "POST":
        form= PostForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your post has been updated')
        except Exception as e:
            messages.warning(request, 'Your post not saved!! error:{}'.format(e))
    else:
        form=PostForm(instance=post)
    context={
        'form':form,
        'post':post,
        }
    return render(request,template,context)

def delete_post(request,pk):
    template='blog/new_post.html'

    post=get_object_or_404(Post,pk=pk)

    try:
        if request.method== "POST":
            form=PostForm(request.POST, instance=post)
            post.delete()
            messages.success(request, 'Your are successfully deleted the post')
        else:
            form=PostForm(instance=post)
    except Exception as e:
        messages.warning(request,'the post couldnot be deleted!! error:{}'.format(e))
        
    context={
        'form':form,
        'post':post,
        }
    return render(request,template,context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return render(request,'blog/change_password.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'blog/change_password.html', {
        'form': form
    })
