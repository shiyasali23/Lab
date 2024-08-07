from django.db import models
from django.db.models import Index

class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=255, db_index=True, unique=True)

    class Meta:
        indexes = [
            Index(fields=['name'])
        ]

    def __str__(self):
        return self.name

class SubCategory(BaseModel):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', db_index=True, null=True, blank=True)

    class Meta:
        indexes = [
            Index(fields=['name']), 
            Index(fields=['category'])
        ]

    def __str__(self):
        return self.name

class Condition(BaseModel):
    name = models.CharField(max_length=255, db_index=True, unique=True)

    class Meta:
        indexes = [
            Index(fields=['name'])
        ]

    def __str__(self):
        return self.name

class Biochemical(BaseModel):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='biochemicals', null=True, blank=True, db_index=True)
    female_min = models.FloatField()
    female_max = models.FloatField()
    male_min = models.FloatField()
    male_max = models.FloatField()
    unit = models.CharField(max_length=50, default='g/dL')
    hyper_conditions = models.ManyToManyField(Condition, related_name='hyper_conditions_for_biochemicals', blank=True)
    hypo_conditions = models.ManyToManyField(Condition, related_name='hypo_conditions_for_biochemicals', blank=True)

    class Meta:
        indexes = [
            Index(fields=['name']),
            Index(fields=['category'])
        ]

    def __str__(self):
        return self.name

class Food(BaseModel):
    name = models.CharField(max_length=255, db_index=True,unique=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='foods', null=True, blank=True, db_index=True)

    class Meta:
        indexes = [
            Index(fields=['name']), 
            Index(fields=['subcategory'])
        ]

    def __str__(self):
        return self.name

class Nutrient(BaseModel):
    name = models.CharField(max_length=255,unique=True, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='nutrients', db_index=True)
    unit = models.CharField(max_length=50)

    class Meta:
        indexes = [
            Index(fields=['name']), 
            Index(fields=['category']), 
        ]

    def __str__(self):
        return f"{self.name} ({self.unit})"


class FoodNutrient(BaseModel):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='food_nutrients', db_index=True)
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE, related_name='food_utrients', db_index=True)
    value = models.FloatField()

    class Meta:
        indexes = [
            Index(fields=['food']),
            Index(fields=['nutrient']),
            Index(fields=['value']),
        ]

    def __str__(self):
        return f"{self.food} - {self.nutrient}"


class Weight(BaseModel):
    weight = models.FloatField(db_index=True)
    biochemical = models.ForeignKey(Biochemical, on_delete=models.CASCADE, related_name='weights', db_index=True)
    nutrient = models.ForeignKey(Nutrient, null=True, blank=True, on_delete=models.CASCADE, related_name='weights', db_index=True)
    food = models.ForeignKey(Food, null=True, blank=True, on_delete=models.CASCADE, related_name='weights', db_index=True)

    class Meta:
        indexes = [
            Index(fields=['biochemical']),
            Index(fields=['nutrient']),
            Index(fields=['food']),
            Index(fields=['weight']),
        ]
        ordering = ['-weight']

    def __str__(self):
        return f'{self.biochemical} - {self.nutrient} - {self.food} - {self.weight}'


