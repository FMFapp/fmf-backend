"""
fmf-backend/fmf_backend/biological/models.py
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class BodyPart(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return "BodyPart({_id}) name: {name}".format(**{
            "_id": self.id if self.id else "Unknone",
            "name": self.name
            })


class PainEffect(models.Model):
    PAIN_TYPES = (
        ('P', 'Pain'),
        ('I', "Infections"),
    )
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    location = models.ForeignKey(BodyPart, on_delete=models.CASCADE)
    painType = models.CharField(max_length=8, choices=PAIN_TYPES)

    def __str__(self):
        return "Pain({_id}) level {level} at location".format(**{
            "_id": self.id if self.id else "Unknown",
            "level": self.level,
            "location": self.location.name
            })

