from django.urls import path
from django.views.generic import TemplateView

app_name = "memory"
urlpatterns = [
    path(
        "",
        view=TemplateView.as_view(template_name="memory/memory.html"),
        name="memory"
    )
]