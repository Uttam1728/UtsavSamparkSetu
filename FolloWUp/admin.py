import html
from django.contrib import admin

import SamparkKarykar.models
from Common.util import getMandal, is_member, messageIcons
from FolloWUp.models import FollowUp,FollowupStatus, ComingStatus
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from django.utils.html import format_html
from Common.filters import KarykarDropdownFilter,HowDropdownFilter, StatusDropdownFilter, KarykramDropdownFilter
from django import forms
# Register your models here.

color= {FollowupStatus.Pending: ("lightgoldenrodyellow","Pending"),
FollowupStatus.Done:("darkseagreen","Done"),
FollowupStatus.No:("indianred","No")}

class FeedbackFilter(admin.SimpleListFilter):
    title = 'Feedback'
    parameter_name = 'feedback'

    def lookups(self, request, model_admin):
        return tuple((statis.value, statis.name) for statis in ComingStatus)

    def queryset(self, request, queryset):
        feedback = self.value()
        if feedback is None:
            return queryset
        return queryset.filter(Coming = feedback)

class AdminFollowUpFilter(admin.SimpleListFilter):
    title = 'Admin'
    parameter_name = 'admin'

    def lookups(self, request, model_admin):
        return (("withadmin","Admin"),("withoutadmin","Without Admin"))

    def queryset(self, request, queryset):
        param = self.value()
        if param is None:
            return queryset
        Mandal = getMandal(request.user)
        karyakar_vrund = SamparkKarykar.models.KaryakarProfile.objects.filter(mandal=Mandal, karykar1profile__FirstName="Admin",
                                                                       karykar1profile__MiddleName=Mandal.Name,
                                                                       karykar1profile__SurName="Mandal").first()

        if param == "withadmin":
            return queryset.filter(KaryKarVrund=karyakar_vrund)
        elif param == "withoutadmin":
            return queryset.exclude(KaryKarVrund=karyakar_vrund)
        return None

class FollowUpAdminForm(forms.ModelForm):
    class Meta:
        model = FollowUp
        fields = '__all__'
    def clean(self):
        # Validation goes here :)
        # print(sel/f)
        cleaned_data  =self.cleaned_data
        if cleaned_data['Coming'] is None: 
            raise forms.ValidationError("Coming Status Required! Please Add it") 
        if cleaned_data['Status'] != FollowupStatus.Done:
            raise forms.ValidationError("Status is not selected as Done, please select!")
        if cleaned_data['Coming'] != ComingStatus.Yes :
            if  cleaned_data["Remark"] is None or cleaned_data["Remark"] == "":
                raise forms.ValidationError("Remark Required! Please Add it")   

