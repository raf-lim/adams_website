from django.urls import path
from games import views

app_name = "games"
urlpatterns = [
    path("game-create/", views.GameCreateView.as_view(), name='game_create'),
    path("game-detail/<pk>", views.GameDetailView.as_view(), name='game_detail'),
    path("game-update/<pk>", views.GameUpdateView.as_view(), name='game_update'),
    path("game-delete/<pk>", views.GameDeleteView.as_view(), name='game_delete'),
    path("", views.GameListView.as_view(), name="games"),
    path("categories/", views.CategoryListView.as_view(), name="categories"),
    path("category-create/", views.CategoryCreateView.as_view(), name='category_create'),
    path("category-detail/<pk>", views.CategoryDetailView.as_view(), name="category_detail"),
    path("category-update/<pk>", views.CategoryUpdateView.as_view(), name="category_update"),
    path("category-delete/<pk>", views.CategoryDeleteView.as_view(), name="category_delete"),
    path("chapters/", views.ChapterListView.as_view(), name="chapters"),
    path("chapter-create/", views.ChapterCreateView.as_view(), name='chapter_create'),
    path("chapter-update/<pk>", views.ChapterUpdateView.as_view(), name="chapter_update"),
    path("chapter-delete/<pk>", views.ChapterDeleteView.as_view(), name="chapter_delete"),
    path("characters/", views.CharacterListView.as_view(), name="characters"),
    path("character-create/", views.CharacterCreateView.as_view(), name='character_create'),
    path("character-detail/<pk>", views.CharacterDetailView.as_view(), name="character_detail"),
    path("character-update/<pk>", views.CharacterUpdateView.as_view(), name="character_update"),
    path("character-delete/<pk>", views.CharacterDeleteView.as_view(), name="character_delete"),
    path("game-detail/<pk>/character-add/", views.CharacterAddView.as_view(), name='character_add'),
]
