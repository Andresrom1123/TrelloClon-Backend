from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tabled(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    fecha_hora = models.DateTimeField(default=timezone.now())
    dueno = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_dueno')
    VISIBLE = 'Pb'
    PRIVATE = 'Pr'
    VISIBLE_PRIVATE_CHOICES = [
        (VISIBLE, 'Publico'),
        (PRIVATE, 'Privado')
    ]
    visibility = models.CharField(
        max_length=2,
        choices=VISIBLE_PRIVATE_CHOICES,
    )
    members = models.ManyToManyField(User, related_name='members_user')
    favorite = models.ManyToManyField(User, related_name='favorite_user', null=True)

    def __str__(self):
        return self.name