class FollowUpAdmin(admin.ModelAdmin):
    # change_list_template = 'admin/followup_change_list.html'

    list_display = ("__str__","YuvakName", "StatusWithColor","ComingLogo","How","Karykar_Names")
    list_filter = [KarykramDropdownFilter,StatusDropdownFilter, HowDropdownFilter,KarykarDropdownFilter,AdminFollowUpFilter]
    fieldsets = ((None, {"fields": ("Karyakram","KaryKarVrund","Yuvak","Status","Coming","How","Remark")}),)
    list_per_page = 25
    form = FollowUpAdminForm
    search_fields = ('KaryKarVrund__karykar1profile__FirstName__icontains',
                        'KaryKarVrund__karykar1profile__SurName__icontains',
                        'KaryKarVrund__karykar2profile__FirstName__icontains',
                        'KaryKarVrund__karykar2profile__SurName__icontains',
                        'KaryKarVrund__Yuvaks__FirstName__icontains',
                        'KaryKarVrund__Yuvaks__SurName__icontains') 
    
    def YuvakName(self,obj):
        return format_html(obj.Yuvak.FirstName + " " +obj.Yuvak.SurName +" <br> "+ messageIcons(obj.Yuvak.WhatsappNo,20,False))
    YuvakName.short_description = "______Yuvak Name_______."
    
    def Karykar_Names(self,obj):
        s= ''
        if obj.KaryKarVrund.karykar1profile:
            s += '<li>{} {}</li>'.format(obj.KaryKarVrund.karykar1profile.FirstName,obj.KaryKarVrund.karykar1profile.SurName)
        if obj.KaryKarVrund.karykar2profile:
            s += '<li>{} {}</li>'.format(obj.KaryKarVrund.karykar2profile.FirstName,obj.KaryKarVrund.karykar2profile.SurName)
        return format_html(s)
    Karykar_Names.short_description = "______Karykar Names_______."

    def StatusWithColor(self,obj):
        return format_html("<button style='color: black;border-radius: 5px;padding-top: 3px;border: none;background: {};'><b>{}</b></button>".format(color[obj.Status][0],color[obj.Status][1]))
    StatusWithColor.short_description = "Status"
    
    def ComingLogo(self,obj):
        if obj.Status == FollowupStatus.Done:
            if obj.Coming == ComingStatus.Yes:
                return format_html('<img src="/static/admin/img/icon-yes.svg" alt="Yes">')
            elif obj.Coming == ComingStatus.No:
                return format_html('<img src="/static/admin/img/icon-no.svg" alt="No">'+"-"+obj.Remark)
            elif obj.Coming == ComingStatus.Not_Sure:
                return format_html('<img src="/static/admin/img/icon-unknown.svg" alt="Not Sure">'+"-"+ obj.Remark)
            
        return ""
    ComingLogo.short_description = "Coming?"
    
    '''
    # actions = ['change_status']
    
    # commenting as per not need, in future may be
    # class UpdateStatusActionForm(ActionForm):
    #     new_status = forms.ChoiceField(choices=[(tag.value, tag.name) for tag in FollowupStatus], required=True,widget=forms.Select())
    #     How  = forms.ChoiceField(choices=[(tag.value, tag.name) for tag in HowMethods], required=True,widget=forms.Select())
    
    # action_form = UpdateStatusActionForm


    # def change_status(self, request, queryset):
        
    #     new_status = request.POST.get('new_status')
    #     how = request.POST.get('How')
    #     queryset.update(Status=int(new_status),How=int(how))

    # change_status.allowed_permissions = ('change',)
    # change_status.short_description = "Mark selected Yuvak as..."
    '''
    
    def get_queryset(self, request):
        qs = super(FollowUpAdmin, self).get_queryset(request) 
        user = request.user
        if user.is_superuser:
            return qs.filter(Karyakram__Mandal=getMandal(user))
        elif is_member(user,"Sampark Karykar"):
            try:
                return qs.filter(Q(KaryKarVrund=request.user.yuvakprofile.Profile1Info) | Q(Yuvak__user=user)) 
            except ObjectDoesNotExist  :
                return qs.filter(Q(KaryKarVrund=request.user.yuvakprofile.Profile2Info) | Q(Yuvak__user=user))
        elif is_member(user,"Yuvak"):
            return qs.filter(Yuvak__user=user)
    
    def get_readonly_fields(self, request, obj) :
        if not request.user.is_superuser:
            return  ["KaryKarVrund","Yuvak","Karyakram"]
        return super().get_readonly_fields(request, obj)
    
    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser:
            if obj and obj.Karyakram.IsDone:
                return False
        return super().has_change_permission(request,obj)

    def get_list_filter(self,request):
        if not request.user.is_superuser:
            return [KarykramDropdownFilter,StatusDropdownFilter, HowDropdownFilter,]
        return super().get_list_filter(request)

    def get_search_fields(self,request):
        if not request.user.is_superuser:
            if not is_member(request.user,"Sampark Karykar"):
                return []
        return super().get_search_fields(request)  



class Attandance(FollowUp):
    
    class Meta:
        proxy=True
        verbose_name = "Attandance"
        verbose_name_plural = "Attandance"

