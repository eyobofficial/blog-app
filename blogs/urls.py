from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post-list'),
    path(
        'post/<int:year>/<int:month>/<int:day>/<slug:slug>',
        views.post_detail,
        name='post-detail'
    ),
    path('post/share/<int:pk>', views.post_share, name='post-share'),
]