from django.db import models

class MusicDirector(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    experience = models.IntegerField()
    famous_album = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music_director"

    @staticmethod
    def create(name, age, experience, famous_album, is_active=True):
        return MusicDirector.objects.create(
            name=name,
            age=age,
            experience=experience,
            famous_album=famous_album,
            is_active=is_active
        )

    @staticmethod
    def get_all():
        return MusicDirector.objects.all()

    @staticmethod
    def get_one(director_id):
        return MusicDirector.objects.filter(id=director_id).first()

    @staticmethod
    def update(director_id, name=None, age=None, experience=None, famous_album=None, is_active=None):
        director = MusicDirector.objects.filter(id=director_id).first()
        if not director:
            return None

        if name is not None:
            director.name = name
        if age is not None:
            director.age = age
        if experience is not None:
            director.experience = experience
        if famous_album is not None:
            director.famous_album = famous_album
        if is_active is not None:
            director.is_active = is_active

        director.save()
        return director

    @staticmethod
    def delete_one(director_id):
        director = MusicDirector.objects.filter(id=director_id).first()
        if not director:
            return False
        director.delete()
        return True
