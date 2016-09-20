from django.contrib import admin

# Register your models here.

from .models import Tournament, Team, TournamentParticipation, Game, \
    GameReport, SpirtScore, Player

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Tournament)
admin.site.register(TournamentParticipation)
admin.site.register(Game)
admin.site.register(GameReport)
admin.site.register(SpirtScore)
