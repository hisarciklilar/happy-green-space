from django.urls import path
from .views import (
    PlantListView,
    PlantDetailView,
    PlantCreateView,
)

app_name = "my_garden"

urlpatterns = [
    path("plants/", PlantListView.as_view(), name="plant_list"),
    path("plants/new/", PlantCreateView.as_view(), name="plant_create"),
    path("plants/<int:pk>/", PlantDetailView.as_view(), name="plant_detail"),
]
