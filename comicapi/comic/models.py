from token import LESSEQUAL

from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

class User(AbstractUser):
    avatar = CloudinaryField(null=True)


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Genre(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Country(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Writer(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.first_name) + str(self.last_name)


class ComicStatus(models.TextChoices):
    ONGOING = 'ongoing', 'Ongoing'
    COMPLETED = 'completed', 'Completed'
    HIATUS = 'hiatus', 'Hiatus'
    CANCELED = 'canceled', 'Canceled'

class Comic(BaseModel):
    name = models.CharField(max_length=255)
    image = CloudinaryField(null=True)
    status = models.CharField(max_length=10, choices=ComicStatus.choices, default=ComicStatus.ONGOING)
    view_count = models.IntegerField()
    description = RichTextField()

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    genres = models.ManyToManyField(Genre)
    writers = models.ManyToManyField(Writer)

    def __str__(self):
        return self.name


class Chapter(BaseModel):
    title = models.TextField()
    order = models.FloatField()

    comic = models.ForeignKey(Comic, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Page(BaseModel):
    order = models.IntegerField()
    image = CloudinaryField()

    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

class Interaction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class History(Interaction):
    pass

class Favorite(Interaction):
    pass

class Comment(Interaction):
    content = RichTextField()


class ReactionType(models.TextChoices):
    LIKE = 'like', 'Like',
    DISLIKE = 'dislike', 'Dislike'
    LOVE = 'love', 'Love'
    HAHA = 'haha', 'Haha'
    SAD = 'sad', 'Sad'
    ANGRY = 'angry', 'Angry'


class Reaction(Interaction):
    type = models.CharField(max_length=10, choices=ReactionType.choices, default=ReactionType.LIKE)

