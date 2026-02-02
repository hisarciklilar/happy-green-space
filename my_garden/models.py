from django.db import models
from django.contrib.auth.models import User


class Plant(models.Model):
    CATEGORY_CHOICES = [
        ('vegetable', 'Vegetable'),
        ('herb', 'Herb'),
        ('flower', 'Flower'),
        ('fruit', 'Fruit'),
        ('shrub', 'Shrub'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=150, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    description = models.TextField(blank=True)
    suggested_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='suggested_plants'
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class GardenPlot(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='garden_plots')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        unique_together = ('owner', 'name')

    def __str__(self):
        return f"{self.name} ({self.owner.username})"


class PlantLog(models.Model):
    STATUS_CHOICES = [
        ('planted', 'Planted'),
        ('growing', 'Growing'),
        ('harvested', 'Harvested'),
        ('failed', 'Failed'),
        ('partial', 'Partial Success'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plant_logs')
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='logs')
    plot = models.ForeignKey(
        GardenPlot, on_delete=models.SET_NULL, null=True, blank=True, related_name='plant_logs'
    )
    date_planted = models.DateField(null=True, blank=True)
    date_harvested = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planted')
    notes = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_planted']

    def __str__(self):
        return f"{self.plant.name} — {self.owner.username} ({self.status})"


class WishList(models.Model):
    SEASON_CHOICES = [
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('autumn', 'Autumn'),
        ('winter', 'Winter'),
        ('any', 'Any Season'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wish_list')
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='wishlisted_by')
    target_season = models.CharField(max_length=10, choices=SEASON_CHOICES, default='any')
    notes = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['plant__name']
        # A user shouldn't be able to wishlist the same plant twice
        unique_together = ('owner', 'plant')

    def __str__(self):
        return f"{self.plant.name} — {self.owner.username} (wishlist)"


class ToDoItem(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_do_items')
    title = models.CharField(max_length=150)
    plant = models.ForeignKey(
        Plant, on_delete=models.SET_NULL, null=True, blank=True, related_name='to_do_items'
    )
    plot = models.ForeignKey(
        GardenPlot, on_delete=models.SET_NULL, null=True, blank=True, related_name='to_do_items'
    )
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    completed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-priority', 'due_date']

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.title} [{status}]"