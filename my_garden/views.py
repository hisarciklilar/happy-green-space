from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Plant, GardenPlot


# PLANT VIEWS

class PlantListView(ListView):
    """Display all plants in the catalogue."""
    model = Plant
    template_name = "my_garden/plant_list.html"
    context_object_name = "plants"
    ordering = ['name']
    paginate_by = 20


class PlantDetailView(DetailView):
    """Display details about a specific plant."""
    model = Plant
    template_name = "my_garden/plant_detail.html"
    context_object_name = "plant"


class PlantCreateView(LoginRequiredMixin, CreateView):
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

class GardenPlotListView(LoginRequiredMixin, ListView):
    model = GardenPlot
    template_name = "my_garden/gardenplot_list.html"
    context_object_name = "plots"

    def get_queryset(self):
        return GardenPlot.objects.filter(
            owner=self.request.user
            ).order_by("name")


class GardenPlotCreateView(LoginRequiredMixin, CreateView):
    model = GardenPlot
    fields = ["name", "description"]
    template_name = "my_garden/gardenplot_form.html"
    success_url = reverse_lazy("my_garden:gardenplot_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class GardenPlotUpdateView(LoginRequiredMixin, UpdateView):
    model = GardenPlot
    fields = ["name", "description"]
    template_name = "my_garden/gardenplot_form.html"
    success_url = reverse_lazy("my_garden:gardenplot_list")

    def get_queryset(self):
        return GardenPlot.objects.filter(owner=self.request.user)


class GardenPlotDeleteView(LoginRequiredMixin, DeleteView):
    model = GardenPlot
    template_name = "my_garden/gardenplot_confirm_delete.html"
    success_url = reverse_lazy("my_garden:gardenplot_list")

    def get_queryset(self):
        return GardenPlot.objects.filter(owner=self.request.user)

# END GARDEN PLOT VIEWS
