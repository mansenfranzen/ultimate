from django.contrib import admin

# Register your models here.

from .models import Tournament, Team, TournamentParticipation, Game, \
    GameReport, SpirtScore, Profile, Nationality, Division, TournamentType, \
    GameReportEventType, GameType, SpiritScoreCategory

admin.site.register(Profile)
admin.site.register(Team)
admin.site.register(Tournament)
admin.site.register(TournamentParticipation)
admin.site.register(Game)
admin.site.register(GameReport)
admin.site.register(SpirtScore)
admin.site.register(Nationality)
admin.site.register(Division)
admin.site.register(TournamentType)
admin.site.register(GameReportEventType)
admin.site.register(GameType)
admin.site.register(SpiritScoreCategory)