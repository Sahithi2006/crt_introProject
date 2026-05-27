from django.urls import path
from .views import  greet,get_name,details
#http://127.0.0.1:8000/user/message

#http://127.0.0.1:8000/user/name
#http://127.0.0.1:8000/user/data

urlpatterns=[
    path("message",greet),
    path("name", get_name),
    path("data",details),
]
