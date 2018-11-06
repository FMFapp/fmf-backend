from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class BodyPart(models.Model):
    name = models.CharField(max_length=30)

    def __repr__(self):
        return f"BodyPart<{self.id}>(name={self.name})"

    def __str__(self):
        return repr(self)


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
    painCharacterization = models.CharField(max_length=8, choices=PAIN_CHARACTERIZATION, blank=True)
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], blank=True, null=True)
    location = models.ForeignKey(BodyPart, on_delete=models.CASCADE, blank=True, null=True)

    def __repr__(self):
        return f"PainEffect<{self.id}>(painType={self.painType}, painCharacterization={self.painCharacterization}," \
               f"level={self.level}, location={self.location})"

    def __str__(self):
        return repr(self)
