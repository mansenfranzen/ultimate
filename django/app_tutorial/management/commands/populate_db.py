"""This module is used to populate common tables."""

# TODO: Fix according to new model
import pandas as pd
import os
from django.core.management.base import BaseCommand
from ...models import *

BASE_URL = os.path.join('..', 'material', 'db_populate', '_db_populate_{class_name}.csv')


class Command(BaseCommand):
    @staticmethod
    def populate_from_csv(model):
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
        classes = [SpiritScoreCategory]
        for class_name in classes:
            self.populate_from_csv(class_name)
