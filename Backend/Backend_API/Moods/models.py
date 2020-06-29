from django.db import models
from Users.models import * 

# Create your models here.

class Generic_Moods(models.Model):
    generic_mood_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length= 255 , null = True )
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)
    
class Patient_Mood(models.Model):
    patient_mood_id = models.AutoField(primary_key = True)
    generic_mood = models.ForeignKey(Generic_Moods, default = 1, on_delete= models.CASCADE)
    patient = models.ForeignKey(Patient_User, on_delete= models.CASCADE,  default = 1)  # Get the Patient user ID
    logged_time = models.DateTimeField(blank = True)
    description = models.CharField(max_length = 255 , null = True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)
