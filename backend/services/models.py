from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import timedelta

class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        abstract = True

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

class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
    ]

    email = models.EmailField(unique=True, db_index=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15, unique=True, db_index=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    job = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField()
    height_cm = models.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        blank=True, 
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(300)]  
    )
    weight_kg = models.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        blank=True, 
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(300)]  
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth', 'gender']

    class Meta:
        db_table = 'services_user'
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['phone_number']),
        ]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

class Biometrics(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='biometrics')

    class Meta:
        indexes = [models.Index(fields=['user'])]

    def __str__(self):
        return f'Biometrics for {self.user.get_full_name()}'

class BiometricsValue(BaseModel):
    biochemical = models.ForeignKey('adminpanel.Biochemical', on_delete=models.CASCADE, related_name='values')
    value = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    scaled_value = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    biometrics = models.ForeignKey(Biometrics, on_delete=models.CASCADE, related_name='entries')
    expired_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=['biochemical']), models.Index(fields=['biometrics'])]

    def __str__(self):
        return f'{self.biometrics.user.get_full_name()} - {self.biochemical.name} - {self.scaled_value}'

    def scale_biometrics(self):
        if self.value is None or self.biochemical is None:
            return None

        user = self.biometrics.user
        healthy_min, healthy_max = self.get_healthy_range(user.gender)
        if healthy_min is None or healthy_max is None:
            return None
        
        optimum_value = (healthy_min + healthy_max) / 2
        value = float(self.value)

        if healthy_min <= value <= healthy_max:
            return round(2 * (value - optimum_value) / (healthy_max - healthy_min), 2)
        elif value < healthy_min:
            return round((value - healthy_min) - 1, 2)
        else:
            return round((value - healthy_max) + 1, 2)

    def get_healthy_range(self, gender):
        if gender == 'female':
            return self.biochemical.female_min, self.biochemical.female_max
        return self.biochemical.male_min, self.biochemical.male_max

    def save(self, *args, **kwargs):
        if self.biochemical:
            self.expired_date = timezone.now() + timedelta(days=self.biochemical.validity_days)
        self.scaled_value = self.scale_biometrics()
        super().save(*args, **kwargs)

class FoodScore(BaseModel):
    biometrics = models.ForeignKey(Biometrics, on_delete=models.CASCADE, related_name='food_scores')
    food = models.ForeignKey('adminpanel.Food', on_delete=models.CASCADE, related_name='food_scores')
    score = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=['biometrics']),
            models.Index(fields=['food']),
        ]

    def __str__(self):
        return f'{self.biometrics.user.get_full_name()} - {self.food.name} - {self.score}'
