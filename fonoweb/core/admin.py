from django.contrib import admin
from .models import Client
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ("user","birth_date")


admin.site.register(Client,ClientAdmin)