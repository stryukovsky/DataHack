from django.contrib import admin

from main.models import University


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'inn', 'post_address', 'sum')


admin.site.register(University, UniversityAdmin)
