from django.contrib import admin
from Common.util import getMandal, is_member
from django.contrib.admin.helpers import ActionForm
from FolloWUp.models import FollowUp,FollowupStatus, HowMethods

from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django import forms
from django.utils.html import format_html
from Common.filters import KarykarDropdownFilter,HowDropdownFilter, StatusDropdownFilter, KarykramDropdownFilter
# Register your models here.

color= {FollowupStatus.Pending: ("lightgoldenrodyellow","Pending"),
FollowupStatus.Done:("darkseagreen","Done"),
FollowupStatus.No:("indianred","No")}


class FollowUpAdmin(admin.ModelAdmin):
    list_display = ("__str__", "StatusWithColor", "KarykarName","YuvakName", "How",)
    list_filter = [KarykramDropdownFilter,StatusDropdownFilter, HowDropdownFilter,]
    fieldsets = ((None, {"fields": ("Karyakram","Yuvak","SamparkKarykar","Status","How","Remark")}),)
    actions = ['change_status']
    

    class UpdateStatusActionForm(ActionForm):
        new_status = forms.ChoiceField(choices=[(tag.value, tag.name) for tag in FollowupStatus], required=True,widget=forms.Select())
        How  = forms.ChoiceField(choices=[(tag.value, tag.name) for tag in HowMethods], required=True,widget=forms.Select())
    
    action_form = UpdateStatusActionForm


    def change_status(self, request, queryset):
        
        new_status = request.POST.get('new_status')
        how = request.POST.get('How')
        queryset.update(Status=int(new_status),How=int(how))

    change_status.allowed_permissions = ('change',)
    change_status.short_description = "Mark selected Yuvak as..."

    def YuvakName(self,obj):
        return obj.Yuvak.FirstName + " " + obj.Yuvak.SurName
    
    def KarykarName(self,obj):
        return obj.SamparkKarykar.profile.FirstName + " " + obj.SamparkKarykar.profile.SurName
    
    def StatusWithColor(self,obj):
        
        return format_html("<button style='color: black;border-radius: 5px;padding-top: 3px;border: none;background: {};'><b>{}</b></button>".format(color[obj.Status][0],color[obj.Status][1]))
    
    def get_queryset(self, request):
        qs = super(FollowUpAdmin, self).get_queryset(request) 
        if request.user.is_superuser:
            return qs.filter(SamparkKarykar__profile__mandal=getMandal(request.user))

        elif is_member(request.user,"Sampark Karykar"):
            return qs.filter(SamparkKarykar__profile__user = request.user)
        elif is_member(request.user,"Yuvak"):
            return qs.filter(Yuvak__user=request.user)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if is_member(request.user,"Sampark Karykar"):
            self.readonly_fields = ["SamparkKarykar","Yuvak","Karyakram"]
        else:
            self.readonly_fields = []
        return super().change_view(request, object_id, form_url, extra_context)
    
    def changelist_view(self, request, extra_context=None):
        user = request.user
        if user.is_superuser:
            self.list_filter.insert(1,KarykarDropdownFilter)
        elif is_member(request.user,"Sampark Karykar"):
             self.list_filter.remove(KarykarDropdownFilter)
        return super(FollowUpAdmin, self).changelist_view(request, extra_context=None)

admin.site.register(FollowUp,FollowUpAdmin)