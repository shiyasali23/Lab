import os
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.db import connection  
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates the initial admin data and superuser'

    def handle(self, *args, **kwargs):
        try:
            # Dropping all tables, sequences, and views in the PostgreSQL database
            with connection.cursor() as cursor:
                cursor.execute("""
                    DO $$ 
                    DECLARE
                        r RECORD;
                    BEGIN
                        -- Drop all tables in the current schema
                        FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = current_schema()) LOOP
                            EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
                        END LOOP;

                        -- Drop all sequences in the current schema
                        FOR r IN (SELECT sequence_name FROM information_schema.sequences WHERE sequence_schema = current_schema()) LOOP
                            EXECUTE 'DROP SEQUENCE IF EXISTS ' || quote_ident(r.sequence_name) || ' CASCADE';
                        END LOOP;
                        
                        -- Drop all views in the current schema
                        FOR r IN (SELECT table_name FROM information_schema.views WHERE table_schema = current_schema()) LOOP
                            EXECUTE 'DROP VIEW IF EXISTS ' || quote_ident(r.table_name) || ' CASCADE';
                        END LOOP;
                    END $$;
                """)

            # Remove all migration files that start with '00'
            migrations_dirs = ['services/migrations/', 'adminpanel/migrations/', 'mlmodels/migrations/', 'diagnosis/migrations/']
            for migrations_dir in migrations_dirs:
                for file in os.listdir(migrations_dir):
                    if file.endswith('.py') and file.startswith('00'):
                        os.remove(os.path.join(migrations_dir, file))

            # Recreate migrations and apply them
            call_command('makemigrations')
            call_command('migrate')

            # Run custom management commands for initial data
            call_command('create_biochemical_units')
            call_command('create_nutrient_categories')
            call_command('create_biochemical_conditions')
            call_command('create_food_nutrients')
            call_command('create_food_bias_weights')
            call_command('create_nutrients_bias_weights')
            call_command('normalize_nutriscore_nutreint')
            call_command('check_normalized_nutrients')
            call_command('create_diagnosis')
            call_command('register_ml_models')
            
            call_command('create_user')
            call_command('create_user_biometrics')

            # Create superuser if it doesn't already exist
            User = get_user_model()
            if not User.objects.filter(email="s@g.com").exists():
                User.objects.create_superuser(
                    email="s@g.com",
                    first_name="s",
                    last_name="s",
                    date_of_birth="1111-11-11",
                    gender="male",
                    phone_number=1111111111,
                    height_cm=175.0,
                    weight_kg=68.0,
                    password="x"
                )

            self.stdout.write(self.style.SUCCESS('Admin data and superuser created successfully.Now you can continue'))

        except Exception as e:
            raise CommandError(f'Error creating admin data: {str(e)}')
