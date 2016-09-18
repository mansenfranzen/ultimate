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

