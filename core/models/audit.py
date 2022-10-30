from django.db import models
from django.db.models import BooleanField, DateTimeField


class Audit(models.Model):
    did_unlock = BooleanField(null=False)
    created_at = DateTimeField(auto_now_add=True)

    @classmethod
    def add_audit(cls, status: bool) -> None:
        cls.objects.create(did_unlock=status)
