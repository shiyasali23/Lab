# Generated by Django 4.2.14 on 2024-08-06 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminpanel", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="biochemical",
            name="unit",
            field=models.CharField(default="g/dL", max_length=50),
        ),
    ]