from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='root@sky.pro',
            first_name='Root',
            last_name='SkyPro',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('12345678')
        user.save()