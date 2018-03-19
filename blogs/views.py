from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    post_list = Post.published.all()
    return render(request, 'blogs/post_list.html', {
        'post_list': post_list,
    })


def post_detail(request, year, month, date, slug):
    post = get_object_or_404(
        Post,
        year=year,
        month=month,
        date=date,
        slug=slug
    )
    return render(request, 'blogs/post_detail.html', {
        'post': post,
    })
