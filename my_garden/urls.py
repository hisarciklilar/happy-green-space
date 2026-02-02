from django.urls import path
from .views import (
    PlantListView, PlantDetailView, PlantCreateView,
    GardenPlotListView, GardenPlotCreateView, GardenPlotUpdateView,
    GardenPlotDeleteView,
)

app_name = "my_garden"

urlpatterns = [
    path("plants/", PlantListView.as_view(), name="plant_list"),
    path("plants/new/", PlantCreateView.as_view(), name="plant_create"),
    path("plants/<int:pk>/", PlantDetailView.as_view(), name="plant_detail"),

    path("plots/", GardenPlotListView.as_view(),
         name="gardenplot_list"),
    path("plots/new/", GardenPlotCreateView.as_view(),
         name="gardenplot_create"),
    path("plots/<int:pk>/edit/", GardenPlotUpdateView.as_view(),
         name="gardenplot_update"),
    path("plots/<int:pk>/delete/", GardenPlotDeleteView.as_view(),
         name="gardenplot_delete"),
]
