from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Plant


# PLANT VIEWS

class PlantListView(ListView):
    """Display all plants in the catalogue."""
    model = Plant
    template_name = "my_garden/plant_list.html"
    context_object_name = "plants"
    # ordering = ['name']
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