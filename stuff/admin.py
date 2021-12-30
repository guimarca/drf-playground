from django.contrib import admin

from stuff.models import Stuff


@admin.register(Stuff)
class StuffAdmin(admin.ModelAdmin):
    pass
