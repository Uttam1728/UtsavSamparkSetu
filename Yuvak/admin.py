from django.urls import reverse
from django.contrib import admin

from rangefilter.filter import DateRangeFilter,DateTimeRangeFilter
from Common.util import  Profile_Completion, getMandal, is_member, messageIcons
from django.db.models import Q
from django.utils.html import format_html
from Yuvak.models import SatsangProfile, YuvakProfile
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext as _
# method for updating
@receiver(post_save, sender=YuvakProfile)
def Create_SatsangiProfile(sender, instance, **kwargs):
    if not SatsangProfile.objects.filter(yuvakProfile=instance).exists():
        s = SatsangProfile(yuvakProfile=instance)
        s.save()
    username = instance.FirstName.lower() + str(instance.pk).zfill(3)
    email = username + '@' + username + '.com'
    if instance.user is None:
        user = User.objects.create_user(username=username,
                                    email=email,
                                    password='1234', is_staff=True)
        
        group = Group.objects.get(name='Yuvak')
        user.groups.add(group)   
        YuvakProfile.objects.filter(pk=instance.pk).update(user=user)

# Register your models here.


class RoleFilter(admin.SimpleListFilter):
    title = 'Role'
    parameter_name = 'role'

    def lookups(self, request, model_admin):
        return (
            ('Sampark Karykar', 'Sampark Karykar'),
            ('Yuvak',  'Yuvak'),
        )

    def queryset(self, request, queryset):
        groupName = self.value()
        if groupName is None:
            return queryset
        return queryset.filter(user__groups__name = groupName)

class YuvakProfileAdmin(admin.ModelAdmin):
    
    # change_list_template = 'admin/yuvak_change_list.html'
    list_display = ("__str__", "Profile_Completion", "WhatsApp","Call","SMS","userLink")
    list_per_page = 20
    list_filter = [RoleFilter,("DateOfBirth",DateRangeFilter)]
    search_fields = ('FirstName__icontains','SurName__icontains')

    def WhatsApp(self,obj):
        buttons = ''
        buttons += "<a href='https://wa.me/+91{}' ><i class='fa fa-whatsapp' style='font-size:30px;color:green'></i></a>".format(obj.WhatsappNo)
        return format_html(buttons)

    def Call(self,obj):
        buttons = ''
        buttons += "<a href='tel:+91{}'> <i class='fa fa-volume-control-phone' style='font-size:27px;color:deepskyblue;'></i> </a>".format(obj.WhatsappNo)
        return format_html(buttons)
    
    def SMS(self,obj):
        buttons = ''
        buttons += "<a href='sms:+91{}'> <i class='fa fa-commenting-o' style='font-size:27px;color:lightblue;'></i> </a>".format(obj.WhatsappNo)  
        return format_html(buttons)
    
    def Profile_Completion(self,obj):
        return format_html(
            '''
            <progress value="{0}" max="100"></progress>
            <span style="font-weight:bold">{0}%</span>
            ''',
            Profile_Completion(obj)
        )

    def MessageIcons(self,obj):
        return format_html(messageIcons(obj.WhatsappNo,27))
    
    def userLink(self,obj):
        return format_html('<a href="{}">{}</a>'.format(reverse('admin:auth_user_change',kwargs={'object_id':obj.user.pk}),obj.user))
    userLink.short_description = "User"
    MessageIcons.short_description = 'Connect'

    def get_list_filter(self,request):
        if not request.user.is_superuser:
            return []
        return super().get_list_filter(request)
    
    def get_search_fields(self,request):
        if is_member(request.user,"Yuvak"):
            return []
        return super().get_search_fields(request)


    def get_queryset(self, request):
        qs = super(YuvakProfileAdmin, self).get_queryset(request) 
        if request.user.is_superuser:
            return qs.filter(mandal=getMandal(request.user))
        elif is_member(request.user,"Sampark Karykar"):
            try:
                return qs.filter(Q(karyakarprofile=request.user.yuvakprofile.Profile1Info) | Q(pk=request.user.yuvakprofile.pk))
            except ObjectDoesNotExist  :
                return qs.filter(Q(karyakarprofile=request.user.yuvakprofile.Profile2Info) | Q(pk=request.user.yuvakprofile.pk))
        elif is_member(request.user,"Yuvak"):
            return qs.filter(pk=request.user.yuvakprofile.pk)
   
    def get_search_results(self, request, queryset, search_term):
        type = request.GET.get('field_name','')
        if type == "Yuvaks":
            queryset =queryset.filter(karyakarprofile__isnull=True).all()
        elif type in ['karykar2profile', 'karykar1profile']:
            queryset = queryset.exclude(Q(Profile1Info__isnull=False) | Q(Profile2Info__isnull=False)).all()
        return super().get_search_results(request, queryset, search_term)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if not request.user.is_superuser:
            self.readonly_fields = ["user","mandal"]
        else:
            self.readonly_fields = []
        return super().change_view(request, object_id, form_url, extra_context)

    def Role(self,obj):
        group_names = []
        for g in obj.user.groups.all():
            group_names.append(g.name)
        return ",".join(group_names)

