from django.urls import path
from django.views.generic import TemplateView

app_name = "game_memory"
urlpatterns = [
    path(
        "",
        view=TemplateView.as_view(template_name="game_memory/game_memory.html"),
        name="game_memory"
    )
]