from django.db import models

# Create your models here.
class Classify(models.Model):
    message_input   = models.CharField(max_length=300, blank=True, null=True)
    priority        = models.BooleanField(default=False)
    sentiment       = models.CharField(max_length=200, blank=True, null=True)
    len_sentence    = models.CharField(max_length=200, blank=True, null=True)
    lst_sentence    = models.CharField(max_length=300, blank=True, null=True)
    duration        = models.CharField(max_length=50, blank=True, null=True)
    created         = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created)
