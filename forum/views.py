from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    # model = Post
    queryset = Post.objects.all()
    
    template_name = "forum/forum_home.html"
    # paginate_by = 10