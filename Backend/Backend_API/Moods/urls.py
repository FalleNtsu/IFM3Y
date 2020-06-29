from django.urls import re_path
from django.urls import path

from .views import GenericMoodsRetriveAPIView, MoodsRetriveAPIView, MoodsAddAPIView

urlpatterns = [
    # http://127.0.0.1:8000/api/mood/generic
    path('generic', GenericMoodsRetriveAPIView.as_view()),
    # http://127.0.0.1:8000/api/mood/{{username}}
    path('<username>', MoodsRetriveAPIView.as_view()),
    # http://127.0.0.1:8000/api/mood/{{username}}/add    
    path('<username>/add', MoodsAddAPIView.as_view())
]