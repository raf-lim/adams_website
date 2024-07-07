from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from games import models
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class ChapterListView(LoginRequiredMixin, ListView):
    model = models.Chapter
    paginate_by = 100


class ChapterCreateView(LoginRequiredMixin, CreateView):
    model = models.Chapter
    fields = "__all__"
    success_url = "/games/chapters/"


class ChapterUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Chapter
    fields = "__all__"
    success_url = "/games/chapters/"


class ChapterDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Chapter
    success_url = "/games/chapters/"


class CategoryListView(LoginRequiredMixin, ListView):
    model = models.Category
    paginate_by = 100


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = models.Category
    fields = "__all__"
    success_url = "/games/categories/"


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = models.Category
    fields = "__all__"


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Category
    fields = "__all__"


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Category
    success_url = "/games/categories/"


class GameListView(ListView):
    model = models.Game


class GameCreateView(LoginRequiredMixin, CreateView):
    model = models.Game
    fields = "__all__"
    success_url = "/games/"


class GameDetailView(DetailView):
    model = models.Game
    fields = "__all__"

    # def get(self, request, pk):
    #     object = self.model.objects.get(pk=pk)
    #     chapters = [character.chapter for character in models.Character.objects.filter(game__pk=pk).distinct("chapter")]
    #     context = {
    #         "object": object,
    #         "chapters": chapters,
    #     }
    #     return render(request, "games/game_detail.html", context)


class GameUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Game
    fields = "__all__"
    success_url = "/games/"


class GameDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Game
    success_url = "/games/"


class CharacterListView(LoginRequiredMixin, ListView):
    model = models.Character
    # paginate_by = 5

class CharacterCreateView(LoginRequiredMixin, CreateView):
    model = models.Character
    fields = "__all__"
    success_url = "/games/characters/"


class CharacterDetailView(DetailView):
    model = models.Character
    fields = "__all__"


class CharacterUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Character
    fields = "__all__"


class CharacterDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Character
    success_url = "/games/characters/"


class CharacterAddView(LoginRequiredMixin, CreateView):
    model = models.Character
    fields = "__all__"

    def get(self, request, pk):
        game = models.Game.objects.get(pk=pk)
        form = self.get_form()
        form.fields['game'].initial = game

        return render(request, "games/character_form.html", {"form": form})

    def post(self, request, pk):
        form = self.get_form()
        if form.is_valid():
            data = form.cleaned_data
            self.model.objects.create(**data)
            messages.info(request, f"Character {data['name']} created.")
            return HttpResponseRedirect(reverse("games:game_detail", args=[pk]))
        else:
            messages.warning(request, "Character already exists.")
            return render(request, "games/character_form.html", {"form": form})

