from django.contrib import admin

from Common.util import getMandal, is_member, messageIcons

from SamparkKarykar.models import KaryakarProfile

from django.utils.html import format_html
from django.contrib import admin


from django.utils.html import format_html
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.db.models import Q
from django.utils.translation import gettext as _

@receiver(post_save, sender=KaryakarProfile)
def Add_KaryKarGroup(sender, instance, **kwargs):
    if instance.karykar1profile:
        user = instance.karykar1profile.user
        if not user.groups.filter(name="Sampark Karykar").exists():
            group = Group.objects.get(name='Sampark Karykar')
            user.groups.add(group)   
    if instance.karykar2profile:
        user = instance.karykar2profile.user
        if not user.groups.filter(name="Sampark Karykar").exists():
            group = Group.objects.get(name='Sampark Karykar')
            user.groups.add(group)  


class KaryakarProfileAdmin(admin.ModelAdmin):
    
    # change_list_template = 'admin/karykar_change_list.html'
    list_display = ("__str__","SamparkKarykar1", "SamparkKarykar2","Yuvak_List") # "WhatsApp","Call","SMS","username")
    list_per_page = 20
    autocomplete_fields = ('karykar1profile', 'karykar2profile', 'Yuvaks')
    search_fields = ('karykar1profile__FirstName__icontains','karykar1profile__SurName__icontains','karykar2profile__FirstName__icontains','karykar2profile__SurName__icontains','Yuvaks__FirstName__icontains','Yuvaks__FirstName__icontains')

    def SamparkKarykar1(self,obj):
        if obj.karykar1profile : 
            return format_html(obj.karykar1profile.FirstName + " " +obj.karykar1profile.SurName +" <br> "+ messageIcons(obj.karykar1profile.WhatsappNo,20,False))
        return ''

    def SamparkKarykar2(self,obj):
        if obj.karykar2profile : 
            return format_html(obj.karykar2profile.FirstName + " " +obj.karykar2profile.SurName +" <br> "+ messageIcons(obj.karykar2profile.WhatsappNo,20,False))
        return ''

    def Yuvak_List(self,obj):
        s = ''
        for yuvak in obj.Yuvaks.all():
            s += '<li>{} {}</li>'.format(yuvak.FirstName,yuvak.SurName)  #+ messageIcons(yuvak.WhatsappNo,20)
        return format_html(s)
    

    def get_queryset(self, request):
        qs = super(KaryakarProfileAdmin, self).get_queryset(request) 
        mandal = getMandal(request.user)
        if request.user.is_superuser:
            return qs.filter(Q(karykar1profile__mandal=mandal) | Q(karykar2profile__mandal=mandal))
        elif is_member(request.user,"Sampark Karykar"):
            return qs.filter(Q(karykar1profile=request.user.yuvakprofile) | Q(karykar2profile=request.user.yuvakprofile))
        elif is_member(request.user,"Yuvak"):
            return request.user.yuvakprofile.karyakarprofile_set
     
    def change_view(self, request, object_id, form_url='', extra_context=None):
        if not request.user.is_superuser:
            self.readonly_fields = ["Yuvaks","karykar1profile","karykar2profile","mandal"]
        else:
            self.readonly_fields = []
        return super().change_view(request, object_id, form_url, extra_context)

# Register your models here.
admin.site.register(KaryakarProfile,KaryakarProfileAdmin)