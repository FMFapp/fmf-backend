"""
fmf-backend/fmf_backend/medical/models.py
"""
from django.db import models
from biological.models import PainEffect
from person.models import MedicationUse


class Medication(models.Model):
    MEDICATION_TYPES = (
        ("P", "Pills"),
        ("I", "Injection"),
        ("T", "Topical"),
        ("D", "Drop"),
        ("O", "Other")
    )
    sideEffects = models.ManyToManyField(PainEffect)  # todo add better way to do this
    name = models.CharField(max_length=40)
    manufacture = models.CharField(max_length=40)

    def __repr__(self):
        return f"Medication<{self.id}>(sideEffects={self.sideEffects}, name={self.name}, " \
               f"manufacture={self.manufacture})"

    def __str__(self):
        return repr(self)


class Mutation(models.Model):
    """The specific mutation that the profile have."""
    name = models.CharField(blank=False, max_length=40)
    note = models.CharField(blank=True, max_length=300)

    def __repr__(self):
        return f"Mutation<{self.id}>(name={self.name}, note={self.note})"

    def __str__(self):
        return repr(self)


class Seizure(models.Model):
    """
    Model for a specific Seizure. a Seizure contains multiple
    changes because a Seizure can start in one thing and end with another.
    """
    globalStartDate = models.DateTimeField(auto_now_add=True)
    globalEndDate = models.DateTimeField(auto_now=True)  # todo change to the last change globalend
    globalNote = models.CharField(max_length=300, blank=True)

    def __repr__(self):
        return f"Seizure<{self.id}>(globalStartDate={self.globalStartDate}, globalEndDate={self.globalEndDate}, " \
               f"globalNote={self.globalNote})"

    def __str__(self):
        return repr(self)


class Change(models.Model):
    """A change in the seizure."""
    pain = models.ForeignKey(PainEffect, on_delete=models.CASCADE)
    startDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField(auto_now=True)
    note = models.CharField(max_length=300, blank=True)
    seizure = models.ForeignKey(Seizure, on_delete=models.CASCADE, null=True)
    medications = models.ForeignKey(MedicationUse, on_delete=models.CASCADE, null=True, blank=True)

    def __repr__(self):
        return f"Changes<{self.id}>(pain={self.pain}, startDate={self.startDate}, endDate={self.endDate}, " \
               f"note={self.note}, seizure={self.seizure}, medications={self.medications})"

    def __str__(self):
        return repr(self)
