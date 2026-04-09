from django.core.management.base import BaseCommand
from django.utils import timezone

from scoredboard.models import Game


class Command(BaseCommand):
    help = (
        "Deletes games that have passed their expiry time or have been marked inactive"
    )

    def handle(self, *args, **options):
        expired = Game.objects.filter(
            expires_at__lt=timezone.now()
        ) | Game.objects.filter(is_active=False)
        count, _ = expired.delete()
        self.stdout.write(self.style.SUCCESS(f"Deleted {count} expired game(s)"))
