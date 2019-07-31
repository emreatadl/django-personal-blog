from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from blog.forms import CommentForm
from django.db import connection


def index(request):
    queryset_index = Post.objects.filter(status=2).order_by('-created_on')
    return render(request, 'index.html',
                  {
                      'queryset_index': queryset_index,
                  }
                  )


def about_me(request):
    return render(request, 'about.html')


def Postlist(request):
    queryset = Post.objects.filter(status=2).order_by('-created_on')
    paginator_ready = Paginator(queryset, 20)
    page = request.GET.get('page')
    post_page = paginator_ready.get_page(page)
    return render(request, 'blog.html',
                  {
                      'queryset': queryset,
                      'post_page': post_page,
                  }
                  )


# def PostDetail(request, slug):
#     post = Post.objects.filter(status=2, slug=slug)
#     comment = Comment.objects.get(approved_comment=True, post=post)
#     print(comment)
#     comment_count = Comment.objects.count()
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.Post = post
#             new_comment.save()
#             return redirect('blog:post_detail', slug)
#
#     else:
#         comment_form = CommentForm()
#
#     return render(request, 'single-blog.html',
#                   {
#                       'post_details': post,
#                       'comments': comment,
#                       'comment_form': comment_form,
#                       'comment_count': comment_count
#                   }
#                   )



def PostDetail(request, slug):
    post = Post.objects.get(status=2, slug=slug)  # notice the get instead of filter
    comment = Comment.objects.filter(approved_comment=True, post=post)
    print(post)
    comment_count = comment.count()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.Post = post
            new_comment.save()
            return redirect('blog:post_detail', slug)

    else:
        comment_form = CommentForm()

    return render(request, 'single-blog.html',
                  {
                      'post_details': post,
                      'comments': comment,
                      'comment_form': comment_form,
                      'comment_count': comment_count
                  }
                  )
