"""
fmf-backend/fmf_backend/person

TODO:
     * prespriction end date requiered if isActive == False
     * add option to record medications side effects
     * add times in mounth that the user forgat to take his / her pills

"""

from django.db import models
from biological import models as bio
from medical import models as med
import datetime

# Create your models here.
class Profile(models.Model):
    HMOs = (
            ("C", "Clalit"),
            ("M", "Maccaby"),
            ("L", "Leumit"),
            ("T", "meuhedet"),  # todo think about something
            )
    nikname = models.CharField(max_length=30)
    birthday = models.DateTimeField()
    diagnosisDate = models.DateTimeField()
    originID = models.IntegerField()
    seizureFrequency = models.IntegerField() # per year
    hmo = models.CharField(max_length=1, null=True)

    def __str__():
        return "{0}".format(nikname)


class Perscripton(models.Model):
    medicationId = models.ForeignKey(med.Medication(), on_delete=models.CASCADE)
    frequency = models.IntegerField()
    amount = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    startDate = models.DateTimeField(default=datetime.datetime.fromtimestamp(1))  # time started to take the prespriction, NOT the creation of the instance
    endDate = models.DateTimeField(null=True)  # todo fixme




class User(models.Model):
    pass

