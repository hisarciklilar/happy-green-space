from django.urls import path
from .views import (
    PostList, 
    PostDetail, 
    PostCreate, 
    PostUpdate, 
    PostDelete,
    ReplyDelete,
    ReplyUpdate,
    ReplyCreate 
)
#from . import views
app_name = 'forum'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('new/', PostCreate.as_view(), name='post_create'),
    path('<slug:slug>/edit/', PostUpdate.as_view(), name='post_update'),
    path('<slug:slug>/delete/', PostDelete.as_view(), name='post_delete'),
    path('<slug:slug>/reply/', ReplyCreate.as_view(), name='reply_create'),
    path('reply/<int:pk>/edit/', ReplyUpdate.as_view(), name='reply_update'),
    path('reply/<int:pk>/delete/', ReplyDelete.as_view(), name='reply_delete'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),

]