"""
fmf-backend/fmf_backend/person
"""
from django.db import models
from biological import models as bio
from medical import models as med

# Create your models here.
class Profile(models.Model):
    nikname = models.CharField(max_length=30)
    birthday = models.DateTimeField()
    diagnosisDate = models.DateTimeField()
    originID = models.IntegerField()
    seizureFrequency = models.IntegerField() # per year

    def __str__():
        return "{0}".format(nikname)


class Perscripton(models.Model):
    medicationId = models.ForeignKey(med.Medication(), on_delete=models.CASCADE)
    frequency = models.IntegerField()
    amount = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class User(models.Model):
    pass

