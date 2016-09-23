"""This module provides a convenient way to create some sample and testing
data.
"""

from django.core.management.base import BaseCommand
from ...models import User, Profile, Team
from sampledatahelper.model_helper import ModelDataHelper
from sampledatahelper.helper import SampleDataHelper

user_cnt = 200
team_cnt = 10

class Command(BaseCommand):
    sd = SampleDataHelper(seed=27)
    mdh = ModelDataHelper(seed=27)

    def handle(self, *args, **options):
        self.mdh.fill_model(User, user_cnt,
                            is_superuser=0,
                            username=lambda instance, sd: sd.name() + " " +
                                                          sd.surname() + " " +
                                                          sd.hex_chars(),
                            first_name=lambda instance, sd: sd.name(),
                            last_name=lambda instance, sd: sd.surname(),
                            email=lambda instance, sd: sd.email(),
                            password=lambda instance, sd: sd.chars(10, 20))

        # self.mdh.fill_model(Profile, user_cnt)

        self.mdh.fill_model(Team, team_cnt,
                            name= lambda instance, sd: sd.fullname(),
                            origin=lambda instance, sd: sd.fullname() + " " +
                                                        sd.zip_code("es"))
