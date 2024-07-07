from django.urls import path
from aircrafts import views

app_name = "aircrafts"
urlpatterns = [
    path("aircraft-create/", views.AircraftCreateView.as_view(), name='aircraft_create'),
    path("aircraft-detail/<pk>", views.AircraftDetailView.as_view(), name='aircraft_detail'),
    path("aircraft-update/<pk>", views.AircraftUpdateView.as_view(), name='aircraft_update'),
    path("aircraft-delete/<pk>", views.AircraftDeleteView.as_view(), name='aircraft_delete'),
    path("", views.AircraftListView.as_view(), name="aircrafts"),

    path("engine-categories/", views.EngineCategoryListView.as_view(), name="engine_categories"),
    path("engine-category-create/", views.EngineCategoryCreateView.as_view(), name='engine_category_create'),
    path("engine-category-detail/<pk>", views.EngineCategoryDetailView.as_view(), name="engine_category_detail"),
    path("engine-category-update/<pk>", views.EngineCategoryUpdateView.as_view(), name="engine_category_update"),
    path("engine-category-delete/<pk>", views.EngineCategoryDeleteView.as_view(), name="engine_category_delete"),

    path("manufacturers/", views.ManufacturerListView.as_view(), name="manufacturers"),
    path("manufacturer-create/", views.ManufacturerCreateView.as_view(), name='manufacturer_create'),
    path("manufacturer-detail/<pk>", views.ManufacturerDetailView.as_view(), name="manufacturer_detail"),
    path("manufacturer-update/<pk>", views.ManufacturerUpdateView.as_view(), name="manufacturer_update"),
    path("manufacturer-delete/<pk>", views.ManufacturerDeleteView.as_view(), name="manufacturer_delete"),
]
