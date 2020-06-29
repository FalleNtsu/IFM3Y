from django.urls import re_path
from django.urls import path
from Users import views

urlpatterns = [
    # http://127.0.0.1:8000/api/user/login
    path('login', views.Login_User),
    # http://127.0.0.1:8000/api/user/add
    path('add', views.Add_User),
    # http://127.0.0.1:8000/api/user/remove
    path('remove', views.Remove_User),
    # http://127.0.0.1:8000/api/user/all
    path('all', views.List_All_Users),

    path('psychologist/<username>/patients', views.get_psychologist_patients),

    path('patient/<username>', views.get_patient),
    # http://127.0.0.1:8000/api/user/?uid=62
    re_path(r'^(?P<uid>)', views.List_Single_User), 
    
]