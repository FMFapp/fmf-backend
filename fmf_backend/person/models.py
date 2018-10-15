"""
fmf-backend/fmf_backend/person
"""
from django.db import models
from ..biological import models as bio
from ..medical import models as med

# Create your models here.
class Profile(model.Model):
    nikname = model.CharFiels(max_length=30)
    birthday = model.DateTimeField()
    diagnosisDate = model.DateTimeField()
    originID = model.IntegerField()
    seizureFrequency = model.IntegerField() # per year

    def __str__():
        return "{0}".format(nikname)


class Perscripton(model.Model):
    medicationId = model.ForeignKey(med.Medication(), on_delete=models.CASCADE)
    frequency = model.IntegerField()
    amount = model.IntegerField()
    profile = model.ForeignKey(Profile)


class User(model.Model):
    pass


