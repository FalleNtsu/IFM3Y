# import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt  # Cookies exception
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from Users.models import User, User_Roles, Roles, Psychologist_User, Patient_User
from Users.serializers import LoginUserSerializer
from Users.serializers import UserSerializer
from Users.serializers import RemoveUserSerializer
from Users.serializers import PatientSerializer
from API.response import Response
import hashlib  # For password hashing

#  Check that passwords match for username 
def authenticate(request,obj,username,password):
    Valid = False # Validity Flag 
    if obj is not None:
        passw = hashlib.sha256(password.encode()).hexdigest() 
        if obj.password == passw and obj.username == username :
          Valid = True
          return Valid
    return Valid
       
    
@csrf_exempt
@api_view(['POST']) 
def Login_User(request):
        if request.method == 'POST':
            try:
                data = JSONParser().parse(request)
                serializer = LoginUserSerializer(data=data)  # Which data to base request on 
                if serializer.is_valid():
                    username = serializer.data.get('username')
                    password = serializer.data.get('password') 
                    user = User.objects.get(username=username) 
                    if user:
                        valid_user = authenticate(request,user,username = username, password = password)
                        if valid_user:
                            user_role = User_Roles.objects.get(user_id= user.user_id)
                            role =  user_role.role.role_name
                            payload = {"username" : user.username , "role" : role}
                            resp = Response(valid_user, "Login Successful",payload= payload)
                            return JsonResponse(resp.to_json(), status =status.HTTP_200_OK)
                        else:
                            resp = Response(valid_user, "Username and / or password is incorrect")
                            return JsonResponse(resp.to_json(), status =status.HTTP_200_OK)
                else:
                    resp = Response(False, "Incorrect data/invalid format sent to API")
                    return JsonResponse(resp.to_json(), status = status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                resp = Response(False, 'Username and/or password is incorrect')
                return JsonResponse(resp.to_json(),status=status.HTTP_200_OK)



# validate username and see if it already exists
def valid_username(request, username):
    Valid = False
    users = User.objects.filter(username=username).count()
    if users > 1:
        return Valid
    elif users < 1:
        Valid = True
    return Valid


@csrf_exempt
@api_view(['POST'])
def Add_User(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.validated_data['password'] = hashlib.sha256(
                serializer.validated_data['password'].encode()).hexdigest()
            username = serializer.validated_data['username']
            if valid_username(request, username):
                serializer.save()
                resp = Response(True, 'User \'{}\''.format(username)+' Added succesfully')
                return JsonResponse(resp.to_json(), status=status.HTTP_201_CREATED)
            resp = Response(False, 'Username \'{}\''.format(username)+' Already taken')
            return JsonResponse(resp.to_json(), status=status.HTTP_200_OK)
        else:
            resp = Response(False, "Incorrect data/invalid format sent to API")
            return JsonResponse(resp.to_json(), status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def Remove_User(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RemoveUserSerializer(data=data)
        # usern = request['username']
        if serializer.is_valid():
            username = serializer.validated_data['username']
            user = User.objects.get(username=username)
            user.is_inactive = True
            user.save()
            resp = Response(True, 'User \'{}\''.format(username)+' set inactive')
            return JsonResponse(resp.to_json(), status=status.HTTP_201_CREATED)
        else:
            resp = Response(False, "Incorrect data/invalid format sent to API")
            return JsonResponse(resp.to_json(), status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['GET'])
def List_All_Users(request):
    if request.method == 'GET':
        user = User.objects.filter(is_inactive=False)  # Get all User Data 
        serializer = UserSerializer(user, many=True)  # Passes user to the serializer
        resp = Response(True, None, serializer.data)
        return JsonResponse(resp.to_json(), safe=False)  # Return Data 

@csrf_exempt
@api_view(['GET'])
def List_Single_User(request, uid):
    if request.method == 'GET':
        username = request.GET['un']
        try:
            user = User.objects.get(username=username) # Get all User Data 
            serializer = UserSerializer(user, many=False)  # Passes user to the serializer
            resp = Response(True, None, serializer.data)
            return JsonResponse(serializer.data, safe=False)  # Return Data 
        except User.DoesNotExist:
                resp = Response(False, 'User \'{}\''.format(username)+' does not exist')
                return JsonResponse(resp.to_json(),status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(['GET'])
def get_psychologist_patients(request, username):
    if request.method == 'GET':
        try:
            patients = Patient_User.objects.filter(psychologist__user__username=username) # Get all the patients from a specifc psychologist 

            serializer = PatientSerializer(patients, many=True)  # Passes patients to the serializer
            resp = Response(True, None, serializer.data)
            return JsonResponse(resp.to_json(), safe=False)  # Return Data 
        except Patient_User.DoesNotExist:
                resp = Response(False, 'User \'{}\''.format(username)+' does not exist')
                return JsonResponse(resp.to_json(),status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['GET'])
def get_patient(request, username):
    if request.method == 'GET':
        try:
            patients = Patient_User.objects.get(user__username=username) # Get all the patients from a specifc psychologist 

            serializer = PatientSerializer(patients, many=False)  # Passes patients to the serializer
            resp = Response(True, None, serializer.data)
            return JsonResponse(resp.to_json(), safe=False)  # Return Data 
        except Patient_User.DoesNotExist:
                resp = Response(False, 'User \'{}\''.format(username)+' does not exist')
                return JsonResponse(resp.to_json(),status=status.HTTP_404_NOT_FOUND)
