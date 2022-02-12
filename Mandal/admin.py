from urllib import request
from django.contrib import admin
from Common.util import getMandal, is_member,is_followUpDone, messageIcons
from datetime import date, datetime
from django.db.models import Q
from django.utils.translation import gettext as _
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from FolloWUp.models import FollowUp, FollowupStatus
from Mandal.models import Karyakram, MandalProfile
from Yuvak.models import YuvakProfile

# Register your models here.

class KaryakramAdmin(admin.ModelAdmin):
    change_form_template = "admin/karyakram_change_form.html"
    
    
    
    list_display = ("__str__", "Karyakram_date", "is_active", "For_All","Start_date","End_date")
    # fieldsets = (("KaryKram Details", {'fields': ('Title', 'is_active', 'Start_date', 'End_date', 'Mandal', 'For_All')}),
    #              ("Yuvak FollowUp", {"fields": ("custom_actions", )}),
    #              )
    # readonly_fields = ('custom_actions',)


    def get_queryset(self, request):
        qs = super(KaryakramAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(Mandal=getMandal(request.user))
        else:
            mandal = getMandal(request.user)
            curr_date = datetime.now()
            return qs.filter(Q(Mandal=mandal) & 
                            Q(End_date__gte=curr_date) & 
                            Q(is_active=True)).order_by('Karyakram_date')
        

    def save_model(self, request, obj, form, change):
        if "_followup_record_create" in request.POST:
            if obj.pk:
                for karyakar_vrund in obj.Mandal.karyakarprofile_set.all():
                    for yuvak in karyakar_vrund.Yuvaks.all():
                        FollowUp.objects.get_or_create(Karyakram=obj,
                                        KaryKarVrund=karyakar_vrund,
                                        Yuvak=yuvak)
            else:
                msg = format_html(_('Please save karykram first.'))
                self.message_user(request, msg, messages.WARNING)
                return HttpResponseRedirect("/admin/Mandal/karyakram")
        else:
            return super().save_model(request, obj, form, change)

class MandalProfileAdmin(admin.ModelAdmin):
    # change_list_template = 'admin/mandal_change_list.html'
    list_display = ("__str__", "Nirikshak_details", "Sanchalak_details",)
    list_per_page = 20

    def Nirikshak_details(self,obj):
        if obj.Nirikshak : 
            return format_html(obj.Nirikshak.FirstName + " " +obj.Nirikshak.SurName +" : "+ messageIcons(obj.Nirikshak.WhatsappNo,20))
        return ''
    def Sanchalak_details(self,obj):
        if obj.Sanchalak:
            return format_html(obj.Sanchalak.FirstName + " " +obj.Sanchalak.SurName +" : " + messageIcons(obj.Nirikshak.WhatsappNo,20))
        return ''
        
admin.site.register(MandalProfile,MandalProfileAdmin)
admin.site.register(Karyakram,KaryakramAdmin)