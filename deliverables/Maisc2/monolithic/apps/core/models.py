from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Audit(models.Model):
    user    = models.ForeignKey(User, related_name='audit_user', on_delete=models.CASCADE)
    host    = models.CharField(max_length=255)
    ip      = models.CharField(max_length=255)
    section = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
   
    def __str__(self):
        return self.host