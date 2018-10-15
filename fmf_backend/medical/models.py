"""
fmf-backend/fmf_backend/medical
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from biological import models as bio

# Create your models here.
class Medication(models.Model):
    """

    """
    sideEffects = models.ManyToManyField(bio.PainEffect)
    name = models.CharField(max_length=40)
    manufacturure = models.CharField(max_length=40)

    def __str__(self):
        return "Medication({_id}) name: {name}".format(**{
            "_id": self.id if self.id else "Unknown",
            "name": self.name
            })


class Mutations(models.Model):
    """
    The specific mutation that the profile have.
    """
    name = models.CharField(blank=False, max_length=40)

    def __str__(self):
        return "Mutation({_id}) name {name}".format(**{
            "_id": self.id if self.id else "Unknown",
            "name": self.name
            })


class Seizure(models.Model):
    """
    Model for a specific Seizure. a Seizure containes multiple
    changes because a Seizure can start in one thing and end with anouther.
    """
    globalStartDate = models.DateTimeField(auto_now_add=True)
    globalEndDate = models.DateTimeField(auto_now=True)
    globalNote = models.CharField(max_length = 300, blank=True)


class Changes(models.Model):
    """
    A change in the seizure.
    """
    pain = models.ForeignKey(bio.PainEffect, on_delete=models.CASCADE)
    globalStartDate = models.DateTimeField(auto_now_add=True)
    globalEndDate = models.DateTimeField(auto_now=True)
    note = models.CharField(max_length = 300, blank=True)
    bodyPart = models.ForeignKey(bio.BodyPart, on_delete=models.CASCADE)

    def __str__(self):
        return "Change({_id}) pain: {pain}".replace(**{
            "_id": self.id if self.id else "Unknown",
            "pain": self.pain if self.pain else "Unknown"
            })
