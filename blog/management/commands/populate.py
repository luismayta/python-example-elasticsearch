# -*- coding: utf-8 -*-
import os
from typing import List, Set

from django.conf import settings
from django.apps import apps
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    """
    Populate with a fixtures directory from all apps.
    """

    _extensions_allowed = ("yaml", "yml", "json")
    _files_ignored = "test"
    _message_finish = "Successfully populated"

    help = "Populate with a fixtures directory from all apps"

    def _get_list_files(self, path: str) -> List:
        """
        Given a directory path returns a list of all files inside it.
        """

        list_files = []
        for (_, _, filenames) in os.walk(path):
            filenames_valid: list = []
            for filename in filenames:
                is_valid_file = [
                    filename != self._files_ignored,
                    filename.split(".")[-1] in self._extensions_allowed,
                ]
                if all(is_valid_file):
                    filenames_valid.append(filename)
            if not filenames_valid:
                continue
            list_files.extend(filenames_valid)
        return list_files

    def get_fixture_paths(self) -> List:
        """
        Get a list of all fixture files inside fixture directory.
        """
        fixtures: List = []

        for app_path in [a.path for a in apps.get_app_configs()]:
            fixture_path = os.path.join(app_path, "fixtures")
            if os.path.exists(fixture_path):
                fixtures.extend(self._get_list_files(fixture_path))
        return fixtures

    def get_fixtures(self) -> List:
        fixtures_order: List = settings.FIXTURES_ORDER.copy()
        fixtures: Set = set(self.get_fixture_paths()).difference(
            set(settings.FIXTURES_IGNORED)
        )
        if len(fixtures_order) <= len(settings.FIXTURES_ORDER):
            fixtures_order.extend(list(set(fixtures)))
        return fixtures_order

    def handle(self, *args, **options) -> None:
        fixtures = self.get_fixtures()
        if not fixtures:
            return None
        for fixture in fixtures:
            call_command("loaddata", fixture, verbosity=1)
        self.stdout.write(self.style.SUCCESS(self._message_finish))
