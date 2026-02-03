from django.urls import path
from .views import (
    MyGardenDashboardView,
    PlantListView, PlantDetailView, PlantCreateView,
    GardenPlotListView, GardenPlotCreateView, GardenPlotUpdateView,
    GardenPlotDeleteView, GardenPlotDetailView,
    PlantLogListView, PlantLogCreateView, PlantLogUpdateView,
    PlantLogDeleteView,
)

app_name = "my_garden"

urlpatterns = [
     path("", MyGardenDashboardView.as_view(), name="dashboard"),

     path("plants/", PlantListView.as_view(), name="plant_list"),
     path("plants/new/", PlantCreateView.as_view(), name="plant_create"),
     path("plants/<int:pk>/", PlantDetailView.as_view(), name="plant_detail"),

     path("plots/", GardenPlotListView.as_view(),
         name="gardenplot_list"),
     path("plots/<int:pk>/", GardenPlotDetailView.as_view(),
          name="gardenplot_detail"),
     path("plots/new/", GardenPlotCreateView.as_view(),
         name="gardenplot_create"),
     path("plots/<int:pk>/edit/", GardenPlotUpdateView.as_view(),
         name="gardenplot_update"),
     path("plots/<int:pk>/delete/", GardenPlotDeleteView.as_view(),
         name="gardenplot_delete"),

     path("logs/", PlantLogListView.as_view(),
         name="plantlog_list"),
     path("logs/new/", PlantLogCreateView.as_view(),
         name="plantlog_create"),
     path("logs/<int:pk>/edit/", PlantLogUpdateView.as_view(),
         name="plantlog_update"),
     path("logs/<int:pk>/delete/", PlantLogDeleteView.as_view(),
         name="plantlog_delete"),
]
