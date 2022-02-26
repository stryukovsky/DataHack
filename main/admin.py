from django.contrib import admin

from main.models import University, Purchase


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'inn', 'post_address', 'students_count', 'rating_position')
    search_fields = ('name', 'inn')


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('university', 'amount', 'date', 'purchase_type')


admin.site.register(University, UniversityAdmin)
admin.site.register(Purchase, PurchaseAdmin)
