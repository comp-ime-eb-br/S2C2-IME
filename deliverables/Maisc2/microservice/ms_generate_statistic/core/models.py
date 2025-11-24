from django.db import models

# Create your models here.
class Statistic(models.Model):

    message_input = models.CharField(max_length=300, blank=True, null=True)
    host_sender = models.CharField(max_length=200, blank=True, null=True)
    ip_sender = models.CharField(max_length=200, blank=True, null=True)
    host_receiver = models.CharField(max_length=200, blank=True, null=True)
    ip_receiver = models.CharField(max_length=200, blank=True, null=True)
    noun_count = models.CharField(max_length=200, blank=True, null=True)
    verb_count = models.CharField(max_length=200, blank=True, null=True)
    pron_count = models.CharField(max_length=200, blank=True, null=True)
    adje_count = models.CharField(max_length=200, blank=True, null=True)
    punc_count = models.CharField(max_length=200, blank=True, null=True)
    num_count = models.CharField(max_length=200, blank=True, null=True)
    adve_count = models.CharField(max_length=200, blank=True, null=True)
    conj_count = models.CharField(max_length=200, blank=True, null=True)
    det_count = models.CharField(max_length=200, blank=True, null=True)
    other_count = models.CharField(max_length=200, blank=True, null=True)
    lst_noun = models.CharField(max_length=200, blank=True, null=True)
    lst_verb = models.CharField(max_length=200, blank=True, null=True)
    lst_adve = models.CharField(max_length=200, blank=True, null=True)
    lst_pron = models.CharField(max_length=200, blank=True, null=True)
    lst_adje = models.CharField(max_length=200, blank=True, null=True)
    lst_punc = models.CharField(max_length=200, blank=True, null=True)
    lst_conj = models.CharField(max_length=200, blank=True, null=True)
    lst_det = models.CharField(max_length=200, blank=True, null=True)
    lst_num = models.CharField(max_length=200, blank=True, null=True)
    lst_other = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    created  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created)