from django.db import models

# Create your models here.
class Recognize(models.Model):
    message_input     = models.CharField(max_length=300, blank=True, null=True)
    message_output    = models.CharField(max_length=300, blank=True, null=True)
    duration          = models.CharField(max_length=50, blank=True, null=True)
    message_tokens    = models.CharField(max_length=300, blank=True, null=True)
    len_tokens        = models.CharField(max_length=300, blank=True, null=True)
    lst_ents_posi     = models.CharField(max_length=300, blank=True, null=True)
    lst_ents_text     = models.CharField(max_length=300, blank=True, null=True)
    lst_ents_kind     = models.CharField(max_length=300, blank=True, null=True)
    list_message_ents = models.CharField(max_length=300, blank=True, null=True)
    dict_message_ents = models.TextField(max_length=300, blank=True, null=True)
    count_ents        = models.CharField(max_length=300, blank=True, null=True)
    created           = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created)
    

#... CONTAINER RECOGNIZE ENTITY ...#
# message_tokens, len_tokens, lst_ents_posi,lst_ents_text, lst_ents_kind, list_message_ents, \
# dict_message_ents,count_ents, message_with_ents = recognize_get_entity_message(message_raw)