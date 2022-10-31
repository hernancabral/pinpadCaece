from django.db import models

# Create your models here.
from django.db.models import CharField, BooleanField


class PinPadStatus(models.Model):
    name = CharField(max_length=255),
    password = CharField(max_length=255, null=False, default='12345678')

    @classmethod
    def get_pinpad_password(cls) -> bool:
        status = cls.objects.filter().first()
        return status and status.password

    @classmethod
    def set_pinpad_password(cls, new_password) -> None:
        status = cls.objects.filter().first()
        if status:
            status.password = new_password
            status.save()
        else:
            cls.objects.create(password=new_password)
