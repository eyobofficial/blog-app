from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('posts/', views.post_list, name='post-list'),
    path(
        'post/<int:year>/<int:month>/<int:day>/<slug:slug>',
        views.post_detail,
        name='post-detail'
    ),
]