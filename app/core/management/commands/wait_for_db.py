"""
Django command to wait to be available.
"""
from psycopg2 import OperationalError as Psycopg20pError
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entry point for command."""
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg20pError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
        self.stdout.write(self.style.SUCCESS('Database available!'))
