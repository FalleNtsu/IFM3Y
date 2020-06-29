from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt  # Cookies exception
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView

# Custom Imports
from API.response import Response
from Users.models import Patient_User, User
from Medication.models import *
from Medication.serializers import *

class ListMedicationRetriveAPIView(RetrieveAPIView):
    serializer_class = List_Medication_Serializer

    def retrieve(self, request, *args, **kwargs):
        meds = List_Medication.objects.filter() 

        serializer = self.serializer_class(meds, many=True)
        resp = Response(True, None, serializer.data)
        return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)

class PatientMedicationRetriveAPIView(RetrieveAPIView):
    serializer_class = Patient_Medication_Serializer

    def retrieve(self, request, username, *args, **kwargs):
        try:
            user = User.objects.get(username=username)
            patient = Patient_User.objects.get(user=user)
            meds = Patient_Medication.objects.filter(patient=patient)

        except Patient_User.DoesNotExist:
            resp = Response(False, "No Pateint with the username {}".format(username))
            return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)
        
        serializer = self.serializer_class(meds, many=True)
        resp = Response(True, None, serializer.data)
        return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)

class MedicationTakenRetriveAPIView(RetrieveAPIView):
    serializer_class = Taken_Medication_Serializer

    def retrieve(self, request, username, *args, **kwargs):
        try:
            user = User.objects.get(username=username)
            patient = Patient_User.objects.get(user=user)
            patient_meds = Taken_Medication.objects.filter(patients_medication__patient=patient)
        except Patient_User.DoesNotExist:
            resp = Response(False, "No Pateint with the username {}".format(username))
            return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)

        serializer = self.serializer_class(patient_meds, many=True)
        resp = Response(True, None, serializer.data)
        return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)