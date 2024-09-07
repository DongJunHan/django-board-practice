from django.db import models

from libs.models import BaseModel


# Create your models here.
class User(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.email}"


class Token(BaseModel):
    key = models.CharField(max_length=100)
