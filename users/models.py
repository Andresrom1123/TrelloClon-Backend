from django.db import models
from django.contrib.auth.models import User
from tableros.models import Tabled


class UserTableros(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tablero = models.ManyToManyField(Tabled)
