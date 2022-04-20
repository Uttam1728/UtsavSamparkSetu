from functools import reduce
from operator import or_

# import pyautogui as pg
from client_side_image_cropping import ClientsideCroppingWidget
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, ImageField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import DateInput, CheckboxSelectMultiple
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html
from more_admin_filters import MultiSelectDropdownFilter
from rangefilter.filter import DateRangeFilter

from Common.util import Profile_Completion, getMandal, is_member, create_Excel_queryset, messageIcons
from FolloWUp.models import FollowUp
from Mandal.admin import adminVrund
from Mandal.models import Karyakram
from Yuvak.models import SatsangProfile, YuvakProfile, SevaVibhag


# method for updating
@receiver(post_save, sender=YuvakProfile)
def YUvakProfileSupport(sender, instance, **kwargs):
    # create satsangi profile and link
    if not SatsangProfile.objects.filter(yuvakProfile=instance).exists():
        s = SatsangProfile(yuvakProfile=instance)
        s.save()
    # create user
    username = instance.FirstName.lower() + str(instance.pk).zfill(3)
    email = username + '@' + username + '.com'
    if instance.user is None:
        user = User.objects.create_user(username=username,
                                        email=email,
                                        password='1234', is_staff=True)

        group = Group.objects.get(name='Yuvak')
        user.groups.add(group)
        YuvakProfile.objects.filter(pk=instance.pk).update(user=user)
    # create followup if any karyakaram is active
    qs = Karyakram.objects.filter(Start_Folloup=True, IsDone=False)
    if qs.exists():
        if not FollowUp.objects.filter(Karyakram=qs.first(), Yuvak=instance).exists():
            FollowUp.objects.get_or_create(Karyakram=qs.first(),
                                           KaryKarVrund=adminVrund(instance.mandal),
                                           Yuvak=instance)


# Register your models here.


class RoleFilter(admin.SimpleListFilter):
    title = 'Role'
    parameter_name = 'role'

    def lookups(self, request, model_admin):
        return (
            ('Sampark Karykar', 'Sampark Karykar'),
            ('Yuvak', 'Yuvak'),
        )

    def queryset(self, request, queryset):
        role = self.value()
        if role is None:
            return queryset
        if role == "Sampark Karykar":
            if queryset.model is YuvakProfile:
                return queryset.filter(Q(Profile1Info__isnull=False) | Q(Profile2Info__isnull=False))
            elif queryset.model is SatsangProfile:
                return queryset.filter(
                    Q(yuvakProfile__Profile1Info__isnull=False) | Q(yuvakProfile__Profile2Info__isnull=False))
        return queryset


class ProgresBarFilter(admin.SimpleListFilter):
    title = 'Profile Completion Above'
    parameter_name = 'ratio'

    def lookups(self, request, model_admin):
        return (
            ('25', '25%'),
            ('50', '50%'),
            ('75', '75%'),
            ('80', '80%'),
            ('90', '90%')
        )

    def queryset(self, request, queryset):
        ratio = self.value()
        if ratio is None:
            return queryset
        if queryset.model is YuvakProfile:
            yuvaklist = []
            all_yuvaks = queryset.all()
            for yuvak in all_yuvaks:
                if Profile_Completion(yuvak) > int(ratio):
                    yuvaklist.append(yuvak.pk)
            return queryset.filter(id__in=yuvaklist)
        elif queryset.model is SatsangProfile:
            satsangilist = []
            all_satsangi = queryset.all()
            for satsangi in all_satsangi:
                if Profile_Completion(satsangi) > int(ratio):
                    satsangilist.append(satsangi.pk)
            return queryset.filter(id__in=satsangilist)


class KaryKarAlloatMentFilter(admin.SimpleListFilter):
    title = 'Karykar Alloted'
    parameter_name = 'alloted'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        alloted = self.value()
        if alloted is None:
            return queryset
        elif alloted == "Yes":
            return queryset.filter(karyakarprofile__isnull=False)
        elif alloted == "No":
            return queryset.filter(karyakarprofile__isnull=True)


class YuvakProfileForm(forms.ModelForm):
    class Meta:
        model = YuvakProfile
        fields = '__all__'
        widgets = {
            'DateOfBirth': DateInput(attrs={'type': 'date'}),
            'Seva_Intrests': CheckboxSelectMultiple()
        }


