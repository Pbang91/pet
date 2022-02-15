from django.db import models

# Create your models here.
class Actor(models.Model):
    first_name    = models.CharField(max_length=45)
    last_name     = models.CharField(max_length=45)
    date_of_birth = models.DateField()


    class Meta:
        db_table = 'actors'

class Movie(models.Model):
    title        = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()
    # 아래가 매니 투 매니 / 액터 클래스를 참조하고, 액터오브무비를 통해서 하고, 무비클래스가 들어가는 무비변수와 액터클래스가 들어가는 액터 변수
    actors       = models.ManyToManyField('Actor', through='ActorOfMovie', through_fields=('movie', 'actor'))

    class Meta:
        db_table = 'movies'

class ActorOfMovie(models.Model):
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)

    class Meta:
        db_table = 'actors_movies'