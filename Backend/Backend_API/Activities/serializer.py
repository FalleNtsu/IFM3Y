from rest_framework import serializers
from Activities.models import *
from Users.models import *
from Users.serializers import * 

class Proof_Activity_Type_Serializer(serializers.ModelSerializer):
   class Meta:
       model = Proof_Activities_Type
       fields = ['name']  

class Activity_Type_Serializer(serializers.ModelSerializer):
   class Meta:
       model = Activity_Types
       fields = ['name'] 

class Activities_Serializer(serializers.ModelSerializer):
    proof_type = Proof_Activity_Type_Serializer()
    activity_type = Activity_Type_Serializer()

    class Meta:
        model = Activities 
        fields = ['id', 'name','description','proof_type','activity_type']

class Assigned_Activities_Serializer(serializers.ModelSerializer):
    activity = Activities_Serializer()

    class Meta:
        model = Assigned_Activities
        fields = ['id', 'activity','patient_id', 'due_date','description','isCompleted']

class Proof_Activities_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Proof_Activities
        fields = ['filename','pathname']

class Completed_Activities_Serializer(serializers.ModelSerializer):
    proof = Proof_Activities_Serializer
    class Meta:
        model = Completed_Activities
        fields = ['assinged_activity','completion_date','proof']


