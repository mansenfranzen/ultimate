from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)


class Tournament(models.Model):
    name = models.CharField(max_length=75)
    location = models.CharField(max_length=50)
    date_begin = models.DateTimeField('Begin Date')
    date_end = models.DateTimeField('End Date')
    type = models.IntegerField()


class Game(models.Model):
    tournament = models.ForeignKey(Tournament)
    time_stamp = models.DateTimeField('Game Time')
    type = models.IntegerField()


class GameScore(models.Model):
    game = models.ForeignKey(Game)
    team = models.ForeignKey(Team)
    value = models.IntegerField()


class SpirtScore(models.Model):
    game = models.ForeignKey(Game)
    subject = models.ForeignKey(Team)
    object = models.ForeignKey(Team)
    type = models.IntegerField()
    value = models.IntegerField()
