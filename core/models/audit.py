import datetime
from django.utils import timezone

from django.db import models
from django.db.models import BooleanField, DateTimeField


class Audit(models.Model):
    did_unlock = BooleanField(null=False)
    created_at = DateTimeField(auto_now_add=True)

    @classmethod
    def add_audit(cls, status: bool) -> None:
        cls.objects.create(did_unlock=status)

    @classmethod
    def is_unlocked(cls) -> bool:
        unlocked = cls.objects.filter().last()
        if not unlocked:
            return False
        expired = unlocked.created_at < timezone.now()-datetime.timedelta(seconds=10)
        return not expired and unlocked.did_unlock
