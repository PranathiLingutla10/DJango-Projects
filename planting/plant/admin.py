from django.contrib import admin
from .models import Plant_Details

# Register your models here.
@admin.register(Plant_Details)
class Plantadmin(admin.ModelAdmin):
    list_display=('plant_name','plant_type','plant_price','plant_benefit')
