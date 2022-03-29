from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    ROLES = (("user", "USER"), ("moderator", "MODERATOR"), ("admin", "ADMIN"))

    email = models.EmailField(max_length=254, unique=True, blank=False)
    bio = models.TextField(verbose_name="Биография", blank=True)
    role = models.CharField(max_length=300, choices=ROLES, default=ROLES[0][0])

    objects = MyUserManager()

    @property
    def is_admin(self):
        return self.is_superuser or self.role == "admin"

    @property
    def is_moderator(self):
        return self.role == "moderator"

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