class AttandanceAdmin(FollowUpAdmin):
    list_display = ("Karyakram","QR","YuvakName","Present", "StatusWithColor","Feedback","How","Karykar_Names")
    fieldsets = ((None, {"fields": ("Karyakram","KaryKarVrund","Yuvak","Status","Coming","How","Remark","Present")}),)
    list_filter = [KarykramDropdownFilter,StatusDropdownFilter, HowDropdownFilter,KarykarDropdownFilter,"Present",FeedbackFilter]
    actions = []
    list_display_links = None 
    search_fields = (
                    'KaryKarVrund__karykar1profile__FirstName__icontains',
                        'KaryKarVrund__karykar1profile__SurName__icontains',
                        'KaryKarVrund__karykar2profile__FirstName__icontains',
                        'KaryKarVrund__karykar2profile__SurName__icontains',
                        'Yuvak__FirstName__icontains',
                        'Yuvak__SurName__icontains')  
    change_list_template = "admin/attandance_change_list.html"
    def Karyakram_name(self,obj):
        return obj.Karyakram.__str__()

    def StatusWithColor(self,obj):
        return format_html("<button style='color: black;border-radius: 5px;padding-top: 3px;border: none;background: {};'><b>{}</b></button>".format(color[obj.Status][0],color[obj.Status][1]))
    StatusWithColor.short_description = "FolloUp"
    
    def Feedback(self,obj):
        if obj.Status == FollowupStatus.Done:
            if obj.Coming == ComingStatus.Yes:
                return format_html('<img src="/static/admin/img/icon-yes.svg" alt="Yes">')
            elif obj.Coming == ComingStatus.No:
                return format_html('<img src="/static/admin/img/icon-no.svg" alt="No">'+" - "+obj.Remark)
            elif obj.Coming == ComingStatus.Not_Sure:
                return format_html('<img src="/static/admin/img/icon-unknown.svg" alt="Not Sure">'+" - "+ obj.Remark)
            
        return ""

    def PresentButton(self,obj):
        url = '/mark_present?followup={}&yuvak={}&present={}&parent={}'.format(obj.pk,obj.Yuvak_id,not obj.Present,html.unescape(self.request.build_absolute_uri()))
        button = format_html(
            '<a type="button" class="button button_preview" id="_sub_preview" href="{url}" >&nbsp;{P_A}&nbsp;</a>',
            url=url,P_A = 'A' if obj.Present else 'P'
        )
        return button
    PresentButton.short_description= ""


    def QR(self,obj):
        if not self.request.user.is_superuser:
            if not obj.Karyakram.IsDone:
                if is_member(self.request.user,"Yuvak") and self.request.user.yuvakprofile == obj.Yuvak:
                    if not obj.Present:
                        url = "https://" +self.request.get_host() + '/mark_present?followup={}&yuvak={}&present={}&parent={}'.format(obj.pk,obj.Yuvak_id,not obj.Present,html.unescape(self.request.build_absolute_uri()))
                        return format_html('<div id="qrcode" value={} ></div>'.format(url))
        return ""
    QR.short_description= ""

    def get_list_display(self,request):
        if request.user.is_superuser:
            return ('PresentButton',) + super().get_list_display(request)
        return super().get_list_display(request)

    def get_queryset(self, request):
        self.request = request
        qs = super(AttandanceAdmin, self).get_queryset(request).order_by('-Karyakram__Karyakram_date')
        return qs.filter(Karyakram__Start_Attandance=True)
        
    def get_search_fields(self,request):
        if not request.user.is_superuser:
            if not is_member(request.user,"Sampark Karykar"):
                return []
        return super().get_search_fields(request)

    def get_list_filter(self,request):
        if not request.user.is_superuser:
            if not is_member(request.user,"Sampark Karykar"):
                return []
        return super().get_list_filter(request)


admin.site.register(FollowUp,FollowUpAdmin)
admin.site.register(Attandance,AttandanceAdmin)