from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer


class ApiOverview(GenericAPIView):
    def get(self, arg):
        data = {
            'Music catalog': 'api/',
            'Swagger documentation': 'swagger/',
            'Alternative Documentation': 'redoc/',
        }
        return Response(data)


class CatalogApiOverview(GenericAPIView):
    def get(self, arg):
        data = {
            'List of artists': 'artists/',
            'List of albums': 'albums/',
            'List of songs': 'songs/',
            'Detail artist': 'artists/<int:id>',
            'Detail album': 'albums/<int:id>',
            'Detail song': 'songs/<int:id>',
        }
        return Response(data)


class ArtistListView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = 'id'


class AlbumListView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    lookup_field = 'id'


class SongListView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'id'
