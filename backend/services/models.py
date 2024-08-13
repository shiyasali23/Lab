from django.db import models
from django.db.models import Index
from adminpanel.models import Food, Biochemical
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        abstract = True

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

# User Model
class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
    ]

    email = models.EmailField(unique=True, db_index=True)
    first_name = models.CharField(max_length=150)  # Reduced length for memory efficiency
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15, blank=True, null=True, db_index=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    job = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField()
    height = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)  # Smaller range for precision
    weight = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth', 'gender']

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    class Meta:
        db_table = 'services_user'
        indexes = [
            Index(fields=['email']),
            Index(fields=['phone_number']),
        ]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Biometrics Model
class Biometrics(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='biometrics', db_index=True)

    class Meta:
        indexes = [models.Index(fields=['user'])]

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

# Biometrics Entry Model
class BiometricsEntry(BaseModel):
    biometrics = models.ForeignKey(Biometrics, on_delete=models.CASCADE, related_name='entries', db_index=True)

    class Meta:
        indexes = [models.Index(fields=['biometrics'])]

    def __str__(self):
        return f'{self.biometrics.user.first_name} {self.biometrics.user.last_name} - Entry {self.id}'

# Biometrics Value Model
class BiometricsValue(BaseModel):
    biochemical = models.ForeignKey(Biochemical, on_delete=models.CASCADE, related_name='values', db_index=True)
    value = models.DecimalField(max_digits=8, decimal_places=2)  # Reduced max digits to save space
    scaled_value = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    biometrics_entry = models.ForeignKey(BiometricsEntry, on_delete=models.CASCADE, related_name='values', db_index=True, null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=['biochemical'])]

    def __str__(self):
        return f'{self.biometrics_entry.biometrics.user.first_name} {self.biometrics_entry.biometrics.user.last_name} - {self.biochemical.name} - {self.scaled_value}'

    def scale_biometrics(self, healthy_min, healthy_max, value):
        optimum_value = (healthy_min + healthy_max) / 2
        if healthy_min <= value <= healthy_max:
            return round(2 * (value - optimum_value) / (healthy_max - healthy_min), 2)
        elif value < healthy_min:
            return round((value - healthy_min) - 1, 2)
        elif value > healthy_max:
            return round((value - healthy_max) + 1, 2)

    def save(self, *args, **kwargs):
        if self.value is not None and self.biochemical is not None:
            user = self.biometrics_entry.biometrics.user
            if user.gender == 'female':
                healthy_min = self.biochemical.female_min
                healthy_max = self.biochemical.female_max
            elif user.gender == 'male':
                healthy_min = self.biochemical.male_min
                healthy_max = self.biochemical.male_max

            self.scaled_value = self.scale_biometrics(healthy_min, healthy_max, float(self.value))

        super().save(*args, **kwargs)

# Food Score Model
class FoodScore(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='food_scores', db_index=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='food_scores', db_index=True)
    score = models.DecimalField(max_digits=5, decimal_places=2)  

    class Meta:
        indexes = [
            Index(fields=['user']),
            Index(fields=['food']),
        ]

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.food.name} - {self.score}'
