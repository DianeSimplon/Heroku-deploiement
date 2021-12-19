from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.forms import fields
from django.forms import Form
import pandas as pd

import csv
import pickle
from io import StringIO


# Create your views here.
def chargement(request):
    if not request.FILES:
        return HttpResponse("Pas de fichier")

  
    file = request.FILES["csv_file"]
    data = pd.read_csv(file, sep=",")
    data = data[["id_lot", "nb_piece", "prix_tva_normale", "prix_HT", "prix_m2_HT"]]
    #f = open('static/immobilier.csv', 'wb')
    data.to_csv('static/immobilier.csv')
    #p = pickle.Pickler(f)
    #p.dump(file)
    #f.close()
    indicateur(data['prix_HT'])
    #html = data.to_html()
    return render(request, "data_view/data_views.html", {"columns":data.columns, "data":data.values.tolist()})
    #return HttpResponse(html)

def indicateur(series: pd.Series):
    if series.dtype == 'int64' or series.dtype=='float64':
        print('mean : \t', series.mean())
        print("****************************************")
        print('variance:  \t', series.var())
        print("****************************************")
        print('std : \t', series.std())
        print("****************************************")
        print('median : \t', series.median())
        print("****************************************")
        print('iqr : \t', series.quantile(0.75) - series.quantile(0.25))
        print("****************************************")
        print('mode : \t', series.mode().values)
        print("****************************************")
        print('skewness: : \t', series.skew())
        return     
