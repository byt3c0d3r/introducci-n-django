from django.contrib import admin

from .models import Post
# Register your models here.

# importando los modelos para que aparezcan en la página admin

class PostView(admin.ModelAdmin):
    list_display = ('title','content')


admin.site.register(Post, PostView)
