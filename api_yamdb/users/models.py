from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN = 1
    MODERATOR = 2
    USER = 3

    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (MODERATOR, 'moderator'),
        (USER, 'user'),
    )

    bio = models.TextField(
        verbose_name='Биография',
        blank=True,
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True
    )
    password = None

    role = models.PositiveSmallIntegerField(
        verbose_name='Роль пользователя',
        choices=ROLE_CHOICES,
        default=USER
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
