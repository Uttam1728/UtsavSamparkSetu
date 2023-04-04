from enum import IntEnum

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models

from Mandal.models import MandalProfile


def Profile_Completion(obj):
    fields_names = [f.name for f in obj._meta.fields]
    completed = 0
    for field_name in fields_names:
        value = getattr(obj, field_name)
        completed += not (value is None or value == '')
    ratio = (completed / len(fields_names)) * 100

    return int(ratio)


class SSPStage(IntEnum):
    No = 0
    prarambh = 1,
    pravesh = 2,
    parichay = 3,
    paravin = 4,
    Pragn_1 = 5,
    Pragn_2 = 6,
    Pragn_3 = 7


class Interests(IntEnum):
    No = 0
    પ્રવક્તા = 1,
    સંગીત = 2,
    સાઉન્ડસિસ્ટમ = 3,
    નાટક = 4,
    વક્તૃત્વ = 5,
    હાજરી = 6,
    પ્રસાદ = 7
    ડેકોરેશન = 8
    સંપર્કકાર્યકાર = 9


class SevaVibhag(models.Model):
    name = models.CharField(max_length=255, )
    guj_name = models.CharField(max_length=255, verbose_name="Seva Name")
    yuvaks = models.ManyToManyField('YuvakProfile', blank=True, related_name='seva_yuvaks')
    leader = models.ForeignKey('YuvakProfile', blank=True, null=True, related_name='seva_leader',
                               on_delete=models.SET_NULL)

    def __str__(self):
        return self.guj_name


class YuvakProfile(models.Model):
    FirstName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50)
    SurName = models.CharField(max_length=50)
    WhatsappNo = models.CharField(max_length=10, db_index=True)
    HomePhoneNo = models.CharField(max_length=10, null=True, blank=True)
    HouseNo = models.IntegerField(verbose_name="House/Flat No.", null=True, blank=True)
    Soc_Name = models.CharField(max_length=50, verbose_name="Sociaty/Apartment Name", null=True, blank=True)
    LandMark = models.CharField(max_length=100, null=True, blank=True)
    Area = models.CharField(max_length=50, null=True, blank=True)
    PinCode = models.CharField(max_length=6, null=True, blank=True)
    Married = models.BooleanField(blank=True, null=True)
    DateOfBirth = models.DateField(blank=True, null=True)
    Education = models.CharField(max_length=100, blank=True, null=True)
    current_Education = models.BooleanField(blank=True, null=True, verbose_name='અભ્યાસ શરુ છે ?')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, )
    mandal = models.ForeignKey(MandalProfile, on_delete=models.CASCADE)
    Seva_Intrests = models.ManyToManyField(
        SevaVibhag, verbose_name="વિશેષ રસ", blank=True,
        help_text="જો આપને આમાંથી કોઈ વિભાગ માં રસ હોય તો એ સિલેક્ટ કરી શકશો"
        # Choices is a list of Tuple
    )
    ProfilePhoto = models.ImageField(
        upload_to='media/yuvak', blank=True, null=True)
    Email = models.EmailField(default="yuvak@utsavmandal.com")

    def get_absolute_url(self):
        return f"/admin/Yuvak/yuvakprofile/{self.pk}/"

    def __str__(self):
        return self.FirstName + " " + self.MiddleName + " " + self.SurName

    @property
    def progress(self):
        return Profile_Completion(self)

    def save(self):
        # if self.ProfilePhoto:
        #     self.ProfilePhoto = self.compressImage(self.ProfilePhoto)
        if self.pk:

            yuvak = YuvakProfile.objects.get(pk=self.pk)
            if yuvak.ProfilePhoto and self.ProfilePhoto:
                old_url = yuvak.ProfilePhoto.url.split('/')[-1]
                new_url = self.ProfilePhoto.url.split('/')[-1]
                if old_url != new_url:
                    yuvak.ProfilePhoto.delete(save=False)

        super(YuvakProfile, self).save()


class SatsangProfile(models.Model):
    yuvakProfile = models.OneToOneField(YuvakProfile, on_delete=models.CASCADE, )
    NityaPuja = models.BooleanField(blank=True, null=True, verbose_name='નિત્યપૂજા')
    NityaPujaYear = models.IntegerField(validators=[MaxValueValidator(30)], blank=True, null=True,
                                        verbose_name="નિત્યપૂજા કેટલા વર્ષથી")
    TilakChandlo = models.BooleanField(blank=True, null=True, verbose_name="તિલક ચાંદલો")
    TilakChandloYear = models.IntegerField(validators=[MaxValueValidator(30)], blank=True, null=True,
                                           verbose_name="તિલક ચાંદલો કેટલા વર્ષથી")
    Satsangi = models.BooleanField(blank=True, null=True, verbose_name="સત્સંગ")
    SatsangiYear = models.IntegerField(validators=[MaxValueValidator(30)], verbose_name="સત્સંગ કેટલા વર્ષથી",
                                       blank=True, null=True)
    AthvadikSabha = models.BooleanField(blank=True, null=True, verbose_name="અઠવાડિકસભા")
    AthvadikSabhaYear = models.IntegerField(validators=[MaxValueValidator(30)], verbose_name="અઠવાડિકસભા કેટલા વર્ષથી",
                                            blank=True,
                                            null=True)
    Ravisabha = models.BooleanField(blank=True, null=True, verbose_name="રવિસભા")
    RavisabhaYear = models.IntegerField(validators=[MaxValueValidator(30)], blank=True, null=True,
                                        verbose_name="રવિસભા કેટલા વર્ષથી")
    GharSatsang = models.BooleanField(blank=True, null=True, verbose_name="ઘરસત્સંગ")
    GharSatsangYear = models.IntegerField(validators=[MaxValueValidator(30)], blank=True, null=True,
                                          verbose_name="ઘરસત્સંગ કેટલા વર્ષથી")
    SSP = models.BooleanField(blank=True, null=True, verbose_name="સત્સંગ શિક્ષણ પરીક્ષા")
    SSPStage = models.IntegerField(
        default=SSPStage.No,
        choices=[(methods.value, methods.name) for methods in SSPStage], verbose_name="છેલ્લી પરીક્ષા"
        # Choices is a list of Tuple
    )
    Ekadashi = models.BooleanField(blank=True, null=True, verbose_name="એકાદશી")
    EkadashiYear = models.IntegerField(validators=[MaxValueValidator(30)], blank=True, null=True,
                                       verbose_name="એકાદશી કેટલા વર્ષથી")
    Niymit_Vanchan = models.BooleanField(blank=True, null=True, verbose_name="નિયમિત વાંચન",
                                         help_text="૧ વચનામૃત અને ૫ સ્વામીની વાતો અથવા પ્રમુખસ્વામી મહારાજ નું જીવન ચરિત્ર વાંચન")
    Niymit_VanchanYear = models.IntegerField(validators=[MaxValueValidator(30)], blank=True, null=True,
                                             verbose_name="નિયમિત વાંચન કેટલા વર્ષથી", )

    def __str__(self):
        return self.yuvakProfile.__str__()

    def get_absolute_url(self):
        return f"/admin/Yuvak/satsangprofile/{self.pk}/"

    @property
    def progress(self):
        return Profile_Completion(self)
