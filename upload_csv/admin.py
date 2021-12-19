from django.contrib import admin

# Register your models here.
from .models import Upload_csv

#Pour que cela soit visible dans la console 
admin.site.register(Upload_csv)