from django.db import IntegrityError
from rest_framework import serializers
from .models import Artist, Album, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'album', 'serial_number')

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            album = validated_data['album']
            serial_number = validated_data['serial_number']
            raise serializers.ValidationError(
                f"A song with serial number {serial_number} already exists for album {album}.")

    def update(self, instance, validated_data):
        try:
            return super().update(instance, validated_data)
        except IntegrityError:
            album = validated_data.get('album', instance.album)
            serial_number = validated_data.get('serial_number', instance.serial_number)
            raise serializers.ValidationError(
                f"A song with serial number {serial_number} already exists for album {album}.")


class AlbumSerializer(serializers.ModelSerializer):
    songs = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = ('id', 'title', 'release_year', 'artist', 'songs')


class ArtistSerializer(serializers.ModelSerializer):
    albums = serializers.StringRelatedField(many=True)

    class Meta:
        model = Artist
        fields = ('id', 'artist_name', 'albums')
