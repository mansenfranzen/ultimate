"""This module is used to populate common tables."""

import pandas as pd
from django.core.management.base import BaseCommand
from ...models import Nationality, Division, TournamentType, GameType, \
    GameReportEventType, SpiritScoreCategory

BASE_URL = "https://raw.githubusercontent.com/mansenfranzen/ultimate/" \
              "master/material/db_populate/_db_populate_{class_name}.csv"


class Command(BaseCommand):


    def populate_from_csv(self, model):
        """Fetch csv from github repo and populate db table.

        The read_csv method requires the keep_default_na and na_values
        parameters because it otherwise interpretes Namibias 'NA' as an np.nan
        for example.
        """

        class_name = model.__name__
        print("Populating {}...".format(class_name))
        url = BASE_URL.format(class_name=class_name.lower())
        csv = pd.read_csv(url, header=0, keep_default_na=False, na_values=[])

        for idx, row in csv.iterrows():
            model.objects.create(**row.to_dict())


    def handle(self, *args, **options):
        self.populate_from_csv(Nationality)
        self.populate_from_csv(Division)
        self.populate_from_csv(TournamentType)
        self.populate_from_csv(GameType)
        self.populate_from_csv(GameReportEventType)
        self.populate_from_csv(SpiritScoreCategory)