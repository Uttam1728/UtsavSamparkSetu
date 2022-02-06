from enum import IntEnum
from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator, MinValueValidator
from Mandal.models import MandalProfile


class SSPStage(IntEnum) :
    No= 0
    prarambh = 1,
    pravesh = 2,
    parichay = 3,
    paravin = 4,
    Pragn_1 = 5,
    Pragn_2 = 6,
    Pragn_3 = 7
class YuvakProfile(models.Model):
    FirstName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50)
    SurName = models.CharField(max_length=50)
    WhatsappNo = models.CharField(max_length=10, db_index=True)
    HomePhoneNo = models.CharField(max_length=10, null=True, blank=True)
    HouseNo = models.IntegerField(verbose_name="House/Flat No.")
    Soc_Name = models.CharField(max_length=50,verbose_name="Sociaty/Apartment Name")
    LandMark = models.CharField(max_length=100)
    Area = models.CharField(max_length=50)
    PinCode = models.CharField(max_length=6, null=True, blank=True)
    Married = models.BooleanField(default=False)
    DateOfBirth = models.DateField(blank=True,null=True)
    Education = models.CharField(max_length=100,blank=True,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True,)
    mandal = models.ForeignKey(MandalProfile,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.mandal.__str__() + ": "+ self.FirstName + " " + self.MiddleName + " " + self.SurName

class SatsangProfile(models.Model):
    yuvakProfile = models.OneToOneField(YuvakProfile,on_delete=models.CASCADE)
    NityaPuja = models.BooleanField(default=False)
    NityaPujaYear = models.IntegerField(validators=[MaxValueValidator(30)],default=0)
    TilakChandlo = models.BooleanField(default=False)
    TilakChandloYear = models.IntegerField(validators=[MaxValueValidator(30)],default=0)
    Satsangi = models.BooleanField(default=False)
    SatsangiYear = models.IntegerField(validators=[MaxValueValidator(30)],default=0)
    AthvadikSabha = models.BooleanField(default=False)
    AthvadikSabhaYear = models.IntegerField(validators=[MaxValueValidator(30)],default=0)
    Ravisabha = models.BooleanField(default=False)
    RavisabhaYear = models.IntegerField(validators=[MaxValueValidator(30)],default=0)
    GharSatsang = models.BooleanField(default=False)
    GharSatsangYear = models.IntegerField(validators=[MaxValueValidator(30)],default=0)
    SSP = models.BooleanField(default=False)
    SSPStage = models.IntegerField(
                default=SSPStage.No,
                choices=[(methods.value, methods.name) for methods in SSPStage]  # Choices is a list of Tuple
             )
    Ekadashi = models.BooleanField(default=False)
    EkadashiYear = models.IntegerField(validators=[MaxValueValidator(30)],default=0)
    Niymit_Vanchan = models.BooleanField(default=False)
    Niymit_VanchanYear = models.IntegerField(validators=[MaxValueValidator(30)],default=0)
    


    def __str__(self):
        return self.yuvakProfile.__str__()
