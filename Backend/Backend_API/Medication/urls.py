from django.urls import re_path
from django.urls import path

from .views import *

urlpatterns = [
    #Types 
    # http://127.0.0.1:8000/api/activity/
    path('listMeds', ListMedicationRetriveAPIView.as_view()),
    path('<username>/patientMeds', PatientMedicationRetriveAPIView.as_view()),
    path('<username>/patientMeds/Taken', MedicationTakenRetriveAPIView.as_view()),
]