class UserAdmin(AuthUserAdmin):
    list_per_page = 20
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request) 
        if request.user.is_superuser:
            return qs.filter(yuvakprofile__mandal=getMandal(request.user))
        else:
            self.list_filter = []
            return qs.filter(pk=request.user.id) 
    
    def get_fieldsets(self, request, obj) :
        if not request.user.is_superuser:
            return ((None, {"fields": ("username","password","email")}),)
        else:
            return super().get_fieldsets(request, obj)
    
    def get_list_display(self,request):
        if not request.user.is_superuser:
            return ['__str__','email','password']
        return super().get_list_display(request)

    def get_list_filter(self,request):
        if not request.user.is_superuser:
            return []
        return super().get_list_filter(request)
    
    def get_search_fields(self,request):
        if not request.user.is_superuser:
            return []
        return super().get_search_fields(request)

    def get_readonly_fields(self, request, obj) :
        if not request.user.is_superuser:
            return ('username',)
        return super().get_readonly_fields(request, obj)


class SatsangProfileAdmin(admin.ModelAdmin):
    list_display = ("__str__", "Profile_Completion",)
    fieldsets = ((None, {"fields": (("NityaPuja","NityaPujaYear"),
    ("TilakChandlo","TilakChandloYear"),
    ("Satsangi","SatsangiYear"),
    ("AthvadikSabha","AthvadikSabhaYear"),
    ("Ravisabha","RavisabhaYear"),
    ("GharSatsang","GharSatsangYear"),
    ("SSP","SSPStage"),
    ("Ekadashi","EkadashiYear"),
    ("Niymit_Vanchan","Niymit_VanchanYear"),
    )}),)
    list_per_page = 20
    def Profile_Completion(self,obj):
        return format_html(
            '''
            <progress value="{0}" max="100"></progress>
            <span style="font-weight:bold">{0}%</span>
            ''',
            Profile_Completion(obj)
        )

    def get_queryset(self, request):
        qs = super(SatsangProfileAdmin, self).get_queryset(request) 
        if request.user.is_superuser:
            return qs.filter(yuvakProfile__mandal=getMandal(request.user))
        # else:
        #     return qs.filter(yuvakProfile=request.user.yuvakprofile) 
        elif is_member(request.user,"Sampark Karykar"):
            try:
                yuvaklist =  YuvakProfile.objects.filter(Q(karyakarprofile=request.user.yuvakprofile.Profile2Info) | Q(pk=request.user.yuvakprofile.pk))
            except ObjectDoesNotExist  :
                yuvaklist = YuvakProfile.objects.filter(Q(karyakarprofile=request.user.yuvakprofile.Profile2Info) | Q(pk=request.user.yuvakprofile.pk))
            return qs.filter(Q(yuvakProfile__in = yuvaklist))
        elif is_member(request.user,"Yuvak"):
            return qs.filter(pk=request.user.yuvakprofile.pk)
    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        if not request.user.is_superuser:
            self.readonly_fields = ["yuvakProfile"]
        else:
            self.readonly_fields = []
        return super().change_view(request, object_id, form_url, extra_context)

# # Create your models here.
# class User(AbstractUser):
    
#     def set_password(self, raw_password):
#         if self.force_pswd_first_login is None:
#             self.default_pwd_updated = False
#         elif not self.force_pswd_first_login:
#             self.default_pwd_updated = True
#         super().set_password(raw_password)


admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(YuvakProfile, YuvakProfileAdmin)
admin.site.register(SatsangProfile,SatsangProfileAdmin)
