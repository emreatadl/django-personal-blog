import requests
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect, render_to_response
from .models import Post, Comment, Category
from .forms import CommentForm


def index(request):
    queryset_index = Post.objects.filter(status=2).order_by('-created_on')[:4]
    return render(request, 'index.html',
                  {
                      'queryset_index': queryset_index,
                  }
                  )


def about_me(request):
    try:
        return render(request, 'about.html')
    except:
        return render(request, 'error_pages.html')


def Postlist(request):
    try:
        queryset = Post.objects.filter(status=2).order_by('-created_on')
        paginator_ready = Paginator(queryset, 20)
        page = request.GET.get('page')
        post_page = paginator_ready.get_page(page)
        category_filter = Category.objects.filter()
        return render(request, 'blog.html',
                      {
                          'queryset': queryset,
                          'post_page': post_page,
                          'category_filter': category_filter,
                      }
                      )
    except:
        return render(request, 'error_pages.html')


def PostDetail(request, slug):
    try:
        post = Post.objects.get(status=2, slug=slug)  # notice the get instead of filter
        comments = post.comments.filter(approved_comment=True, post_id=post.id)
        last_content = Post.objects.filter(status=2).order_by('-created_on')[:3]
        comment_count = comments.count()
        category_filter = Category.objects.filter()
        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.save()
                return redirect('blog:post_detail', slug)

        else:
            comment_form = CommentForm()

        return render(request, 'single-blog.html',
                      {
                          'post_details': post,
                          'last_content': last_content,
                          'comments': comments,
                          'comment_form': comment_form,
                          'comment_count': comment_count,
                          'category_filter': category_filter
                      }
                      )
    except:
        return render(request, 'error_pages.html')


def category_list(request, slug):
    try:
        categories = Category.objects.get(slug=slug, )
        post_category = Post.objects.filter(category_id=categories)
        return render(request, 'category.html',
                      {
                          'post_category': post_category,
                          'categories': categories,
                      }
                      )
    except:
        return render(request, 'error_pages.html')
