from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
#    queryset = Post.objects.all()
    template_name = "forum/post_list.html"
    context_object_name = "posts"
    ordering = ['-created_on']
    paginate_by = 10

class PostDetail(generic.DetailView):
    model = Post
    template_name = "forum/post_detail.html"
    context_object_name = "post"