"""
/fmf-backend/fmf_backend/person/views.py
"""
from django.shortcuts import render
from person.models import Profile, User, Prescription
from rest_framework import viewsets


class UserController(viewsets.ModelViewSet):
    def get(self, request):
        # queryset =
        return

    def post(self, request):
        return

    def delete(self, request):
        return


class ProfileController(View):
    def get(self, request):
        queryset =
        return

    def post(self, request):
        return

    def delete(self, request):
        return


class PrescriptionController(View):
    def get(self, request):
        return

    def post(self, request):
        return

    def delete(self, request):
        return

