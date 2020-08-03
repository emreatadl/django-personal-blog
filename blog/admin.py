from .models import Post, Comment, Category
from material.admin.options import MaterialModelAdmin
from material.admin.sites import site


site.site_header = 'Admin Dashboard'
site.site_title = 'Emre Atadil Blog'
site.index_title = 'Admin Dashboard'


class PostAdmin(MaterialModelAdmin):
    list_display = ('title', 'slug', 'created_on', 'author', 'status')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(MaterialModelAdmin):
    list_display = ('author', 'comment', 'email', 'approved_comment', 'created_date')


site.register(Post, PostAdmin)
site.register(Comment, CommentAdmin)
site.register(Category)