from django.contrib import admin

from .models import Drink, Operation

class OperationAdmin(admin.ModelAdmin):
    list_display = ('data', 'operation', 'drink')
    search_fields = ('data', 'operation', 'drink')


admin.site.register(Drink)
admin.site.register(Operation, OperationAdmin)
