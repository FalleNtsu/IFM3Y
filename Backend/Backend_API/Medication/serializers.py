from rest_framework import serializers
from Activities.models import *
from Medication.models import *
from Users.serializers import * 

class List_Medication_Serializer(serializers.ModelSerializer):
       class Meta:
        model = List_Medication
        fields = ['medication_name','medication_description']  

class Patient_Medication_Serializer(serializers.ModelSerializer):
    # patient = PatientSerializer()
    medication = List_Medication_Serializer()
    class Meta:
        model = Patient_Medication
        fields = ['medication','instructions','dosage','dosage_time_hours']

class Taken_Medication_Serializer(serializers.ModelSerializer):
    patients_medication = Patient_Medication_Serializer()
    class Meta: 
        model = Taken_Medication
        fields = ['patients_medication','time_taken']