import os
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.db import connection  
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Delete all tables, sequences, and views in the PostgreSQL database'

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
                        
            call_command('makemigrations')
            call_command('migrate')            

            

            self.stdout.write(self.style.SUCCESS('Database deleted successfully.'))

        except Exception as e:
            raise CommandError(f'Error creating admin data: {str(e)}')
