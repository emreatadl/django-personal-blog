from .models import Post, Comment, Category
from material.admin import admin
from material.admin.options import MaterialModelAdmin
from material.admin.sites import site


site.site_header = 'EA Admin Dashboard'
site.site_title = 'Emre Atadil'
site.index_title = 'Admin Dashboard'


class PostAdmin(MaterialModelAdmin):
    list_display = ('title', 'slug', 'created_on', 'author', 'status')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(MaterialModelAdmin):
    list_display = ('author', 'comment', 'approved_comment', 'created_date')


site.register(Post, PostAdmin)
site.register(Comment, CommentAdmin)
site.register(Category)