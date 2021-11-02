from django.db import models
from core.models import TimeStampModel


class User(TimeStampModel):
    name = models.CharField(max_length=16)
    email = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    last_login = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
