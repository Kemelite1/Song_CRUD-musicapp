from django.urls import path
from . import views

# various endpoints
urlpatterns = [
    path('artiste', views.CreateArtise.as_view()),
    path('song', views.Create_and_get_all_Song.as_view()),
    path('lyrics', views.CreateLyrics.as_view()),
    path('song/<int:pk>', views.Update_read_del.as_view()),
]
