Updated DB schema
=================

See additional notes below.

.. image::  https://cdn.rawgit.com/mansenfranzen/ultimate/master/material/db_model_19092016.svg

:game:
  The ``type`` column defines the kind of game including group, crossover and knockout games (and others...).
  The ``round`` column additionaly indicates the ascending order of games being played at a tournament.
  Both columns may provide sufficient information to construct the entire playing schedule.
  
:team:
  The ``division`` column refers to the kind of division a team belongs to. The same team may participate in multiple divisions like Open and Mixed. See `here
  <http://ultimateliga.de/index.php/deutsche-meisterschaften>`_ for more.
  
:tournament:
  The ``type`` column indicates the tournament category like fun tournaments, nationals or european championships.
  
:spirit_score:
  The ``score_category`` column states the spirit dimension on which a value is given. See `here
  <http://www.wfdf.org/sotg/spirit-rules-a-scoring>`_ for more.
  
:game_report:
  The ``event`` column may identify game events like the start and end time of points, timeouts or half time.
  
:player:
  The ``external_id`` column may be used to create a reference of to an external source of players information.
  The ``external_id_type`` column is intended to account for different types of external sources, like the DFV or european players databases.
  
  

