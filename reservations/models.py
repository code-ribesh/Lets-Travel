from django.db import models
from core import models as core_models

# Create your models here.
class Reservation(core_models.TimeStampModel):

    STATUS_PENDING = "pending"
    STATUS_COMFIRMED = "comfirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_COMFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"
