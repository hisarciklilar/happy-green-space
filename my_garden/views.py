from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Plant, GardenPlot, PlantLog


# PLANT VIEWS

class PlantListView(generic.ListView):
    """Display all plants in the catalogue."""
    model = Plant
    template_name = "my_garden/plant_list.html"
    context_object_name = "plants"
    ordering = ['name']
    paginate_by = 20


class PlantDetailView(generic.DetailView):
    """Display details about a specific plant."""
    model = Plant
    template_name = "my_garden/plant_detail.html"
    context_object_name = "plant"


class PlantCreateView(LoginRequiredMixin, generic.CreateView):
    """Allow users to suggest a new plant to the catalogue."""
    model = Plant
    template_name = "my_garden/plant_form.html"
    fields = [
        'name',
        'scientific_name',
        'category',
        'use_type',
        'is_edible',
        'height_cm_min',
        'height_cm_max',
        'spread_cm_min',
        'spread_cm_max',
        'spacing_cm',
        'sun_requirement',
        'description'
        ]
    success_url = reverse_lazy('my_garden:plant_list')

    def form_valid(self, form):
        form.instance.suggested_by = self.request.user
        return super().form_valid(form)

# END PLANT VIEWS

# GARDEN PLOT VIEWS

class GardenPlotListView(LoginRequiredMixin, generic.ListView):
    model = GardenPlot
    template_name = "my_garden/gardenplot_list.html"
    context_object_name = "plots"

    def get_queryset(self):
        return GardenPlot.objects.filter(
            owner=self.request.user
            ).order_by("name")


class GardenPlotCreateView(LoginRequiredMixin, generic.CreateView):
    model = GardenPlot
    fields = ["name", "description"]
    template_name = "my_garden/gardenplot_form.html"
    success_url = reverse_lazy("my_garden:gardenplot_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class GardenPlotUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = GardenPlot
    fields = ["name", "description"]
    template_name = "my_garden/gardenplot_form.html"
    success_url = reverse_lazy("my_garden:gardenplot_list")

    def get_queryset(self):
        return GardenPlot.objects.filter(owner=self.request.user)


class GardenPlotDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = GardenPlot
    template_name = "my_garden/gardenplot_confirm_delete.html"
    success_url = reverse_lazy("my_garden:gardenplot_list")

    def get_queryset(self):
        return GardenPlot.objects.filter(owner=self.request.user)

# END GARDEN PLOT VIEWS

# PLANT LOG VIEWS


class PlantLogListView(LoginRequiredMixin, generic.ListView):
    model = PlantLog
    template_name = "my_garden/plantlog_list.html"
    context_object_name = "logs"
    ordering = ["-date_planted"]

    def get_queryset(self):
        return PlantLog.objects.filter(owner=self.request.user)\
            .select_related("plant", "plot")\
            .order_by("-date_planted", "-created_on")


class PlantLogCreateView(LoginRequiredMixin, generic.CreateView):
    model = PlantLog
    fields = ["plant", "plot", "date_planted",
              "date_harvested", "status", "notes"]
    template_name = "my_garden/plantlog_form.html"
    success_url = reverse_lazy("my_garden:plantlog_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["plot"].queryset = GardenPlot.objects\
            .filter(owner=self.request.user).order_by("name")
        plot_id = self.request.GET.get("plot")
        if plot_id:
            try:
                form.fields["plot"].initial = GardenPlot.objects\
                    .get(owner=self.request.user, pk=plot_id)
            except GardenPlot.DoesNotExist:
                pass
        return form


class PlantLogUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = PlantLog
    fields = ["plant", "plot", "date_planted",
              "date_harvested", "status", "notes"]
    template_name = "my_garden/plantlog_form.html"
    success_url = reverse_lazy("my_garden:plantlog_list")

    def get_queryset(self):
        return PlantLog.objects.filter(owner=self.request.user)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["plot"].queryset = (
            GardenPlot.objects.filter(owner=self.request.user).order_by("name")
        )
        return form


class PlantLogDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = PlantLog
    template_name = "my_garden/plantlog_confirm_delete.html"
    success_url = reverse_lazy("my_garden:plantlog_list")

    def get_queryset(self):
        return PlantLog.objects.filter(owner=self.request.user)

# END PLANT LOG VIEWS

# PLOT DETAIL VIEW


class GardenPlotDetailView(LoginRequiredMixin, generic.DetailView):
    model = GardenPlot
    template_name = "my_garden/gardenplot_detail.html"
    context_object_name = "plot"

    def get_queryset(self):
        return GardenPlot.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logs"] = (
            PlantLog.objects.filter(owner=self.request.user, plot=self.object)
            .select_related("plant", "plot")
            .order_by("-date_planted", "-created_on")
        )
        return context
    
# END PLOT DETAIL VIEW

# MY GARDEN DASHBOARD VIEW


class MyGardenDashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = "my_garden/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        plots_qs = GardenPlot.objects.filter(owner=self.request.user)
        logs_qs = (
            PlantLog.objects.filter(owner=self.request.user)
            .select_related("plant", "plot")
            .order_by("-date_planted", "-created_on")
        )

        # context["plots"] = GardenPlot.objects.filter(owner=self.request.user)
        context["plot_count"] = plots_qs.count()
        context["log_count"] = logs_qs.count()
        context["recent_plots"] = plots_qs.order_by("-created_on")[:5]
        context["recent_logs"] = logs_qs[:5]
        context["active_lgs"] = logs_qs.exclude(
            status__in=['harvested', 'failed']
            )[:5]

        return context