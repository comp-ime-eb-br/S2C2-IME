from django.db import models

# Create your models here.
class Delivery(models.Model):
    message_input           = models.CharField(max_length=300, blank=True, null=True)
    background_message      = models.CharField(max_length=300, blank=True, null=True)
    color_border_message    = models.CharField(max_length=300, blank=True, null=True)
    weight_border_message   = models.CharField(max_length=300, blank=True, null=True)
    highlight_text_message  = models.CharField(max_length=300, blank=True, null=True)
    duration                = models.CharField(max_length=50, blank=True, null=True)
    created                 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created)
