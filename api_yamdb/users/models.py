from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES = (('user', 'USER'), ('moderator', 'MODERATOR'), ('admin', 'ADMIN'))

    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=254,
        unique=True,
        blank=False
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=128,
        blank=True
    )
    bio = models.TextField(verbose_name='Биография', blank=True)
    role = models.CharField(
        verbose_name='Роль',
        max_length=300,
        choices=ROLES,
        default=ROLES[0][0]
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def is_admin(self):
        return self.is_superuser or self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    def __str__(self):
        return self.username
