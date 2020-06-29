# import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt  # Cookies exception
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from rest_framework.generics import RetrieveAPIView, CreateAPIView, DestroyAPIView
from rest_framework.views import APIView

# Custom Imports
from API.response import Response
from Users.models import Patient_User, User
from Activities.models import *
from Activities.serializer import * 

class ActivityTypesRetrieveAPIView(RetrieveAPIView):
    serializer_class = Activity_Type_Serializer

    def retrieve(self, request, *args, **kwargs):
        activity_types = Activity_Types.objects.filter() # Get all the Activity types 
        serializer = self.serializer_class(activity_types, many = True) # Pass all activities to serializer
        resp = Response(True, None, serializer.data)
        return JsonResponse(resp.to_json(), status = status.HTTP_200_OK)

class ActivityProofTypeAPIView(RetrieveAPIView):
    serializer_class = Activity_Type_Serializer

    def retrieve(self, request, *args, **kwargs):
        activity_proof_types = Proof_Activities_Type.objects.filter()  # return all activity proof
        serializer = self.serializer_class(activity_proof_types, many = True)
        resp = Response(True,None, serializer.data)
        return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)

class AddActivityAPIView(CreateAPIView):
    serializer_class = Activities_Serializer

    def create(self, request, *args, **kwargs):
         # Get values from request
        name = request.data.get('activity_name')
        
        activity_desc = request.data.get('description')

        activity_proof_type = {
            'name' : request.data.get('proofType')
        } # Get name of proof Type 
        activity_type = {
            'name' : request.data.get('activityType')
        } # Get name of activity Type 

        # Put data in an object for the serializer
        serializerData = {
            'name' : name, 
            'description' : activity_desc, 
            'proof_type' : activity_proof_type,
            'activity_type' : activity_type
        }

        # Give the data to the serializer
        serializer = self.serializer_class (data = serializerData)

        if not serializer.is_valid():
            resp = Response(False, 'Incorrect data sent to API')
            return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)

        try:
            # Get proof and activity Type 
            prf_type = Proof_Activities_Type.objects.get(name = activity_proof_type.get('name'))
            act_type = Activity_Types.objects.get(name = activity_type.get('name'))
            AddAct = Activities.objects.create(
                name = name,
                description = activity_desc,
                proof_type = prf_type,
                activity_type = act_type,
            )

            AddAct.save() # Add newly created Activity

            # Response to Created Activity 
            resp = Response(True, 'Mood Added Succsefully', payload = serializer.data)
            return JsonResponse(resp.to_json(), status=status.HTTP_200_OK) 

        except Proof_Activities_Type.DoesNotExist: 
            resp = Response(False, "No Activity Proof Found")
            return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)
        
        except Activity_Types.DoesNotExist:
            resp = Response(False, "No Activity Type Found")
            return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)

class GetAssignedActivitesAPIView(RetrieveAPIView):
    serializer_class = Assigned_Activities_Serializer
    
    def retrieve(self, request, username, *args, **kwargs):
        try:
            user = User.objects.get(username=username)
            patient = Patient_User.objects.get(user=user)

        except Patient_User.DoesNotExist:
            resp = Response(False, "No Pateint with the username {}".format(username))
            return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)
        
        assigned_act = Assigned_Activities.objects.filter(patient_id = patient.user_id) # Get all the Activity types 
        serializer = self.serializer_class(assigned_act, many = True) # Pass all activities to serializer
        resp = Response(True, None, serializer.data)
        return JsonResponse(resp.to_json(), status = status.HTTP_200_OK)

class GetSpecificAssignedActivitesAPIView(RetrieveAPIView):
    serializer_class = Assigned_Activities_Serializer
    
    def retrieve(self, request, username, activity_id, *args, **kwargs):
        try:
            user = User.objects.get(username=username)
            patient = Patient_User.objects.get(user=user)
            
            assigned_act = Assigned_Activities.objects.filter(patient_id = patient.user_id).get(id = activity_id) # Get all the Activity types 
            serializer = self.serializer_class(assigned_act) # Pass all activities to serializer
            resp = Response(True, None, serializer.data)
            return JsonResponse(resp.to_json(), status = status.HTTP_200_OK)

        except Patient_User.DoesNotExist:
            resp = Response(False, "No Pateint with the username {}".format(username))
            return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)

        except Assigned_Activities.DoesNotExist:
            resp = Response(False, "No assinged activities with the id {}".format(activity_id))
            return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)
        
class UnassignAssignedActivityAPIView(APIView):       
    serializer_class = Assigned_Activities_Serializer

    def post(self, request, *args, **kwargs):
        # TODO: do verfication checks such as if the patient belongs to a specifc psychologist
        assignedID = request.data.get('assigned_activity_id')
        
        assigned_act = Assigned_Activities.objects.get(id = assignedID).delete() # Get all the Activity types 
        
        resp = Response(True, "Succesfully unassinged activity", None)
        return JsonResponse(resp.to_json(), status = status.HTTP_200_OK)

class GetActivitesAPIView(RetrieveAPIView):
    serializer_class = Activities_Serializer
    
    def retrieve(self, request, *args, **kwargs):
        try:    
            activities = Activities.objects.filter() # Get all the Activity types 
            serializer = self.serializer_class(activities, many = True) # Pass all activities to serializer
            resp = Response(True, None, serializer.data)
            return JsonResponse(resp.to_json(), status = status.HTTP_200_OK)

        except Patient_User.DoesNotExist:
            resp = Response(False, "No Pateint with the username {}".format(username))
            return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)

        except Assigned_Activities.DoesNotExist:
            resp = Response(False, "No assinged activities with the id {}".format(username))
            return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)