from django.contrib import admin
from NPC_Gen.models import NPC

# Register your models here.
@admin.register(NPC)
class NPCAdmin(admin.ModelAdmin):
    list_display = ('name', 'race', 'char_class')