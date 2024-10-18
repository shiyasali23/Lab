from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a regular user with only mandatory fields.'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.create_user(
                email = "m@g.com",
                password = "x",
                first_name = "Muhsina",
                last_name = "hashim",
                date_of_birth = "1985-07-30",  
                gender = "female",
            )
            self.stdout.write(self.style.SUCCESS(f'User "{user.get_full_name()}" created successfully with email "{user.email}".'))

        except Exception as e:
            raise CommandError(f'Error creating user: {str(e)}')
