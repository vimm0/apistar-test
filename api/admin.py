from django.contrib import admin

from .models import AccessToken, Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(AccessToken)
admin.site.register(Customer, CustomerAdmin)
