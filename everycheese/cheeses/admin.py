from django.contrib import admin
from .models import Cheese

@admin.register(Cheese)
class CheeseAdmin(admin.ModelAdmin):
    fields       = ("name", "country", "description")   # orden personalizado
    list_display = ("name", "country", "added_by")