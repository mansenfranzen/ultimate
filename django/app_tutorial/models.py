from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateTimeField('Birthday')
    nationality = models.IntegerField()
    external_id_type = models.IntegerField()
    external_id = models.IntegerField()


class Team(models.Model):
    name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    division = models.IntegerField()


class Tournament(models.Model):
    name = models.CharField(max_length=75)
    location = models.CharField(max_length=50)
    date_begin = models.DateTimeField('Begin Date')
    date_end = models.DateTimeField('End Date')
    type = models.IntegerField()


class Game(models.Model):
    tournament_id = models.ForeignKey(Tournament)
    date = models.DateTimeField('Game Time')
    team_id_home = models.ForeignKey(Team)
    team_id_away = models.ForeignKey(Team)
    score_home = models.IntegerField()
    score_away = models.IntegerField()
    type = models.IntegerField()
    round = models.IntegerField()


class GameReport(models.Model):
    game_id = models.ForeignKey(Game)
    player_id_assist = models.ForeignKey(Player)
    player_id_score = models.ForeignKey(Player)
    timestamp = models.DateTimeField('Timestamp')
    event = models.IntegerField()


class SpirtScore(models.Model):
    game_id = models.ForeignKey(Game)
    team_id_providing = models.ForeignKey(Team)
    team_id_receiving = models.ForeignKey(Team)
    score_category = models.IntegerField()
    score = models.IntegerField()


class TournamentParticipation(models.Model):
    tournament_id = models.ForeignKey(Tournament)
    team_id = models.ForeignKey(Team)
    player_id = models.ForeignKey(Player)
    player_number = models.IntegerField()
