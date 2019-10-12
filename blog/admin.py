from django.contrib import admin
from .models import Category,Post


class CategoryAdmin(admin.ModelAdmin):
    exclude=('slug',)
admin.site.register(Category,CategoryAdmin)
class PostAdmin(admin.ModelAdmin):
    exclude=('slug',)
    list_display=('title','status','category','created','updated')
    list_filter=('category',)
    search_fields=('title','body')
admin.site.register(Post,PostAdmin)
