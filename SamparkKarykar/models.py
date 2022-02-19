from django.db import models

from Mandal.models import MandalProfile
from Yuvak.models import YuvakProfile


class KaryakarProfile(models.Model):
    karykar1profile = models.OneToOneField(YuvakProfile, on_delete=models.CASCADE, related_name="Profile1Info")
    karykar2profile = models.OneToOneField(YuvakProfile, on_delete=models.CASCADE, null=True, blank=True,
                                           related_name="Profile2Info")
    Yuvaks = models.ManyToManyField(YuvakProfile, blank=True, )
    mandal = models.ForeignKey(MandalProfile, on_delete=models.CASCADE)

    def __str__(self):
        return "Vrund No : " + str(self.pk)

    class Meta:
        verbose_name = "KaryKar Vrund"
