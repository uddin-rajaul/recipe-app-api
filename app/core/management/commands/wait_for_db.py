"""
Django command to wait to be available.
"""
from typing import Any, Optional
from django.core.management import BaseCommand

class Command(BaseCommand):
    """Django command to wait for database."""
    def handle(self, *args: Any, **options) :
        pass