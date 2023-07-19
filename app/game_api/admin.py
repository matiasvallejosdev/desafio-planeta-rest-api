from django.contrib import admin
from .models import *


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    pass


@admin.register(Piece)
class PieceAdmin(admin.ModelAdmin):
    pass


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass
