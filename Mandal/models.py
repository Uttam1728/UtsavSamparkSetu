from django.db import models

# from Yuvak.models import YuvakProfile

# from SamparkKarykar.models import KaryakarProfile
# from Yuvak.models import YuvakProfile

# Create your models here.

class MandalProfile(models.Model):
    Name = models.CharField(max_length=100)
    Area = models.CharField(max_length=100)
    Nirikshak = models.ForeignKey('Yuvak.YuvakProfile',on_delete=models.DO_NOTHING,related_name="nirikshak",blank=True,null=True)
    Sanchalak = models.ForeignKey('Yuvak.YuvakProfile',on_delete=models.DO_NOTHING,related_name="sanchalak",blank=True,null=True)
    
    def __str__(self):
        return self.Name +" - "  + self.Area

class Karyakram(models.Model):
    Title = models.CharField(max_length=1000)
    Start_date = models.DateTimeField(blank=True,null=True,verbose_name="Followup Start Date")
    End_date = models.DateTimeField(blank=True,null=True,verbose_name="Followup End Date")
    Karyakram_date=models.DateTimeField(blank=True,null=True)
    Mandal = models.ForeignKey(MandalProfile,blank=True,null=True,on_delete=models.CASCADE)
    Start_Folloup = models.BooleanField(default=False)
    Start_Attandance = models.BooleanField(default=False)
    def __str__(self):
        return self.Title


