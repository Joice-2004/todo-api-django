from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    singers = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "songs"

    @staticmethod
    def create(name, description="", singers="", is_active=True):
        return Song.objects.create(
            name=name,
            description=description,
            singers=singers,
            is_active=is_active
        )

    @staticmethod
    def get_all(params=None):
        qs = Song.objects.all()

        if not params:
            return qs

        page_num = int(params.get("page_num", 1))
        limit = int(params.get("limit", 10))

        start = (page_num - 1) * limit
        end = start + limit

        return qs[start:end]

    @staticmethod
    def get_one(song_id):
        return Song.objects.filter(id=song_id).first()

    @staticmethod
    def update(song_id, name=None, description=None, singers=None, is_active=None):
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

        song.save()
        return song

    @staticmethod
    def delete_one(song_id):
        song = Song.objects.filter(id=song_id).first()
        if not song:
            return False
        song.delete()
        return True
