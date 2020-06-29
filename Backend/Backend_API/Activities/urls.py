from django.urls import re_path
from django.urls import path

from .views import *

urlpatterns = [
    #Types 
    # http://127.0.0.1:8000/api/activity/
    path('activityTypes', ActivityTypesRetrieveAPIView.as_view()),
    path('proofTypes', ActivityProofTypeAPIView.as_view()),
    # Add Activity 
    path('add', AddActivityAPIView.as_view()),
    path('<username>/assigned', GetAssignedActivitesAPIView.as_view()),
    path('<username>/assigned/<activity_id>', GetSpecificAssignedActivitesAPIView.as_view()),
    path('unassign', UnassignAssignedActivityAPIView.as_view()),
    path('all', GetActivitesAPIView.as_view()),
    # http://127.0.0.1:8000/api/mood/{{username}}/add    
    # path('<username>/add', MoodsAddAPIView.as_view())
    # api/activity/activityTypes
]