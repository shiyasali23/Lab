# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Biometrics, User
# from .scripts import calculate_food_scores  

            
# @receiver(post_save, sender=Biometrics)
# def update_food_scores(sender, instance, **kwargs):
#     user_id = instance.user.id
#     calculate_food_scores(user_id)
