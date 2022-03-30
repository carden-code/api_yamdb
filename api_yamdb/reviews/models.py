from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='name')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='индентификатор')

    class Meta:
        ordering = ('name',)
        verbose_name = 'категория'


class Genre(models.Model):
    name = models.CharField(max_length=256, verbose_name='имя')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='индентификатор')

    class Meta:
        ordering = ('name',)
        verbose_name = 'жанр'


class Title(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='имя')
    description = models.TextField(verbose_name='описание')
    year = models.IntegerField()
    genre = models.ManyToManyField(
        'Genre',
        related_name='genre'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='category',
        null=True,
        verbose_name='категория'
    )

    class Meta:
        ordering = ('name', 'year',)
        verbose_name = 'произведения'

