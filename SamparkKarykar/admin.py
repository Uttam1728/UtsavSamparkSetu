from django.contrib import admin

from Common.util import getMandal, is_member

from SamparkKarykar.models import KaryakarProfile

from django.utils.html import format_html
from django.contrib import admin


from django.utils.html import format_html
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group

from django.utils.translation import gettext as _

@receiver(post_save, sender=KaryakarProfile)
def Add_KaryKarGroup(sender, instance, **kwargs):
    if instance.profile.user is not None:
        user = instance.profile.user
        if not user.groups.filter(name="Sampark Karykar").exists():
            group = Group.objects.get(name='Sampark Karykar')
            user.groups.add(group)   


class KaryakarProfileAdmin(admin.ModelAdmin):
    
    change_list_template = 'admin/karykar_change_list.html'
    
    list_display = ("__str__", "WhatsApp","Call","SMS","username")

    def WhatsApp(self,obj):
        buttons = ''
        buttons += "<a href='https://wa.me/+91{}' ><i class='fa fa-whatsapp' style='font-size:30px;color:green'></i></a>".format(obj.profile.WhatsappNo)
        return format_html(buttons)

    def Call(self,obj):
        buttons = ''
        buttons += "<a href='tel:+91{}'> <i class='fa fa-volume-control-phone' style='font-size:27px;color:deepskyblue;'></i> </a>".format(obj.profile.WhatsappNo)
        return format_html(buttons)
    
    def SMS(self,obj):
        buttons = ''
        buttons += "<a href='sms:+91{}'> <i class='fa fa-commenting-o' style='font-size:27px;color:lightblue;'></i> </a>".format(obj.profile.WhatsappNo)  
        return format_html(buttons)
    
    def username(self,obj):
        return obj.profile.user

    def get_queryset(self, request):
        qs = super(KaryakarProfileAdmin, self).get_queryset(request) 
        if request.user.is_superuser:
            return qs.filter(profile__mandal=getMandal(request.user))
        elif is_member(request.user,"Sampark Karykar"):
            return qs.filter(profile=request.user.yuvakprofile)
        elif is_member(request.user,"Yuvak"):
            return request.user.yuvakprofile.karyakarprofile_set
        
    def Whatsapp_no(self,obj):
        return obj.profile.WhatsappNo

# Register your models here.
admin.site.register(KaryakarProfile,KaryakarProfileAdmin)