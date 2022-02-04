from django.contrib import admin

from Mandal.models import Karyakram, MandalProfile

# Register your models here.

class KaryakramAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_active", "For_All","Start_date","End_date")



admin.site.register(MandalProfile)
admin.site.register(Karyakram,KaryakramAdmin)