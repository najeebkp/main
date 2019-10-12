
from django.conf.urls import include,url
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views

from login.forms import LoginForm
from login.views import *
from django.urls import path 
from blog import views as vs

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.post_list, name='post_list'),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #path('post/new/', vs.post_new, name='post_new'),
    url(r'', include('login.urls')),
    url(r'posts', include('posts.urls')),
    url(r'^login$', views.LoginView.as_view(),name='login' ),
    url(r'^login/$', views.LoginView.as_view(),{'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^logout/$', views.LogoutView.as_view(),{'next_page': '/login/'}),
    url(r'^signup/$', signup,  name='signup'),
    url(r'^blog/', include('blog.urls')),
]
