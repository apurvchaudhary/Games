from django.urls import path
from . import views


urlpatterns = [
    path('get_all_games/', views.GameList.as_view()),
    path('upload_games/', views.UploadGames.as_view()),
    path('title/', views.SearchGame.as_view()),
]