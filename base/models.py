from django.db import models
from django.utils.translation import ugettext_lazy as _

class TimeStampModel(models.Model):
    created_at=models.DateTimeField(_("created"),auto_now_add=True,editable=False)
    updated_at=models.DateTimeField(_("updated"),auto_now=True)
    created_by=models.CharField(default="Murli")

    class Meta:
        abstract=True