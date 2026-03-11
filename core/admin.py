from django.contrib import admin

# Register your models here.
from core.models import Testing,Transaction
admin.site.register(Testing)
admin.site.register(Transaction)