from django.shortcuts import render
from django.views import generic
from django.utils.text import slugify
from django.contrib.auth.models import User

from .models import Post, Reply


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
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['replies'] = self.object.replies.all().order_by('created_on')
        return context

class PostCreate(generic.CreateView):
    model = Post
    template_name = "forum/post_form.html"
    fields = ['title', 'content']

    def form_valid(self, form):
        fallback_user = User.objects.filter(is_superuser=True).first()
        if fallback_user is None:
            fallback_user = User.objects.first()
#        form.instance.author = self.request.user
        form.instance.author = fallback_user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)    
