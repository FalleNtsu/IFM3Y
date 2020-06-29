from rest_framework import serializers
from Users.models import *

#  Defines what gets serialized and deserialized 
class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email_address','password','title',
        'first_name','surname','cell_number','date_of_birth','gender','primary_address',
        'city','postal_code','country','citizenship']

class RemoveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ['name','description']

class PsychologistSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Psychologist_User
        fields = ['user', 'practitioners_id','practice_address','practice_work_number','practice_email','isProcessed','isApproved']

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    psychologist = PsychologistSerializer()
    diagnosis = DiagnosisSerializer()
    class Meta:
        model = Patient_User
        fields = ['user','psychologist','diagnosis']