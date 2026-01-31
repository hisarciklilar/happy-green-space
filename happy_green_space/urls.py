"""
URL configuration for happy_green_space project.
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    # auth
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), 
         name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Application URL
    path('accounts/', include('accounts.urls')),
    path('', include('main.urls'), name='main-url'),
#    path('plants/', include('plants.urls'), name='plants-url'),    
    path('forum/', include('forum.urls'), name='forum-url'),
]

