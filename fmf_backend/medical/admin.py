from django.contrib import admin
from .models import Medication, Mutation, Seizure, Changes
# Register your models here.
admin.site.register(Medication)
admin.site.register(Mutation)
admin.site.register(Seizure)
admin.site.register(Changes)
