from django.db import models


class Classification(models.Model):
    title = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}-{self.serial_number}"

class LguEquipment(models.Model):

    CONDITION_CHOICES = [('Serviceable','Serviceable'),('Unserviceable','Unserviceable')]
    classification = models.ForeignKey(Classification,on_delete=models.CASCADE,related_name='equipments',null=True,blank=True)
    article = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    property_number = models.CharField(max_length=50, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=50)  # e.g., "MTO", "SB", "MEO"
    condition = models.CharField(max_length=20,choices=CONDITION_CHOICES,default='Serviceable')  # Add choices if needed
    remarks = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.article} - {self.property_number}"


