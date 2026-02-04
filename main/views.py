from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "main/home.html"


class AboutView(TemplateView):
    template_name = "main/about.html"


class TasksJanuaryView(TemplateView):
    template_name = "main/tasks_january.html"
