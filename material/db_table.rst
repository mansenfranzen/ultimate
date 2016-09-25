Updated DB schema
=================

See additional notes below.

.. image::  https://cdn.rawgit.com/mansenfranzen/ultimate/master/material/db_model_25092016.svg

:Game:
  The ``type`` column defines the kind of game including group, crossover and knockout games (and others...).
  The ``round`` column additionaly indicates the ascending order of games being played at a tournament.
  Both columns may provide sufficient information to construct the entire playing schedule.
  
:Team:
  The ``division`` column refers to the kind of division a team belongs to. The same team may participate in multiple divisions like Open and Mixed. See `here
  <http://ultimateliga.de/index.php/deutsche-meisterschaften>`_ for more.
  
:Tournament:
  The ``type`` column indicates the tournament category like fun tournaments, nationals or european championships.
  The ``division`` column refers to the kind of division of a tournament.
  
:SpiritScore:
  The ``score_category`` column states the spirit dimension on which a value is given. See `here
  <http://www.wfdf.org/sotg/spirit-rules-a-scoring>`_ for more.
  
:GameReport:
  The ``event`` column identifies game events like regular points, callahan points, turnovers, start and end times (per point and game), timeouts, substitutions, half time etc.
  The ``team_id`` columns is included to define events triggered by one team (like time outs).
  
:Profile:
  The *Profile* table extends the builtin django.conrib.auth.user table.
  The ``team`` and ``number`` columns define the current main team and number of the player. These values are used as default values in the ``TournamentParticipation`` table (if not explicitly set).
  The ``external_id`` column may be used to create a reference of to an external source of players information.
  The ``external_id_type`` column is intended to account for different types of external sources, like the DFV or european players databases.
  
  

