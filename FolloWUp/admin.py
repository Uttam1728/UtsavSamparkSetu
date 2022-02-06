from django.contrib import admin
from Common.util import is_member

from django.contrib.admin.helpers import ActionForm
from FolloWUp.models import FollowUp,FollowupStatus, HowMethods

from django import forms
from django.utils.html import format_html
# Register your models here.

color= {FollowupStatus.Pending: ("lightgoldenrodyellow","Pending"),
FollowupStatus.Done:("darkseagreen","Done"),
FollowupStatus.No:("indianred","No")}

class FollowUpAdmin(admin.ModelAdmin):
    list_display = ("__str__", "StatusWithColor", "YuvakName", "How",)
    list_filter = ("Status","How")
    fieldsets = ((None, {"fields": ("Karyakram","Yuvak","SamparkKarykar","Status","How","Remark")}),)
    actions = ['change_status']
    

    class UpdateStatusActionForm(ActionForm):
        new_status = forms.ChoiceField(choices=[(tag.value, tag.name) for tag in FollowupStatus], required=True,widget=forms.Select())
        How  = forms.ChoiceField(choices=[(tag.value, tag.name) for tag in HowMethods], required=True,widget=forms.Select())
    
    action_form = UpdateStatusActionForm


    def change_status(self, request, queryset):
        """
        change the status of the submissions to the desired one
        :param request:
        :param queryset: the list of items selected by the user
        :return:
        """
        if request.user.is_superuser:
            new_status = request.POST.get('new_status')
            how = request.POST.get('How')
            queryset.update(Status=int(new_status),How=int(how))

    change_status.allowed_permissions = ('change',)
    change_status.short_description = "Mark selected Yuvak as..."
    def YuvakName(self,obj):
        return obj.Yuvak.FirstName + " " + obj.Yuvak.SurName
    
    def StatusWithColor(self,obj):
        
        return format_html("<button style='color: black;border-radius: 5px;border: none;background: {};'>{}</button>".format(color[obj.Status][0],color[obj.Status][1]))
    
    def get_queryset(self, request):
        qs = super(FollowUpAdmin, self).get_queryset(request) 
        if request.user.is_superuser:
            # self.list_display+= ("Groups",)
            return qs
        # elif is_member(request.user,"Yuvak"):
        #     return qs.filter(user=request.user)
        elif is_member(request.user,"Sampark Karykar"):
            return qs.filter(SamparkKarykar__profile__user = request.user)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if is_member(request.user,"Sampark Karykar"):
            self.readonly_fields = ["SamparkKarykar","Yuvak","Karyakram"]
        return super().change_view(request, object_id, form_url, extra_context)
    

admin.site.register(FollowUp,FollowUpAdmin)