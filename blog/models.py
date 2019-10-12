from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your models here.

class Category(models.Model):
    
    title=models.CharField(max_length=250)
    description=models.CharField(max_length=250)
    seo_title=models.CharField(max_length=60,blank=True,null=True)
    seo_description=models.CharField(max_length=165,blank=True,null=True)
    slug=models.SlugField(max_length=200,unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Category,self).save(*args,**kwargs)
    def __str__(self):
        return self.title



class Post(models.Model):
    STATUS_CHOICES=(
        ('Published','Published'),
        ('Draft','Draft'),
        )
    title=models.CharField(max_length=250)
    
    body=models.TextField()
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    seo_title=models.CharField(max_length=250,blank=True,null=True)
    seo_description=models.CharField(max_length=165,blank=True,null=True)
    slug=models.SlugField(max_length=200,unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,default='Published',choices=STATUS_CHOICES)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Post,self).save(*args,**kwargs)
    def __str__(self):
        return self.title




