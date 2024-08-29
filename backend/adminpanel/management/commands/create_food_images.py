from django.core.management.base import BaseCommand
from django.db import transaction
from django.core.files import File
from adminpanel.models import Food, FoodImage
import os

class Command(BaseCommand):
    help = 'Create Food Images from PNG files'

    def handle(self, *args, **kwargs):
        food_image_path = '/Users/shiyas/Desktop/code-red/Lab/datasets/food_images'

        if not os.path.exists(food_image_path):
            self.stderr.write(self.style.ERROR(f"Directory {food_image_path} does not exist."))
            return

        image_files = [f for f in os.listdir(food_image_path) if f.endswith('.png')]
        food_images = {}
        failed_foods = []

        for image_file in image_files:
            food_name = os.path.splitext(image_file)[0]
            try:
                food = Food.objects.get(name=food_name)
                food_images[food] = image_file
            except Food.DoesNotExist:
                failed_foods.append(food_name)

        if not food_images:
            self.stderr.write(self.style.ERROR("No matching foods found for the images."))
            return

        with transaction.atomic():
            for food, image_file in food_images.items():
                try:
                    image_path = os.path.join(food_image_path, image_file)
                    with open(image_path, 'rb') as img_file:
                        food_image, created = FoodImage.objects.get_or_create(food=food)
                        if created:
                            food_image.image.save(image_file, File(img_file))
                            self.stdout.write(self.style.SUCCESS(f"Image {image_file} added to Food {food_name}."))
                        else:
                            self.stdout.write(self.style.WARNING(f"Food {food_name} already has an image."))
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Error processing {image_file}: {e}"))
                    # Automatically rollback the transaction in case of error

        if failed_foods:
            self.stderr.write(self.style.ERROR(f"No matching Food objects found for the following names: {', '.join(failed_foods)}"))
        else:
            self.stdout.write(self.style.SUCCESS("All images processed successfully."))
