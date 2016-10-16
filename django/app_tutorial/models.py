"""This module contains the data models"""

from django.db import models
from django.contrib.auth.models import User


class DivisionAge(models.Model):
    name = models.CharField(max_length=50)
    # In our discussion this was denoted as type, I thought this might be handier.
    age_min = models.IntegerField()
    age_max = models.IntegerField()


class DivisionType(models.Model):
    name = models.CharField(max_length=50)


class FieldType(models.Model):
    type = models.CharField(max_length=50)


class Field(models.Model):
    location = models.CharField(max_length=100)
    type = models.ForeignKey(FieldType)


class Location(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)


class Tournament(models.Model):
    name = models.CharField(max_length=75)
    location = models.ForeignKey(Location)
    date_begin = models.DateField('Begin Date')
    date_end = models.DateField('End Date')
    # type = models.ForeignKey(TournamentType)


class TournamentDivision(models.Model):
    tournament = models.ForeignKey(Tournament)
    age_group = models.ForeignKey(DivisionAge)
    division = models.ForeignKey(DivisionType)


class TournamentField(models.Model):
    tournament = models.ForeignKey(Tournament)
    field = models.ForeignKey(Field)
    field_number = models.CharField(max_length=24)


class Squad(models.Model):
    # TODO: When teams are added, make name nullable and build squad name from division age and type if name is empty.
    division_age = models.ForeignKey(DivisionAge)
    division_type = models.ForeignKey(DivisionType)
    name = models.CharField(max_length=50)
    # team = models.ForeignKey(Team)


class Game(models.Model):
    division = models.ForeignKey(TournamentDivision)  # TODO: Redundant? Contained in Squad.division
    date = models.DateTimeField('Game Time')
    squad_home = models.ForeignKey(Squad, related_name='squad_home')
    squad_away = models.ForeignKey(Squad, related_name='squad_away')
    # type = models.ForeignKey(GameType)
    # round = models.IntegerField()


class GameScore(models.Model):
    score_home = models.IntegerField()
    score_away = models.IntegerField()
    game = models.OneToOneField(Game)


class Profile(models.Model):
    user_id = models.OneToOneField(User)
    number = models.IntegerField(blank=True, null=True)
    birthday = models.DateField('Birthday', blank=True)
    #    nationality = models.ForeignKey(Nationality, blank=True, null=True)
    external_id_type = models.IntegerField(blank=True, null=True)
    external_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        tpl = "{first_name} {last_name} #{number} {team}"
        return tpl.format(first_name=self.user_id.first_name,
                          last_name=self.user_id.last_name,
                          number=self.number,
                          team=self.team_id.name)


class SpiritReport(models.Model):
    squad_from = models.ForeignKey(Squad, related_name='squad_from')
    squad_for = models.ForeignKey(Squad, related_name='squad_for')
    game = models.ForeignKey(Game)


class SpiritScoreCategory(models.Model):
    name = models.CharField(max_length=50)


class SpiritScore(models.Model):
    report = models.ForeignKey(SpiritReport)
    type = models.ForeignKey(SpiritScoreCategory)
    score = models.IntegerField()


class Team(models.Model):
    name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    division = models.ForeignKey(DivisionType)

# ################### Legacy and future work
# class Nationality(models.Model):
#    abbreviation = models.CharField(max_length=5)
#    name = models.CharField(max_length=75)
#
#
# class TournamentType(models.Model):
#    name = models.CharField(max_length=50)
#
#
# class GameType(models.Model):
#     name = models.CharField(max_length=50)
#
#
# class GameReportEventType(models.Model):
#     name = models.CharField(max_length=50)
#
#
# class GameReport(models.Model):
#     game_id = models.ForeignKey(Game)
#     team_id = models.ForeignKey(Team)
#     player_id_assist = models.ForeignKey(Profile, blank=True, null=True,
#                                          related_name='player_assist')
#     player_id_score = models.ForeignKey(Profile, blank=True, null=True,
#                                         related_name='player_score')
#     timestamp = models.DateTimeField('Timestamp')
#     event = models.ForeignKey(GameReportEventType, blank=True, null=True)
#
#
# class TournamentParticipation(models.Model):
#     tournament_id = models.ForeignKey(Tournament)
#     team_id = models.ForeignKey(Team, blank=True)
#     player_id = models.ForeignKey(Profile)
#     player_number = models.IntegerField(blank=True)
