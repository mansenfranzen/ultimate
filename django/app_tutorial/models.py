"""This module contains the data models"""

from django.db import models
from django.contrib.auth.models import User

class Nationality(models.Model):
    abbreviation = models.CharField(max_length=5)
    name = models.CharField(max_length=75)


class Division(models.Model):
    name = models.CharField(max_length=50)


class TournamentType(models.Model):
    name = models.CharField(max_length=50)


class GameType(models.Model):
    name = models.CharField(max_length=50)


class GameReportEventType(models.Model):
    name = models.CharField(max_length=50)


class SpiritScoreCategory(models.Model):
    name = models.CharField(max_length=50)


class Team(models.Model):
    name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    division = models.ForeignKey(Division)


class Profile(models.Model):
    user_id = models.ForeignKey(User, unique=True)
    team_id = models.ForeignKey(Team)
    number = models.IntegerField(blank=True, null=True)
    birthday = models.DateField('Birthday', blank=True)
    nationality = models.ForeignKey(Nationality, blank=True, null=True)
    external_id_type = models.IntegerField(blank=True, null=True)
    external_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        tpl = "{first_name} {last_name} #{number} {team}"
        return tpl.format(first_name=self.user_id.first_name,
                          last_name=self.user_id.last_name,
                          number=self.number,
                          team=self.team_id.name)


class Tournament(models.Model):
    name = models.CharField(max_length=75)
    location = models.CharField(max_length=50)
    date_begin = models.DateField('Begin Date')
    date_end = models.DateField('End Date')
    type = models.ForeignKey(TournamentType)
    division = models.ForeignKey(Division)


class Game(models.Model):
    tournament_id = models.ForeignKey(Tournament)
    date = models.DateTimeField('Game Time')
    team_id_home = models.ForeignKey(Team, related_name='team_home')
    team_id_away = models.ForeignKey(Team, related_name='team_away')
    score_home = models.IntegerField()
    score_away = models.IntegerField()
    type = models.ForeignKey(GameType)
    round = models.IntegerField()


class GameReport(models.Model):
    game_id = models.ForeignKey(Game)
    team_id = models.ForeignKey(Team)
    player_id_assist = models.ForeignKey(Profile, blank=True, null=True,
                                         related_name='player_assist')
    player_id_score = models.ForeignKey(Profile, blank=True, null=True,
                                        related_name='player_score')
    timestamp = models.DateTimeField('Timestamp')
    event = models.ForeignKey(GameReportEventType, blank=True, null=True)


class SpirtScore(models.Model):
    game_id = models.ForeignKey(Game)
    team_id_providing = models.ForeignKey(Team, related_name='team_providing')
    team_id_receiving = models.ForeignKey(Team, related_name='team_receiving')
    score_category = models.ForeignKey(SpiritScoreCategory)
    score = models.IntegerField()


class TournamentParticipation(models.Model):
    tournament_id = models.ForeignKey(Tournament)
    team_id = models.ForeignKey(Team, blank=True)
    player_id = models.ForeignKey(Profile)
    player_number = models.IntegerField(blank=True)
