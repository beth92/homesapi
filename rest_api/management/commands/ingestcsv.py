import csv
import os
from typing import Dict


from django.conf import settings
from django.db import transaction
from django.core.management.base import BaseCommand, CommandError, CommandParser

from ...serializers import HomeSerializer


class Command(BaseCommand):
    help = 'Parse a CSV into a list of homes to be saved in the DB'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('file', type=str, nargs='?', default='rest_api/resources/sample.csv')

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, kwargs['file'])
        with open(file_path, mode='r') as input_file:
            reader = csv.DictReader(input_file)
            with transaction.atomic():
                [create_home_from_csv_row(row, reader.line_num) for row in reader]


def create_home_from_csv_row(row: Dict[str, str], row_number) -> None:
    home_data = remove_empty_values(row)
    home = HomeSerializer(data=home_data)
    if home.is_valid():
        home.save()
    else:
        raise CommandError(
            f'Invalid row found at line {row_number}.\n' +
            f'Errors: {home.errors}'
        )


def remove_empty_values(row: Dict[str, str]) -> Dict[str, str]:
    """
    Remove blank values from row so they are treated as null in db
    """
    return {k: v for k, v in row.items() if v != ''}
