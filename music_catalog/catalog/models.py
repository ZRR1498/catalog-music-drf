from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(max_length=100, verbose_name='Artist name', unique=True)

    def __str__(self):
        return f'id: {self.pk} | name: {self.artist_name}'

    class Meta:
        verbose_name = 'Artist'
        ordering = ['artist_name']


class Album(models.Model):
    title = models.CharField(max_length=100, verbose_name='Album title')
    release_year = models.PositiveIntegerField()
    artist = models.ForeignKey(Artist, related_name='albums', verbose_name='Artist', on_delete=models.CASCADE)

    def __str__(self):
        return f"id: {self.pk} | title: {self.title} | year: {self.release_year}"

    class Meta:
        verbose_name = 'Album'
        ordering = ['artist', '-release_year']


class Song(models.Model):
    title = models.CharField(max_length=100, verbose_name='Song title')
    album = models.ForeignKey(Album, related_name='songs', verbose_name='Album', on_delete=models.CASCADE)
    serial_number = models.PositiveIntegerField()

    class Meta:
        unique_together = ('album', 'serial_number')
        verbose_name = 'Song'
        ordering = ['album', 'serial_number']

    def __str__(self):
        return f"id: {self.pk} | title: {self.title} ({self.serial_number}) | album: {self.album.title}"
