"""
fmf-backend/fmf_backend/biological/models.py
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from biological import models as bio

# Create your models here.
class BodyPart(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return "BodyPart({_id}) name: {name}".format(**{
            "_id": self.id if self.id else "Unknone",
            "name": self.name if self.name else "Unkown"

            })


class PainEffect(models.Model):
    PAIN_TYPES = (
        ('P', 'Pain'),
        ('I', "Infections"),
        ('D', 'Diarrhea'),
        ('N', 'Nausea'),
        ('V', 'Vomiting'),
        ('C', 'Consipation'),
        ('O', 'Other')
    )
    PAIN_CHARACTERIZATION = (
            ('D', 'Dull'),
            ('S', 'Sharp'),
            ('B', 'Burning'),
            ('P', 'Pulling'),
            )
    painType = models.CharField(max_length=8, choices=PAIN_TYPES, blank=True)
    painCharacterization = models.CharField(max_length=8, choices=PAIN_CHARACTERIZATION , blank=True)
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],blank=True, null=True)
    location = models.ForeignKey(bio.BodyPart, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Pain({self.id if self.id else 'Unkown'}) type {self.painType if self.painType else 'Unknown'} at location"
