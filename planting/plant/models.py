from django.db import models

# Create your models here.
class Plant_Details(models.Model):
    plant_name=models.CharField(max_length=20)
    plant_type=models.CharField(max_length=20)
    plant_price=models.FloatField()
    plant_benefit=models.CharField(max_length=100)
    def __str__(self):
        return str(self.id)+","+str(self.plant_type)+","+str(self.plant_price)+","+str(self.plant_benefit)
