from django.db import models
from django.db.models import Index
from adminpanel.models import Food, Biochemical
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
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
        user.save()
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
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    email = models.EmailField(unique=True, db_index=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True, db_index=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    job = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField()
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth', 'gender']
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    class Meta:
        indexes = [
            Index(fields=['email']),
            Index(fields=['phone_number']),
        ]

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'

class Biometrics(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='biometrics', db_index=True)
    biochemical = models.ForeignKey(Biochemical, on_delete=models.CASCADE, related_name='biometrics', db_index=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    scaled_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        indexes = [
            Index(fields=['user']),
            Index(fields=['biochemical']),
            Index(fields=['created']),
        ]

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.biochemical.name} - {self.value}'

class FoodScore(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='food_scores', db_index=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='food_scores', db_index=True)
    score = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        indexes = [
            Index(fields=['user']),
            Index(fields=['food']),
            Index(fields=['created']),
        ]

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.food.name} - {self.score}'