from django.core.management.base import BaseCommand
from django.test import Client
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Call the register_model view to register machine learning models.'

    def handle(self, *args, **kwargs):
        # Use Django's test client to make a POST request to the view
        client = Client()

        try:
            # Call the register_model view function with an absolute URL
            response = client.post('/api/mlmodels/register_model/')

            # Check the status of the response
            if response.status_code in [200, 201]:
                self.stdout.write(self.style.SUCCESS('Models registered successfully.'))
                logger.info('Models registered successfully.')
            else:
                self.stdout.write(self.style.ERROR(f'Failed to register models: {response.status_code}, {response.content}'))
                logger.error(f'Failed to register models: {response.status_code}, {response.content}')
        except Exception as e:
            # Handle unexpected exceptions
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
            logger.error(f'An error occurred: {str(e)}')
