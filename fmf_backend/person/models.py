"""
fmf-backend/fmf_backend/person/models.py

TODO:
     * add times in mounth that the user forgat to take his / her pills
     * add option to record medications side effects

"""

from django.db import models
from biological import models as bio
from medical import models as med
import datetime


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

    def __str__(self):
        return "Mutation({_id}) name {name}".format(**{
             "_id": self.id if self.id else "Unknown",
             "name": self.name if self.name else "Unknown",
             })


class Prescription(models.Model):
    medication = models.ForeignKey(med.Medication(), on_delete=models.CASCADE)
    frequency = models.IntegerField()
    amount = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    startDate = models.DateTimeField(default=datetime.datetime.fromtimestamp(2))  # time started to take the prespriction, NOT the creation of the instance
    endDate = models.DateTimeField(default=datetime.datetime.fromtimestamp(1))  # todo fixme

    def __str__(self):
        return "{isActive} Prescription({_id}): medication {med} frequency {freq} assinged to profile {prof}".format(**{
            "_id": self.id if self.id else "Unknown",
            "med": self.medication.name if self.medication.name else "Unknown",
            "freq": self.frequency if self.frequency else "Unknown",
            "prof": self.profile.nikname if self.profile.nikname else "Unknown",
            "isActive": self.isActive
            })


class User(models.Model):
    pass


class MdeicationUse(models.Model):
    time_taken = models.DateTimeField()
    # medication = models.ForeignField(med.medicaion, on_delete=models.CASCADE)
    amount = models.IntegerField()


