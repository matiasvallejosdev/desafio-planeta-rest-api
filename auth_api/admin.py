from django.contrib import admin
from auth_api import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass
