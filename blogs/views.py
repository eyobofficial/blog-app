from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post


class PostList(ListView):
    model = Post

    def get_queryset(self, *args, **kwargs):
        return Post.published.all()


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(
        Post,
        status='published',
        slug=slug,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(request, 'blogs/post_detail.html', {
        'post': post,
    })
