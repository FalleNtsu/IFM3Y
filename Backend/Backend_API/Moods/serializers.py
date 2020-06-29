from rest_framework import serializers
from Moods.models import *
from Users.models import *
from Users.serializers import * 

class Generic_MoodSerializer(serializers.ModelSerializer):
   class Meta:
       model = Generic_Moods
       fields = ['name'] 

class Patient_MoodSerializer(serializers.ModelSerializer):
    generic_mood = Generic_MoodSerializer()
    # patient = PatientSerializer()
    # TODO: Review patient usage in this serializer
    class Meta: 
        model = Patient_Mood
        fields = ['generic_mood','logged_time','description']
