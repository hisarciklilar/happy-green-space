from django.urls import path
from .views import HomeView, AboutView, TasksJanuaryView

app_name = 'main'

urlpatterns = [
path("", HomeView.as_view(), name="home"),
path("about/", AboutView.as_view(), name="about"),
path("tasks-january/", TasksJanuaryView.as_view(), name="tasks_january"),
]

