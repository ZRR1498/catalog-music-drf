from django.urls import path
from . import views

urlpatterns = [
    path('', views.CatalogApiOverview.as_view()),
    path('artists/', views.ArtistListView.as_view(), name='artists-list'),
    path('artists/<int:id>', views.ArtistDetailView.as_view(), name='artist-detail'),
    path('albums/', views.AlbumListView.as_view(), name='albums-list'),
    path('albums/<int:id>', views.AlbumDetailView.as_view(), name='album-detail'),
    path('songs/', views.SongListView.as_view(), name='song-list'),
    path('songs/<int:id>', views.SongDetailView.as_view(), name='song-detail'),
]