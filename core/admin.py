from django.contrib import admin

from core.models.audit import Audit
from core.models.pinpad import PinPadStatus


class PinPadAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PinPadStatus._meta.concrete_fields]


admin.site.register(PinPadStatus, PinPadAdmin)


class AuditAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Audit._meta.concrete_fields]


admin.site.register(Audit, AuditAdmin)

