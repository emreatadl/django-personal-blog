import base64
import datetime
import itertools
import json
import sys

import requests
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect
from .models import Post, Comment, Category
from .forms import CommentForm
from django.db import connection


def index(request):
    queryset_index = Post.objects.filter(status=2).order_by('-created_on')[:3]
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


def PostDetail(request, slug):
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


def category_list(request, slug):
    categories = Category.objects.get(slug=slug, )
    post_category = Post.objects.filter(category_id=categories)
    return render(request, 'category.html',
                  {
                      'post_category': post_category,
                      'categories': categories,
                  }
                  )
