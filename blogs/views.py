from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    post_list = Post.published.all()
    return render(request, 'blogs/post_list.html', {
        'post_list': post_list,
    })


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(request, 'blogs/post_detail.html', {
        'post': post,
    })
