# Generated by Django 4.2.14 on 2024-08-07 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0002_user_groups_user_is_active_user_is_staff_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("male", "male"), ("female", "female")], max_length=6
            ),
        ),
        migrations.AlterModelTable(
            name="user",
            table="services_user",
        ),
    ]