from django.contrib import admin

from .models import ProcessoAdm

@admin.register(ProcessoAdm)
class ProcessoAdmAdmin(admin.ModelAdmin):
    list_display = ('numero', 'user_create')