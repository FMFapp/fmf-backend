"""
TODO:
    - think about how in the mother of god to do this
"""

from django.db import models


class HMO(models.Model):
    HMOs = (
        ("C", "Clalit"),
        ("M", "Maccaby"),
        ("L", "Leumit"),
        ("T", "meuhedet"),  # todo think about something
    )


class Facility(models.Model):
    hmo = models.ForeignKey(HMO, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    city = models.CharField(max_length=85)  # there is a city called Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu (wiki: https://en.wikipedia.org/wiki/Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu)
    street = models.CharField(max_length=85)

    def __repr__(self):
        return f"Facility<{self.id}>(hmo={self.hmo}, latitude={self.latitude}, longitude={self.longitude}, " \
               f"city={self.city}, street={self.street})"

    def __str__(self):
        return repr(self)
