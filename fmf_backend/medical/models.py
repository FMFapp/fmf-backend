"""
fmf-backend/fmf_backend/medical
"""
from django.db import models
from django.core import MaxValueValidator, MinValueValidator
from ..biological import models as bio

# Create your models here.
class Medication(model.Model):
    """

    """
    sideEffects = models.ManyToManyField()
    name = models.CharFields(max_length=40)
    manufacturure = models.CharFields(max_length=40)

    def __str__(self):
        return "Medication({_id}) name: {name}".format(**{
            "_id": self.id if self.id else "Unknone",
            "name": self.name
            })


class Mutations(model.Model):
    """
    The specific mutation that the profile have.
    """
    name = models.CharFields(blank=False, max_length=40)

    def __str__(self):
        return "Mutation({_id}) name {name}".format({
            "_id": self.id if self.id else "Unknone",
            "name": self.name
            })


class Seizure(model.Model):
    """
    Model for a specific Seizure. a Seizure containes multiple
    changes because a Seizure can start in one thing and end with anouther.
    """
    globalStartDate = models.DateTimeField(auto_now_add=True)
    globalEndDate = models.DateTimeField(auto_now=True)
    globalNote = models.CharField(max_length = 300, blank=True)


class Changes(model.Model):
    """
    A change in the seizure.
    """
    pain = models.ForeignKey(bio.PainEffect)
    globalStartDate = models.DateTimeField(auto_now_add=True)
    globalEndDate = models.DateTimeField(auto_now=True)
    note = models.CharField(max_length = 300, blank=True)
    bodyPart = models.ForeignKey(bio.BodyPart)

    def __str__(self):
        return "Change({_id}) pain: {pain}".replace(**{
            "_id": self.id if self.id else "Unknone",
            "pain": self.pain if self.pain else
            })
