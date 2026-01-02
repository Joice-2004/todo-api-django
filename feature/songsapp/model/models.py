from django.db import models
from feature.musicdirector.model.models import MusicDirector

class Song(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    singers = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    music_director = models.ForeignKey(
        MusicDirector,
        on_delete=models.CASCADE,
        related_name="songs",
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "songs"

    @staticmethod
    def create(name, description="", singers="",is_active=True,music_director=None):
        return Song.objects.create(
            name=name,
            description=description,
            singers=singers,
            is_active=is_active,
            music_director=music_director
        )

    @staticmethod
    def get_all(params=None):
        return Song.objects.all()


    @staticmethod
    def get_one(song_id):
        return Song.objects.filter(id=song_id).first()

    @staticmethod
    def update(song_id, name=None, description=None, singers=None, is_active=None, music_director=None):
        song = Song.objects.filter(id=song_id).first()
        if not song:
            return None

        if name is not None:
            song.name = name
        if description is not None:
            song.description = description
        if singers is not None:
            song.singers = singers
        if is_active is not None:
            song.is_active = is_active
        if music_director is not None:
            song.music_director = music_director

        song.save()
        return song

    @staticmethod
    def delete_one(song_id):
        song = Song.objects.filter(id=song_id).first()
        if not song:
            return False
        song.delete()
        return True
