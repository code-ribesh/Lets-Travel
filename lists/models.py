from django.db import models
from core import models as core_models


# Create your models here.
class List(core_models.TimeStampModel):

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self):
        return self.name