class YuvakProfileAdmin(admin.ModelAdmin):
    # change_list_template = 'admin/yuvak_change_list.html'
    form = YuvakProfileForm
    list_display = ("yuvakimage", "Yuvak", "Profile_Completion", "WhatsApp", "Call", "SMS", "userLink", "Role")
    list_per_page = 20
    list_filter = [RoleFilter, ("DateOfBirth", DateRangeFilter), KaryKarAlloatMentFilter, ProgresBarFilter,
                   ('Education', MultiSelectDropdownFilter), 'current_Education',
                   ('Seva_Intrests__guj_name', MultiSelectDropdownFilter)]
    search_fields = ('FirstName__icontains', 'SurName__icontains')
    list_display_links = ["Yuvak", ]
    actions = ['create_excel', 'send_Whatsapp_msg']
    # autocomplete_fields = ('Seva_Intrests',)
    formfield_overrides = {
        ImageField: {'widget': ClientsideCroppingWidget(
            width=300,
            height=300,
            preview_width=100,
            preview_height=100,
        ), },
    }

    @admin.action(description='Create Excel')
    def create_excel(modeladmin, request, queryset):
        csvfile = create_Excel_queryset(queryset)
        response = HttpResponse(csvfile.getvalue(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Yuvak_records.csv'
        return response

    @admin.action(description='Send Whatsapp Message of Sabha')
    def send_Whatsapp_msg(modeladmin, request, queryset):
        pass
        # time.sleep(5)
        # pg.write("hi")
        # time.sleep(0.5)
        # pg.press("Enter")

    def get_actions(self, request):
        actions = super(YuvakProfileAdmin, self).get_actions(request)
        if not request.user.is_superuser:
            return dict()
        return actions

    # specify which fields can be selected in the advanced filter
    # creation form

    def Yuvak(self, obj):
        s = obj.__str__()
        if obj.karyakarprofile_set.exists():
            s += ' <img src="/static/admin/img/icon-yes.svg" alt="Yes">'
        return format_html(s)

    def WhatsApp(self, obj):
        buttons = ''
        buttons += "<a href='https://wa.me/+91{}' target='_blank'><i class='fa fa-whatsapp' style='font-size:30px;color:green'></i></a>".format(
            obj.WhatsappNo)
        return format_html(buttons)

    WhatsApp.short_description = " "

    def Call(self, obj):
        buttons = ''
        buttons += "<a href='tel:+91{}' target='_blank'> <i class='fa fa-volume-control-phone' style='font-size:27px;color:deepskyblue;'></i> </a>".format(
            obj.WhatsappNo)
        return format_html(buttons)

    Call.short_description = " "

    def SMS(self, obj):
        buttons = ''
        buttons += "<a href='sms:+91{}' target='_blank'> <i class='fa fa-commenting-o' style='font-size:27px;color:lightblue;'></i> </a>".format(
            obj.WhatsappNo)
        return format_html(buttons)

    SMS.short_description = " "

    def Profile_Completion(self, obj):
        return format_html(
            '''
            <progress value="{0}" max="100"></progress>
            <span style="font-weight:bold">{0}%</span>
            ''',
            Profile_Completion(obj)
        )

    def userLink(self, obj):
        return format_html(
            '<a href="{}">{}</a>'.format(reverse('admin:auth_user_change', kwargs={'object_id': obj.user.pk}),
                                         obj.user))

    userLink.short_description = "User"

    def yuvakimage(self, obj):
        if obj.ProfilePhoto:
            s = '<img src={} height="80px" width="80px" style="border-radius: 50%;border: 1px solid black" alt="profilepic"/></div>'.format(
                obj.ProfilePhoto.url)
        else:
            s = '<img  height="80px" width="80px" src="/static/img/yuvak.png" >'
        return format_html(s)

    yuvakimage.short_description = ""

    def Role(self, obj):
        group_names = []
        for g in obj.user.groups.all():
            group_names.append(g.name)
        return ",".join(group_names)

    def get_list_filter(self, request):
        if not request.user.is_superuser:
            if is_member(request.user, "Sampark Karykar"):
                return [("DateOfBirth", DateRangeFilter), ProgresBarFilter]
            elif is_member(request.user, "Yuvak"):
                return []
        return super().get_list_filter(request)

    def get_search_fields(self, request):
        if not request.user.is_superuser:
            if not is_member(request.user, "Sampark Karykar"):
                return []
        return super().get_search_fields(request)

    def get_readonly_fields(self, request, obj):
        if not request.user.is_superuser:
            return ["user", "mandal"]
        return super().get_readonly_fields(request, obj)

    def get_queryset(self, request):
        qs = super(YuvakProfileAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(mandal=getMandal(request.user))
        elif is_member(request.user, "Sampark Karykar"):
            try:
                return qs.filter(
                    Q(karyakarprofile=request.user.yuvakprofile.Profile1Info) | Q(pk=request.user.yuvakprofile.pk))
            except ObjectDoesNotExist:
                return qs.filter(
                    Q(karyakarprofile=request.user.yuvakprofile.Profile2Info) | Q(pk=request.user.yuvakprofile.pk))
        elif is_member(request.user, "Yuvak"):
            return qs.filter(pk=request.user.yuvakprofile.pk)

    def get_search_results(self, request, queryset, search_term):
        type = request.GET.get('field_name', '')
        if type == "Yuvaks":
            queryset = queryset.filter(karyakarprofile__isnull=True).all()
        elif type in ['karykar2profile', 'karykar1profile']:
            queryset = queryset.exclude(Q(Profile1Info__isnull=False) | Q(Profile2Info__isnull=False)).all()

        orig_queryset = queryset
        queryset, use_distinct = super(YuvakProfileAdmin, self).get_search_results(
            request, queryset, search_term)
        search_words = search_term.split(',')
        if search_words:
            q_objects = [Q(**{field: word})
                         for field in self.search_fields
                         for word in search_words]

            queryset |= self.model.objects.filter(reduce(or_, q_objects))

        queryset = queryset & orig_queryset

        return queryset, use_distinct

    class Media:
        css = {'all': ("client_side_image_cropping/croppie.css", "client_side_image_cropping/cropping_widget.css",)}
        js = ("client_side_image_cropping/croppie.min.js", "client_side_image_cropping/cropping_widget.js",)


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

    def get_fieldsets(self, request, obj):
        if not request.user.is_superuser:
            return ((None, {"fields": ("username", "password", "email")}),)
        else:
            return super().get_fieldsets(request, obj)

    def get_list_display(self, request):
        if not request.user.is_superuser:
            return ['__str__', 'email', 'password']
        return super().get_list_display(request)

    def get_list_filter(self, request):
        if not request.user.is_superuser:
            return []
        return super().get_list_filter(request)

    def get_search_fields(self, request):
        if not request.user.is_superuser:
            return []
        return super().get_search_fields(request)

    def get_readonly_fields(self, request, obj):
        if not request.user.is_superuser:
            return ('username',)
        return super().get_readonly_fields(request, obj)


class SatsangProfileAdmin(admin.ModelAdmin):
    list_display = ("yuvakimage", "SatsangiWithLogo", "Profile_Completion", "WhatsApp", "Call", "SMS",)
    fieldsets = ((None, {"fields": (("NityaPuja", "NityaPujaYear"),
                                    ("TilakChandlo", "TilakChandloYear"),
                                    ("Satsangi", "SatsangiYear"),
                                    ("AthvadikSabha", "AthvadikSabhaYear"),
                                    ("Ravisabha", "RavisabhaYear"),
                                    ("GharSatsang", "GharSatsangYear"),
                                    ("SSP", "SSPStage"),
                                    ("Ekadashi", "EkadashiYear"),
                                    ("Niymit_Vanchan", "Niymit_VanchanYear"),
                                    )}),)
    list_per_page = 20
    search_fields = ('yuvakProfile__FirstName__icontains', 'yuvakProfile__SurName__icontains')
    list_filter = [RoleFilter, ProgresBarFilter, 'GharSatsang']
    list_display_links = ["SatsangiWithLogo", ]
    actions = ['create_excel', ]

    # advanced_filter_fields = tuple(f.name for f in SatsangProfile._meta.fields)
    # advanced_filter_fields = ('NityaPuja')
    @admin.action(description='Create Excel')
    def create_excel(modeladmin, request, queryset):
        csvfile = create_Excel_queryset(queryset)
        response = HttpResponse(csvfile.getvalue(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Yuvak_records.csv'
        return response

    def get_actions(self, request):
        actions = super(SatsangProfileAdmin, self).get_actions(request)
        if not request.user.is_superuser:
            return dict()
        return actions

    def SatsangiWithLogo(self, obj):
        s = obj.yuvakProfile.__str__()
        if obj.yuvakProfile.karyakarprofile_set.exists():
            s += ' <img src="/static/admin/img/icon-yes.svg" alt="Yes">'
        return format_html(s)

    SatsangiWithLogo.short_description = "Satsangi"

    def WhatsApp(self, obj):
        buttons = ''
        buttons += "<a href='https://wa.me/+91{}' target='_blank' ><i class='fa fa-whatsapp' style='font-size:30px;color:green'></i></a>".format(
            obj.yuvakProfile.WhatsappNo)
        return format_html(buttons)

    WhatsApp.short_description = " "

    def Call(self, obj):
        buttons = ''
        buttons += "<a href='tel:+91{}' target='_blank'> <i class='fa fa-volume-control-phone' style='font-size:27px;color:deepskyblue;'></i> </a>".format(
            obj.yuvakProfile.WhatsappNo)
        return format_html(buttons)

    Call.short_description = " "

    def SMS(self, obj):
        buttons = ''
        buttons += "<a href='sms:+91{}' target='_blank'> <i class='fa fa-commenting-o' style='font-size:27px;color:lightblue;'></i> </a>".format(
            obj.yuvakProfile.WhatsappNo)
        return format_html(buttons)

    SMS.short_description = " "

    def Profile_Completion(self, obj):
        return format_html(
            '''
            <progress value="{0}" max="100"></progress>
            <span style="font-weight:bold">{0}%</span>
            ''',
            Profile_Completion(obj)
        )

    def yuvakimage(self, obj):
        if obj.yuvakProfile.ProfilePhoto:
            s = '<img src={} height="80px" width="80px" style="border-radius: 50%;border: 1px solid black" alt="profilepic"/></div>'.format(
                obj.yuvakProfile.ProfilePhoto.url)
        else:
            s = '<img  height="80px" width="80px" src="/static/img/yuvak.png" >'
        return format_html(s)

    yuvakimage.short_description = ""

    def get_search_fields(self, request):
        if not request.user.is_superuser:
            if not is_member(request.user, "Sampark Karykar"):
                return []
        return super().get_search_fields(request)

    def get_list_filter(self, request):
        if not request.user.is_superuser:
            if is_member(request.user, "Sampark Karykar"):
                return [ProgresBarFilter, 'GharSatsang']
            elif is_member(request.user, "Yuvak"):
                return []
        return super().get_list_filter(request)

    def get_queryset(self, request):
        qs = super(SatsangProfileAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(yuvakProfile__mandal=getMandal(request.user))
        # else:
        #     return qs.filter(yuvakProfile=request.user.yuvakprofile) 
        elif is_member(request.user, "Sampark Karykar"):
            try:
                yuvaklist = YuvakProfile.objects.filter(
                    Q(karyakarprofile=request.user.yuvakprofile.Profile1Info) | Q(pk=request.user.yuvakprofile.pk))
            except ObjectDoesNotExist:
                yuvaklist = YuvakProfile.objects.filter(
                    Q(karyakarprofile=request.user.yuvakprofile.Profile2Info) | Q(pk=request.user.yuvakprofile.pk))
            return qs.filter(Q(yuvakProfile__in=yuvaklist))
        elif is_member(request.user, "Yuvak"):
            return qs.filter(yuvakProfile=request.user.yuvakprofile)

    def get_readonly_fields(self, request, obj):
        if not request.user.is_superuser:
            return ('yuvakProfile',)
        return super().get_readonly_fields(request, obj)

    def get_search_results(self, request, queryset, search_term):

        orig_queryset = queryset
        queryset, use_distinct = super(SatsangProfileAdmin, self).get_search_results(
            request, queryset, search_term)
        search_words = search_term.split(',')
        if search_words:
            q_objects = [Q(**{field: word})
                         for field in self.search_fields
                         for word in search_words]

            queryset |= self.model.objects.filter(reduce(or_, q_objects))

        queryset = queryset & orig_queryset

        return queryset, use_distinct


class SevaVibhagAdmin(admin.ModelAdmin):
    list_display = ('guj_name', 'leader_details', 'Yuvak_List')
    search_fields = ('name__icontains',)

    autocomplete_fields = ('yuvaks', 'leader')

    def leader_photo(selfself, obj):
        if obj.leader and obj.leader.ProfilePhoto:
            s = '<img src={} height="60px" width="60px" style="border-radius: 50%;border: 1px solid black" alt="profilepic"/></div>'.format(
                obj.leader.ProfilePhoto.url)
        else:
            s = '<img  height="60px" width="60px" src="/static/img/yuvak.png" >'
        return format_html(s)

    def leader_details(self, obj):
        s = ''
        if obj.leader and obj.leader.ProfilePhoto:
            s += '<img src={} height="60px" width="60px" style="border-radius: 50%;border: 1px solid black;margin:7px"" alt="profilepic"/></div>'.format(
                obj.leader.ProfilePhoto.url)
        else:
            s += '<img  height="60px" width="60px" src="/static/img/yuvak.png" >'
        if obj.leader:
            s += obj.leader.FirstName + " " + obj.leader.SurName + messageIcons(
                obj.leader.WhatsappNo, 20)
        return format_html(s)

    leader_details.short_description = "_______________Leader Details_______________"

    def Yuvak_List(self, obj):
        s = ''

        for yuvak in obj.yuvaks.all():
            if yuvak.ProfilePhoto:
                s += '<img src={} height="60px" width="60px" style="border-radius: 50%;border: 1px solid black;margin:7px" alt="profilepic"/></div>'.format(
                    yuvak.ProfilePhoto.url)
            else:
                s += '<img  height="60px" width="60px" src="/static/img/yuvak.png" >'
            s += format_html(yuvak.FirstName + " " + yuvak.SurName + messageIcons(
                yuvak.WhatsappNo, 20))
            s += "<br>"
        return format_html(s)

    Yuvak_List.short_description = "__________________________Yuvak List__________________________."


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(YuvakProfile, YuvakProfileAdmin)
admin.site.register(SatsangProfile, SatsangProfileAdmin)
admin.site.register(SevaVibhag, SevaVibhagAdmin)
