from django.urls import path
from .views import PostList, PostDetail
#from . import views
app_name = 'forum'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
#    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]