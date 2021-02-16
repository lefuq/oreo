from django.contrib import admin
from .models import Addressee, Phone, Mail


@admin.register(Addressee)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth', 'sex')


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'phone_number', 'phone_type')


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'mail_address', 'mail_type')
