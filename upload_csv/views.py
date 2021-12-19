from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render
from django.forms import fields
from django.forms import Form




# Create your views here.
def home(request):
    #retourne une reponse par rapport au lien
    return render(request, "upload_csv/acceuil.html")

