from django.db import models
from Users.models import Patient_User # Patient Model import
# Create your models here.

class Proof_Activities_Type(models.Model):
    id = models.AutoField( primary_key = True ) 
    name = models.CharField(max_length= 255, null = True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class Activity_Types(models.Model):
    id = models.AutoField(primary_key = True )
    name = models.CharField(max_length= 255, null = True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class Activities(models.Model):
    id = models.AutoField(primary_key = True )
    # patient_activities = models.ForeignKey(Patient_User, on_delete= models.CASCADE,  default = 1) 
    name = models.CharField(max_length= 255, null= True)
    description = models.CharField(max_length= 255 , null = True)
    proof_type = models.ForeignKey(Proof_Activities_Type, default = 1 , on_delete = models.CASCADE)
    activity_type = models.ForeignKey(Activity_Types, default = 1 , on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class Assigned_Activities(models.Model) :
    id = models.AutoField(primary_key = True )
    activity = models.ForeignKey(Activities, default = 1 , on_delete= models.CASCADE)
    patient = models.ForeignKey(Patient_User , default = 1, on_delete= models.CASCADE)
    due_date = models.DateTimeField(blank = True)
    description = models.CharField(max_length= 255 , null = True)
    isCompleted = models.BooleanField(null = True )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class Proof_Activities(models.Model) : 
    id = models.AutoField(primary_key = True)
    filename = models.CharField(max_length= 255)
    pathname = models.CharField(max_length= 255) 
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class Completed_Activities(models.Model):
    assinged_activity = models.ForeignKey(Assigned_Activities, primary_key = True, default = 1 , on_delete= models.CASCADE)
    completion_date = models.DateTimeField(auto_now_add= True)
    proof = models.ForeignKey(Proof_Activities, default = 1, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

