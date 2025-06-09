from django.db import models
from experimenter.models import Round

class XMLField(models.TextField):
    def db_type(self, connection):
        return 'XML'

    def rel_db_type(self, connection):
        return 'XML'

class Result(models.Model):
    xml_content = XMLField(blank=True, null=True)
    round = models.OneToOneField(Round, models.CASCADE, unique=True)
    class Meta:
        db_table = "Result"