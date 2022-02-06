from urllib import request
from django.contrib import admin
from Common.util import is_member,is_followUpDone, messageIcons

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
        self.request = request
        return qs

    def custom_actions(self,obj):
        
        table = '''
            <table>
                <tr>
                    <th>
                        YuvakName
                    </th>
                    <th>
                        Is FollowUp Done :
                    </th>
                    <th>
                        How
                    </th>
                    <th>
                        Submit
                    </th>
                </tr>
        '''
        if is_member(self.request.user,"Sampark Karykar"):
            yuvaks = YuvakProfile.objects.filter(karyakarprofile__user = self.request.user)

            for yuvak in yuvaks.all():

                tmp = '<tr>'
                tmp += '<td>{}</td>'.format(yuvak)
                tmp += '<td>{}</td>'.format(is_followUpDone(yuvak,self.request.user,obj))
                tmp += '<td>{}</td>'.format(yuvak)
                tmp += '<td>{}</td>'.format(yuvak)
                tmp += '</tr>'
                table += tmp
        table += '</table>'


        return format_html(table) 

    def save_model(self, request, obj, form, change):
        if "_followup_record_create" in request.POST:
            if obj.pk:
                # print(obj)
                for karyakar in obj.Mandal.karyakarprofile_set.all():
                    for yuvak in karyakar.Yuvaks.all():
                        if not FollowUp.objects.filter(Karyakram=obj,
                                    SamparkKarykar=karyakar,
                                    Yuvak=yuvak).exists():
                            f = FollowUp(Karyakram=obj,
                                        SamparkKarykar=karyakar,
                                        Yuvak=yuvak,
                                        Status=FollowupStatus.Pending)
                            f.save()
                            print(f)
  
                pass
            else:
                msg = format_html(_('Please save karykram first.'))
                self.message_user(request, msg, messages.WARNING)
                return HttpResponseRedirect("/admin/Mandal/karyakram")
        else:
            return super().save_model(request, obj, form, change)

class MandalProfileAdmin(admin.ModelAdmin):
    change_list_template = 'admin/mandal_change_list.html'

    list_display = ("__str__", "Nirikshak_details", "Sanchalak_details",)
    
    def Nirikshak_details(self,obj):
        return format_html(obj.Nirikshak.FirstName + " " +obj.Nirikshak.SurName +" : "+ messageIcons(obj.Nirikshak.WhatsappNo,20))
    
    def Sanchalak_details(self,obj):
        # msg = 
        # msg += 
        return format_html(obj.Sanchalak.FirstName + " " +obj.Sanchalak.SurName +" : " + messageIcons(obj.Nirikshak.WhatsappNo,20))
    
admin.site.register(MandalProfile,MandalProfileAdmin)
admin.site.register(Karyakram,KaryakramAdmin)