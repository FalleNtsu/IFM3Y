from django.db import models
import datetime
# from Login.models import UserLogin


# class to store data on user
class User(models.Model):
    user_id = models.AutoField(primary_key= True)
    username = models.CharField(max_length = 255, null = True)
    email_address = models.CharField(max_length = 255, null = True)
    password = models.CharField(max_length = 255, null = True)
    title = models.CharField(max_length = 255, null = True)
    first_name = models.CharField(max_length = 255, null = True)
    surname = models.CharField(max_length = 255, null = True)
    cell_number = models.CharField(max_length = 255, null = True)
    date_of_birth = models.DateTimeField(auto_now=True, null = True)
    gender = models.CharField(max_length = 255, null = True)
    primary_address = models.CharField(max_length = 255, null = True)
    city = models.CharField(max_length = 255, null = True)
    postal_code = models.CharField(max_length = 255, null = True)
    country = models.CharField(max_length = 255, null = True)
    citizenship = models.CharField(max_length = 255, null = True)
    is_inactive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

# class for storing the data for roles
class Roles(models.Model):
    role_id = models.AutoField(primary_key= True) 
    role_name = models.CharField(max_length = 255, null = True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

# class for storing the roles that the user has
class User_Roles(models.Model):
    user_role_id = models.AutoField(primary_key= True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, default = 1)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, null = True,  default = 1)

class Psychologist_User(models.Model):
    # psychologist_id = models.ForeignKey(primary_key = True, max_length= 255 , null = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default = 1)
    practitioners_id = models.CharField(max_length= 255, null = True)
    practice_address = models.CharField(max_length= 255, null = True)
    practice_work_number = models.CharField(max_length= 255, null = True)
    practice_email = models.CharField(max_length= 255, null = True)
    isProcessed = models.BooleanField(default=False)
    isApproved = models.BooleanField(default=False)

class Diagnosis(models.Model):
    diagnosis_id = models.AutoField(primary_key= True)
    name = models.CharField(max_length = 255, null = True)
    description = models.CharField(max_length = 255, null = True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class Patient_User(models.Model):
    # patient_id = models.CharField(max_length= 255, null = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default = 1)
    psychologist = models.ForeignKey(Psychologist_User, on_delete= models.CASCADE , null = True,  default = 1 )
    diagnosis = models.ForeignKey(Diagnosis, on_delete= models.CASCADE , null = True,  default = 1 )