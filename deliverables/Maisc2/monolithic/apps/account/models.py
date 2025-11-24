from django.db import models
from django.conf import settings
from PIL import Image

class Profile(models.Model):
    user          = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo         = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, null=True)
    collor        = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
        
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
                super().save(force_insert, force_update, using, update_fields)

                img = Image.open(self.photo.path)

                if img.height > 300 or img.width > 300:
                    new_img = (300, 300)
                    img.thumbnail(new_img)
                    img.save(self.photo.path)   


# def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
#             super().save(force_insert, force_update, using, update_fields)