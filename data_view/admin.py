from django.contrib import admin

# Register your models here.
from .models import Data_view

#Pour que cela soit visible dans la console 
admin.site.register(Data_view)