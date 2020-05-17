from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.Message)
class MesasgeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    pass
