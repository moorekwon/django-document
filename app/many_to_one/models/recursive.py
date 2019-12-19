from django.db import models
from django.db.models import SET_NULL


class WPSUser(models.Model):
    instructor = models.ForeignKey('self', on_delete=SET_NULL, related_name='student_set', null=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
