from django.urls import path
from .views import PostList, PostDetail, PostCreate
#from . import views
app_name = 'forum'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('new/', PostCreate.as_view(), name='post_create'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]