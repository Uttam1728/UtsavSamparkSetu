from django.db import models

# Create your models here.

class MandalProfile(models.Model):
    Name = models.CharField(max_length=100)
    Area = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name +" - "  + self.Area

