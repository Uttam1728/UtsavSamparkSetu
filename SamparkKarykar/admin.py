from django.contrib import admin
from Common.util import is_member

from SamparkKarykar.models import KaryakarProfile



class KaryakarProfileAdmin(admin.ModelAdmin):
    list_display = ("__str__", "Whatsapp_no", "user")

    def get_queryset(self, request):
        qs = super(KaryakarProfileAdmin, self).get_queryset(request) 
        if request.user.is_superuser:
            return qs
        elif is_member(request.user,"Yuvak"):
            return request.user.yuvakprofile_set.all()[0].karyakarprofile_set
        else:
            return qs.filter(user=request.user)

    def Whatsapp_no(self,obj):
        return obj.profile.WhatsappNo

# Register your models here.
admin.site.register(KaryakarProfile,KaryakarProfileAdmin)