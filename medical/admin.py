from django.contrib import admin
from .models import Medication, Mutation, Seizure, Change


admin.site.register(Medication)
admin.site.register(Mutation)
admin.site.register(Seizure)
admin.site.register(Change)
