from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(DivisionAge)
admin.site.register(DivisionType)
admin.site.register(Field)
admin.site.register(FieldType)
admin.site.register(Game)
admin.site.register(GameScore)
admin.site.register(Location)
admin.site.register(Profile)
admin.site.register(SpiritReport)
admin.site.register(SpiritScore)
admin.site.register(SpiritScoreCategory)
admin.site.register(Squad)
admin.site.register(Team)
admin.site.register(Tournament)
admin.site.register(TournamentDivision)
admin.site.register(TournamentField)
