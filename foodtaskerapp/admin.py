from django.contrib import admin

# Register your models here.
from foodtaskerapp.models import Restaurant, Customer, Driver

#admin.site.register(Restaurant) if uncommented, define self in models.py

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name','phone','address','user')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user','avatar','phone','address')


class DriverAdmin(admin.ModelAdmin):
    list_display = ('user','avatar','phone','address')

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Driver, DriverAdmin)
