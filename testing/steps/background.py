# -*- coding: utf-8 -*-

from behave import given
from django.core.management import call_command


@given('load data "{filename}"')
def load_data_filename(context, filename):
    """
    BACKGROUND steps are called at begin of each scenario before other steps.
    """
    call_command("loaddata", filename, verbosity=1)
