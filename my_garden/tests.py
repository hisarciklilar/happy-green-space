from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.db import IntegrityError
from my_garden.models import Plant, GardenPlot, PlantLog
from my_garden.views import PlantDetailView


class MyGardenURLTests(TestCase):
    def test_dashboard_url_resolves(self):
        url = reverse("my_garden:dashboard")
        match = resolve(url)
        self.assertIsNotNone(match.func)

    def test_plant_list_url_resolves(self):
        url = reverse("my_garden:plant_list")
        match = resolve(url)
        self.assertIsNotNone(match.func)

    def test_plant_detail_url_resolves(self):
        plant = Plant.objects.create(name="Test plant")
        url = reverse("my_garden:plant_detail", args=[plant.pk])
        self.assertEqual(resolve(url).func.view_class, PlantDetailView)

    def test_gardenplot_list_url_resolves(self):
        url = reverse("my_garden:plant_list")
        match = resolve(url)
        self.assertIsNotNone(match.func)

    def test_gardenplot_detail_url_resolves(self):
        url = reverse("my_garden:plant_list")
        match = resolve(url)
        self.assertIsNotNone(match.func)

    def test_plantlog_list_url_resolves(self):
        url = reverse("my_garden:plant_list")
        match = resolve(url)
        self.assertIsNotNone(match.func)

    def test_plantlog_detail_url_resolves(self):
        url = reverse("my_garden:plant_list")
        match = resolve(url)
        self.assertIsNotNone(match.func)


class MyGardenModelTests(TestCase):
    def setUp(self):
        self.alice = User.objects.create_user(username="alice", password="pass12345")
        self.bob = User.objects.create_user(username="bob", password="pass12345")

        self.plant = Plant.objects.create(
            name="Field Maple",
            scientific_name="Acer campestre",
            category="ornamental_tree",
            sun_requirement="full_sun",
        )

        self.plot = GardenPlot.objects.create(
            owner=self.alice,
            name="Plot A",
            description="My first plot",
        )

    def test_plant_str(self):
        self.assertEqual(str(self.plant), "Field Maple")

    def test_gardenplot_str(self):
        self.assertIn("Plot A", str(self.plot))
        self.assertIn("alice", str(self.plot))

    def test_gardenplot_unique_per_owner(self):
        GardenPlot.objects.create(owner=self.bob, name="Plot A")

        with self.assertRaises(IntegrityError):
            GardenPlot.objects.create(owner=self.alice, name="Plot A")

    def test_plantlog_str(self):
        log = PlantLog.objects.create(owner=self.alice, plant=self.plant, plot=self.plot, status="planted")
        s = str(log)
        self.assertIn("Field Maple", s)
        self.assertIn("alice", s)
        self.assertIn("planted", s)


class MyGardenViewTests(TestCase):
    def setUp(self):
        self.alice = User.objects.create_user(username="alice", password="pass12345")
        self.bob = User.objects.create_user(username="bob", password="pass12345")

        self.plant = Plant.objects.create(
            name="Rosemary",
            scientific_name="Salvia rosmarinus",
            category="herb",
            sun_requirement="full_sun",
        )

        self.plot_alice = GardenPlot.objects.create(owner=self.alice, name="Alice Plot")
        self.plot_bob = GardenPlot.objects.create(owner=self.bob, name="Bob Plot")

        self.log_alice = PlantLog.objects.create(
            owner=self.alice,
            plant=self.plant,
            plot=self.plot_alice,
            status="growing",
            notes="Alice note",
        )
        self.log_bob = PlantLog.objects.create(
            owner=self.bob,
            plant=self.plant,
            plot=self.plot_bob,
            status="planted",
            notes="Bob note",
        )

    # Auth smoke tests 

    def test_dashboard_redirects_when_logged_out(self):
        response = self.client.get(reverse("my_garden:dashboard"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", response.url)

    def test_plots_list_redirects_when_logged_out(self):
        response = self.client.get(reverse("my_garden:gardenplot_list"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", response.url)

    def test_logs_list_redirects_when_logged_out(self):
        response = self.client.get(reverse("my_garden:plantlog_list"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", response.url)

    def test_dashboard_loads_when_logged_in(self):
        self.client.login(username="alice", password="pass12345")
        response = self.client.get(reverse("my_garden:dashboard"))
        self.assertEqual(response.status_code, 200)

    # Plant pages (public)

    def test_plant_list_loads(self):
        response = self.client.get(reverse("my_garden:plant_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rosemary")

    def test_plant_detail_loads(self):
        response = self.client.get(reverse("my_garden:plant_detail", args=[self.plant.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rosemary")

    # Ownership filtering

    def test_plot_list_shows_only_logged_in_users_plots(self):
        self.client.login(username="alice", password="pass12345")
        response = self.client.get(reverse("my_garden:gardenplot_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Alice Plot")
        self.assertNotContains(response, "Bob Plot")

    def test_log_list_shows_only_logged_in_users_logs(self):
        self.client.login(username="alice", password="pass12345")
        response = self.client.get(reverse("my_garden:plantlog_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Alice note")
        self.assertNotContains(response, "Bob note")

    def test_plot_detail_denies_access_to_other_users_plot(self):
        self.client.login(username="alice", password="pass12345")
        response = self.client.get(reverse("my_garden:gardenplot_detail", args=[self.plot_bob.pk]))

        self.assertIn(response.status_code, (403, 404))

    def test_log_update_denies_access_to_other_users_log(self):
        self.client.login(username="alice", password="pass12345")
        response = self.client.get(reverse("my_garden:plantlog_update", args=[self.log_bob.pk]))
        self.assertIn(response.status_code, (403, 404))
