"""
fmf-backend/fmf_backend/medical/models.py
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from biological import models as bio
from person import models as person

# Create your models here.
class Medication(models.Model):
    """

    """
    MEDICATION_TYPES = (
            ("P", "Pills"),
            ("I", "Injection"),
            ("T", "Topiccal"),
            ("D", "Drop"),
            ("O", "Other")
            )
    sideEffects = models.ManyToManyField(bio.PainEffect)  # todo add better way to do this
    name = models.CharField(max_length=40)
    manufacturure = models.CharField(max_length=40)


    def __str__(self):
        return "Medication({_id}) name: {name}".format(**{
            "_id": self.id if self.id else "Unknown",
            "name": self.name if self.name else "Unkown"
            })


class Mutation(models.Model):
    """
    The specific mutation that the profile have.
    """
    name = models.CharField(blank=False, max_length=40)
    note = models.CharField(blank=True, max_length=300)

    def __str__(self):
        return "Mutation({_id}) name {name}".format(**{
            "_id": self.id if self.id else "Unknown",
            "name": self.name if self.name else "Unkown"
            })


class Seizure(models.Model):
    """
    Model for a specific Seizure. a Seizure containes multiple
    changes because a Seizure can start in one thing and end with anouther.
    """
    globalStartDate = models.DateTimeField(auto_now_add=True)
    globalEndDate = models.DateTimeField(auto_now=True) # todo change to the last change globalend
    globalNote = models.CharField(max_length = 300, blank=True)


class Changes(models.Model):
    """
    A change in the seizure.
    """
    pain = models.ForeignKey(bio.PainEffect, on_delete=models.CASCADE)
    StartDate = models.DateTimeField(auto_now_add=True)
    EndDate = models.DateTimeField(auto_now=True)
    note = models.CharField(max_length = 300, blank=True)
    sizure = models.ForeignKey(Seizure, on_delete=models.CASCADE, null=True)
    medications = models.ForeignKey(person.MedicationUse, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "Change({_id}) pain: {pain}".replace(**{
            "_id": self.id if self.id else "Unknown",
            "pain": self.pain if self.pain else "Unknown"
            })
