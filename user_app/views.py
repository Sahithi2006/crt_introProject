from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#http://127.0.1:8000/user/message
def greet(request):
    return HttpResponse("Hii , good morning")
def get_name(request):
    return HttpResponse("my name is sahithi")

def details(request):
    return HttpResponse([{
"name": "amit",
"email":"amit@gmail.com",
"address":"hyd"
},
{
"name": "hanu",
"email":"hanu@gmail.com",
"address":"hyd",
}])