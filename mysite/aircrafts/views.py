from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from aircrafts import models
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class ManufacturerListView(LoginRequiredMixin, ListView):
    model = models.Manufacturer
    paginate_by = 100


class ManufacturerCreateView(LoginRequiredMixin, CreateView):
    model = models.Manufacturer
    fields = "__all__"
    success_url = "/aircrafts/manufacturers/"


class ManufacturerDetailView(LoginRequiredMixin, DetailView):
    model = models.Manufacturer
    fields = "__all__"


class ManufacturerUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Manufacturer
    fields = "__all__"
    success_url = "/aircrafts/manufacturers/"


class ManufacturerDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Manufacturer
    success_url = "/aircrafts/manufacturers/"


class EngineCategoryListView(LoginRequiredMixin, ListView):
    model = models.EngineCategory
    paginate_by = 100


class EngineCategoryCreateView(LoginRequiredMixin, CreateView):
    model = models.EngineCategory
    fields = "__all__"
    success_url = "/aircrafts/engine-categories/"


class EngineCategoryDetailView(LoginRequiredMixin, DetailView):
    model = models.EngineCategory
    fields = "__all__"


class EngineCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = models.EngineCategory
    fields = "__all__"
    success_url = "/aircrafts/engine-categories/"


class EngineCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = models.EngineCategory
    success_url = "/aircrafts/engine-categories/"


class AircraftListView(ListView):
    model = models.Aircraft


class AircraftCreateView(LoginRequiredMixin, CreateView):
    model = models.Aircraft
    fields = "__all__"
    success_url = "/aircrafts/"


class AircraftDetailView(DetailView):
    model = models.Aircraft
    fields = "__all__"


class AircraftUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Aircraft
    fields = "__all__"
    success_url = "/aircrafts/"


class AircraftDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Aircraft
    success_url = "/aircrafts/"


class EngineCategoryAddView(LoginRequiredMixin, CreateView):
    model = models.EngineCategory
    fields = "__all__"

    def get(self, request, pk):
        aircraft = models.Aircraft.objects.get(pk=pk)
        form = self.get_form()
        form.fields['aircraft'].initial = aircraft

        return render(request, "aircrafts/engine_category_form.html", {"form": form})

    def post(self, request, pk):
        form = self.get_form()
        if form.is_valid():
            data = form.cleaned_data
            self.model.objects.create(**data)
            messages.info(request, f"Engine Category {data['name']} created.")
            return HttpResponseRedirect(reverse("aircrafts:aircraft_detail", args=[pk]))
        else:
            messages.warning(request, "Engine Category already exists.")
            return render(request, "aircrafts/engine_category_form.html", {"form": form})

