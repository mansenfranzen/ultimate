from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.DivisionAge)
admin.site.register(models.DivisionType)
admin.site.register(models.Field)
admin.site.register(models.FieldType)
admin.site.register(models.Game)
admin.site.register(models.GameScore)
admin.site.register(models.Location)
admin.site.register(models.Profile)
admin.site.register(models.SpiritReport)
admin.site.register(models.SpiritScore)
admin.site.register(models.SpiritScoreCategory)
admin.site.register(models.Squad)
admin.site.register(models.Team)
admin.site.register(models.Tournament)
admin.site.register(models.TournamentDivision)
admin.site.register(models.TournamentField)
