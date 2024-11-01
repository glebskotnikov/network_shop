from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@yandex.ru",
            name="Admin",
            country="Brazil",
            city="Rio",
            street="Avenida Vieira Souto",
            house_number="13",
            role="a",
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )

        user.set_password("123qwe456rty")
        user.save()
