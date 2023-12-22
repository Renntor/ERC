from django.core.management import BaseCommand
from users.models import User
import os
from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('EMAIL_ADMIN'),
            is_staff=True,
            is_superuser=True,
        )
        user.set_password(os.getenv('PASSWORD_ADMIN'))
        user.save()
