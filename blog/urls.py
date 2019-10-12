from django.conf.urls import url,include
from django.urls import path
from .views import post_list,post_detail,category_detail,new_post,post_list_admin,edit_post,delete_post,change_password
app_name = 'blog'
urlpatterns = [
    
    url(r'^post-list/$',post_list,name='post_list'),
    url(r'^post-detail/(?P<slug>[-\w]+)/$',post_detail,name='post_detail'),
    url(r'^category-detail/(?P<slug>[-\w]+)/$',category_detail,name='category_detail'),
    #custom_admin
    url(r'^new-post/$',new_post,name='new_post'),
    url(r'^admin-post/$',post_list_admin,name='post_list_admin'),
    url(r'^edit-post/(?P<pk>\d+)/$',edit_post,name='edit_post'),
    url(r'^delete-post/(?P<pk>\d+)/$',delete_post,name='delete_post'),
    url(r'^password/$',change_password, name='change_password'),
]
