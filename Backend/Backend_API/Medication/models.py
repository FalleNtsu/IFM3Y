from django.db import models
from Users.models import Patient_User # Patient Model import
# Create your models here.

class List_Medication(models.Model):
    id = models.AutoField(primary_key = True )
    medication_name = models.CharField(max_length= 255, null = True)
    medication_description = models.CharField(max_length= 255, null = True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class Patient_Medication(models.Model):
    id = models.AutoField(primary_key = True)
    medication = models.ForeignKey(List_Medication, default = 1 , on_delete = models.CASCADE)
    patient = models.ForeignKey(Patient_User, default = 1, on_delete = models.CASCADE)
    instructions = models.CharField(max_length= 255 , null = True)
    dosage = models.IntegerField( default = 1 )
    dosage_time_hours = models.DecimalField(max_digits= 3, decimal_places= 2)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class Taken_Medication(models.Model):
    id = models.AutoField( primary_key = True ) 
    patients_medication = models.ForeignKey(Patient_Medication,default = 1 , on_delete = models.CASCADE)
    time_taken = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)




