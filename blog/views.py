from django.http import Http404
from django.shortcuts import render, get_object_or_404

from blog.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, "blog/index.html", {"posts": posts})


def post(request, id):
    post = get_object_or_404(Post, pk=id)

    return render(request, "blog/post.html", {"post": post})
