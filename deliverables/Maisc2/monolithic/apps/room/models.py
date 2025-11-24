from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Room(models.Model):
    room    = models.CharField(max_length=255)
    slug    = models.SlugField(unique=True)
    user    = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                                related_name='room_user',
                                                blank=True)
    nlp     = models.BooleanField(default=True) # if true aplied it does then it doesnt 
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def written_by(self):
        return "; ".join([str(_).lower() for _ in self.user.all()])
    
    def __str__(self):
        return self.slug


class Message(models.Model):
    room     = models.ForeignKey(Room, related_name='message_room', on_delete=models.CASCADE)
    user     = models.ForeignKey(User, related_name='message_user', on_delete=models.CASCADE)
    content  = models.TextField()
    priority = models.BooleanField(default=False)
    duration = models.CharField(blank=True, null=True)
    created  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return str(self.room.slug)


class Hierarchy(models.Model):
    user    = models.ForeignKey(User, related_name='hierarchy_user', on_delete=models.CASCADE)
    parent  = models.ForeignKey(User, related_name='hierarchy_parent', on_delete=models.CASCADE)
    child   = models.ForeignKey(User, related_name='hierarchy_child', on_delete=models.CASCADE)
    room    = models.ForeignKey(Room, related_name='hierarchy_room', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)


class Grupo(models.Model):
    group = models.CharField(max_length=200) 
    agent = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                                related_name='group_agent',
                                                blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)