# import requests
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
from Moods.models import Patient_Mood, Generic_Moods
from Moods.serializers import Patient_MoodSerializer, Generic_MoodSerializer

class GenericMoodsRetriveAPIView(RetrieveAPIView):
    serializer_class = Generic_MoodSerializer

    def retrieve(self, request, *args, **kwargs):
        genericMoods = Generic_Moods.objects.filter()

        serializer = self.serializer_class(genericMoods, many=True)
        resp = Response(True, None, serializer.data)
        return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)

class MoodsRetriveAPIView(RetrieveAPIView):
    serializer_class = Patient_MoodSerializer

    def retrieve(self, request, username, *args, **kwargs):
        try:
            user = User.objects.get(username=username)
            patient = Patient_User.objects.get(user=user)
            moods = Patient_Mood.objects.filter(patient=patient)

        except Patient_User.DoesNotExist:
            resp = Response(False, "No Pateint with the username {}".format(username))
            return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)

        serializer = self.serializer_class(moods, many=True)
        resp = Response(True, None, serializer.data)
        return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)
        

class MoodsAddAPIView(CreateAPIView):
    serializer_class = Patient_MoodSerializer

    def create(self, request, username):
        # Get values from request
        genericMood = {
            'name' : request.data.get('generic_mood')
        }
        loggedTime = request.data.get('logged_time')
        description = request.data.get('description')

        # Put data in an object for the serializer
        serializerData = {
            'generic_mood' : genericMood, 
            'logged_time' : loggedTime, 
            'description' : description
        }

        # Give the data to the serializer
        serializer = self.serializer_class(data=serializerData)

        if not serializer.is_valid():
            resp = Response(False, 'Incorrect data sent to API')
            return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)

        try:
            # get patient user
            user = User.objects.get(username=username)
            patient = Patient_User.objects.get(user=user)
            # get the generic Mood 
            generic_mood = Generic_Moods.objects.get(name=genericMood.get('name'))

            # Create patient mood
            patientMood = Patient_Mood.objects.create(
                generic_mood = generic_mood,
                patient = patient,
                logged_time = loggedTime,
                description = description
            )

            # Save pateint mood that has been created
            patientMood.save() 

            # give succesful response
            resp = Response(True, 'Mood Added Succsefully', payload = serializer.data)
            return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)   

        except Patient_User.DoesNotExist: # if the patient does not exsists 
            # Giver error response
            resp = Response(False, "No Pateint with the username {}".format(username))
            return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)
        except Generic_Moods.DoesNotExist: # if the generic mood does not exsists 
            # Giver error response
            resp = Response(False, "Generic Mood does not exsist")
            return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)
        
            