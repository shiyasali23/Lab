import os
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates the initial admin data and superuser'

    def handle(self, *args, **kwargs):
        try:
            if os.path.exists('db.sqlite3'):
                os.remove('db.sqlite3')
            migrations_dirs = ['services/migrations/', 'adminpanel/migrations/']
            for migrations_dir in migrations_dirs:
                for file in os.listdir(migrations_dir):
                    if file.endswith('.py') and file.startswith('00'):
                        os.remove(os.path.join(migrations_dir, file))


            call_command('makemigrations')
            call_command('migrate')


            call_command('create_biochemical_units')
            call_command('create_nutrient_categories')
            call_command('create_biochemical_conditions')
            call_command('create_food_nutrients')
            call_command('create_food_bias_weights')
            call_command('create_nutrients_bias_weights')
            call_command('normalize_nutriscore_nutreint')
            call_command('check_normalized_nutrients')


            User = get_user_model()
            if not User.objects.filter(email="s@g.com").exists():
                User.objects.create_superuser(
                    email="s@g.com",
                    first_name="s",
                    last_name="s",
                    date_of_birth="1111-11-11",
                    gender="male",
                    password="x"
                )
            self.stdout.write(self.style.SUCCESS('Admin data and superuser created successfully.'))

        except Exception as e:
            raise CommandError(f'Error creating admin data: {str(e)}')
