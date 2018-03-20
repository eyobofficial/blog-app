from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post
from .forms import EmailPostForm


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


def post_share(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form_class = EmailPostForm
    sent = False

    if request.method == 'POST':
        form = form_class(request.POST)

        if form.is_valid():
            # Retrieve validated fields
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            to = form.cleaned_data['to']
            comment = form.cleaned_data.get('comment', '')

            post_absolute_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you a blog post'.format(name, email)
            message = '''Read <strong>{}</strong>
                         {}
                         {}
                      '''.format(post.title, post_absolute_url, comment)
            send_mail(subject, message, 'myemail@gmail.com', [to, ])
            sent = True
    else:
        form = form_class()
    return render(request, 'blogs/post_share.html', {
        'form': form,
        'post': post,
        'sent': sent,
    })
