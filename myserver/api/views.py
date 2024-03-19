from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.



def handshakeCheckView(request):


    return HttpResponse("server - api : is up and running! ... port 8000 ...")



