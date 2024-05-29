from django.urls import path
from django.views.generic import TemplateView

app_name = "webgames"
urlpatterns = [
    path(
        "memory/",
        view=TemplateView.as_view(template_name="webgames/memory/memory.html"),
        name="memory"
    )
]