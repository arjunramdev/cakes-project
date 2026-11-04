from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class RoleChoices(models.TextChoices):

    ADMIN = 'Admin', 'Admin'
    USER = 'User', 'User'

class Profile(AbstractUser):

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='profile_set',
        related_query_name='profile',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='profile_set',
        related_query_name='profile',
    )
    role = models.CharField(max_length=20, choices=RoleChoices.choices)

    class Meta:

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):

        return self.first_name
