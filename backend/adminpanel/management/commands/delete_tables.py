from django.core.management.base import BaseCommand
from services.models import User

class Command(BaseCommand):
    help = 'Delete users with a specific phone number'

    def add_arguments(self, parser):
        parser.add_argument(
            '--phone_number',
            type=str,
            help='Phone number of the users to delete',
        )

    def handle(self, *args, **kwargs):
        phone_number = kwargs['phone_number']
        if not phone_number:
            self.stdout.write(self.style.ERROR('You must provide a phone number using --phone_number'))
            return

        deleted_count, _ = User.objects.filter(phone_number=phone_number).delete()
        if deleted_count:
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {deleted_count} users with phone number {phone_number}'))
        else:
            self.stdout.write(self.style.WARNING(f'No users found with phone number {phone_number}'))
