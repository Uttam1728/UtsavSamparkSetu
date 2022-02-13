from django.contrib import admin
from Common.util import getMandal, is_member, messageIcons
from FolloWUp.models import FollowUp,FollowupStatus, PreentStatus
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from django.utils.html import format_html
from Common.filters import KarykarDropdownFilter,HowDropdownFilter, StatusDropdownFilter, KarykramDropdownFilter
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.contrib import messages
from django import forms
# Register your models here.

color= {FollowupStatus.Pending: ("lightgoldenrodyellow","Pending"),
FollowupStatus.Done:("darkseagreen","Done"),
FollowupStatus.No:("indianred","No")}

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
        if cleaned_data['Coming'] != PreentStatus.Yes :
            if  cleaned_data["Remark"] is None or cleaned_data["Remark"] == "":
                raise forms.ValidationError("Remark Required! Please Add it")   

class FollowUpAdmin(admin.ModelAdmin):
    # change_list_template = 'admin/followup_change_list.html'

    list_display = ("__str__","YuvakName", "StatusWithColor","ComingLogo","How","Karykar_Names")
    list_filter = [KarykramDropdownFilter,StatusDropdownFilter, HowDropdownFilter,KarykarDropdownFilter]
    fieldsets = ((None, {"fields": ("Karyakram","KaryKarVrund","Yuvak","Status","Coming","How","Remark")}),)
    list_per_page = 25
    form = FollowUpAdminForm
    
    
    def YuvakName(self,obj):
        return format_html(obj.Yuvak.FirstName + " " +obj.Yuvak.SurName +" <br> "+ messageIcons(obj.Yuvak.WhatsappNo,20,False))
        
    def Karykar_Names(self,obj):
        s= ''
        if obj.KaryKarVrund.karykar1profile:
            s += '<li>{} {}</li>'.format(obj.KaryKarVrund.karykar1profile.FirstName,obj.KaryKarVrund.karykar1profile.SurName)
        if obj.KaryKarVrund.karykar2profile:
            s += '<li>{} {}</li>'.format(obj.KaryKarVrund.karykar2profile.FirstName,obj.KaryKarVrund.karykar2profile.SurName)
        return format_html(s)
    
    def StatusWithColor(self,obj):
        return format_html("<button style='color: black;border-radius: 5px;padding-top: 3px;border: none;background: {};'><b>{}</b></button>".format(color[obj.Status][0],color[obj.Status][1]))
    StatusWithColor.short_description = "Status"
    
    def ComingLogo(self,obj):
        if obj.Status == FollowupStatus.Done:
            if obj.Coming == PreentStatus.Yes:
                return format_html('<img src="/static/admin/img/icon-yes.svg" alt="Yes">')
            elif obj.Coming == PreentStatus.No:
                return format_html('<img src="/static/admin/img/icon-no.svg" alt="No">'+"-"+obj.Remark)
            elif obj.Coming == PreentStatus.Not_Sure:
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
                return qs.filter(Q(KaryKarVrund=request.user.yuvakprofile.Profile1Info))
            except ObjectDoesNotExist  :
                return qs.filter(Q(KaryKarVrund=request.user.yuvakprofile.Profile2Info))
        elif is_member(user,"Yuvak"):
            return qs.filter(Yuvak__user=user)
    
    def get_readonly_fields(self, request, obj) :
        if not request.user.is_superuser:
            return  ["KaryKarVrund","Yuvak","Karyakram"]
        return super().get_readonly_fields(request, obj)
    
    def get_list_filter(self,request):
        if not request.user.is_superuser:
            return [KarykramDropdownFilter,StatusDropdownFilter, HowDropdownFilter,]
        return super().get_list_filter(request)
        
    def changelist_view(self, request, extra_context=None):
        user = request.user
        if user.is_superuser:
            # self.list_filter.insert(1,KarykarDropdownFilter)
            pass
        elif is_member(request.user,"Sampark Karykar"):
             if KarykarDropdownFilter in self.list_filter : 
                self.list_filter.remove(KarykarDropdownFilter)
        return super(FollowUpAdmin, self).changelist_view(request, extra_context=None)

   

admin.site.register(FollowUp,FollowUpAdmin)