from django.contrib import admin
from .models import Profile, User, Prescription, MdeicationUse

# Register your models here.
admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Prescription)
admin.site.register(MdeicationUse)
