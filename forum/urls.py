from django.urls import path
from .views import PostList, PostDetail, PostCreate, ReplyCreate, PostUpdate
#from . import views
app_name = 'forum'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('new/', PostCreate.as_view(), name='post_create'),
    path('<slug:slug>/edit/', PostUpdate.as_view(), name='post_update'),
    path('<slug:slug>/reply/', ReplyCreate.as_view(), name='reply_create'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]