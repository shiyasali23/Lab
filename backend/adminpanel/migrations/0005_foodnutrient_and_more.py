# Generated by Django 4.2.14 on 2024-08-06 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("adminpanel", "0004_alter_subcategory_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="FoodNutrient",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("value", models.FloatField()),
            ],
        ),
        migrations.RemoveIndex(
            model_name="nutrient",
            name="adminpanel__food_id_87d658_idx",
        ),
        migrations.RemoveField(
            model_name="nutrient",
            name="food",
        ),
        migrations.RemoveField(
            model_name="nutrient",
            name="value",
        ),
        migrations.AddField(
            model_name="foodnutrient",
            name="food",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="food_nutrients",
                to="adminpanel.food",
            ),
        ),
        migrations.AddField(
            model_name="foodnutrient",
            name="nutrient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="food_utrients",
                to="adminpanel.nutrient",
            ),
        ),
        migrations.AddIndex(
            model_name="foodnutrient",
            index=models.Index(fields=["food"], name="adminpanel__food_id_853b20_idx"),
        ),
        migrations.AddIndex(
            model_name="foodnutrient",
            index=models.Index(
                fields=["nutrient"], name="adminpanel__nutrien_487e31_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="foodnutrient",
            index=models.Index(fields=["value"], name="adminpanel__value_ec5d4e_idx"),
        ),
    ]