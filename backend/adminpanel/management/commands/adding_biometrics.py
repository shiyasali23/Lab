from django.core.management.base import BaseCommand
from adminpanel.models import Biochemical
from services.models import Biometrics,User
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Process food biochemicals data from a CSV file'

    def handle(self, *args, **kwargs):
        user_data = {
            "id": 5,
            "email": "muhsina@example.com",
            "first_name": "Muhsina",
            "last_name": "Hashim",
            "phone_number": "+1234567890",
            "city": "Kozhikode",
            "address": "123 Main St",
            "job": "House maker",
            "date_of_birth": "1989-04-11",
            "height": "165.00",
            "weight": "80.00",
            "gender": "female",
            "biometrics": {
                "Blood Glucose": {"value": 103},
                "Hemoglobin A1c": {"value": 5.7},
                "Glycated Albumin": {"value": 15.5},
                "Total Cholesterol": {"value": 204},
                "LDL Cholesterol": {"value": 130},
                "HDL Cholesterol": {"value": 55},
                "Triglycerides": {"value": 150},
                "Apolipoprotein A1": {"value": 160},
                "Apolipoprotein B": {"value": 110},
                "Vitamin D": {"value": 18},
                "Vitamin C": {"value": 8},
                "Vitamin K": {"value": 1.5},
                "Vitamin B6 (Pyridoxine)": {"value": 30},
                "Vitamin B1 (Thiamine)": {"value": 120},
                "Vitamin B2 (Riboflavin)": {"value": 20},
                "Vitamin B3 (Niacin)": {"value": 25},
                "Vitamin B5 (Pantothenic Acid)": {"value": 500},
                "Vitamin B7 (Biotin)": {"value": 600},
                "Vitamin B9 (Folate)": {"value": 3.0},
                "Vitamin B12 (Cobalamin)": {"value": 220},
                "Vitamin A": {"value": 45},
                "Creatinine": {"value": 0.9},
                "Uric Acid": {"value": 5.0},
                "Blood Urea Nitrogen": {"value": 18},
                "Cystatin C": {"value": 0.85},
                "Sodium": {"value": 140},
                "Potassium": {"value": 4.2},
                "Calcium": {"value": 9.5},
                "Magnesium": {"value": 1.9},
                "Phosphate": {"value": 3.5},
                "Chloride": {"value": 102},
                "Bicarbonate": {"value": 26},
                "Iron": {"value": 60},
                "Globulin": {"value": 2.8},
                "Albumin": {"value": 4.2},
                "Total Protein": {"value": 7.0},
                "Albumin/Globulin Ratio": {"value": 1.5},
                "C-Reactive Protein": {"value": 2.5},
                "Haptoglobin": {"value": 120},
                "Transferrin": {"value": 280},
                "C-Peptide": {"value": 2.5},
                "Testosterone": {"value": 40},
                "Estrogen": {"value": 45},
                "Progesterone": {"value": 0.5},
                "Cortisol": {"value": 20},
                "Aldosterone": {"value": 10},
                "Thyroid-Stimulating Hormone (TSH)": {"value": 3.8},
                "Free Thyroxine (Free T4)": {"value": 1.2},
                "Free Triiodothyronine (Free T3)": {"value": 3.2},
                "Aspartate Aminotransferase": {"value": 28},
                "Alanine Aminotransferase": {"value": 30},
                "Alkaline Phosphatase": {"value": 80},
                "Gamma-Glutamyl Transferase": {"value": 25},
                "Bilirubin": {"value": 0.8},
                "Lactate Dehydrogenase": {"value": 200},
                "Prothrombin Time": {"value": 12},
                "Partial Thromboplastin Time": {"value": 30},
                "Fibrinogen": {"value": 300}
            }
        }

        # Try to get the User object; raise an exception if not found
        try:
            user = User.objects.get(id=user_data['id'])
        except ObjectDoesNotExist:
            self.stdout.write(self.style.ERROR(f'User with id {user_data["id"]} not found.'))
            return

        # Caching Biochemical objects
        biochemical_cache = {biochemical.name: biochemical for biochemical in Biochemical.objects.all()}

        for biochemical_name, data in user_data['biometrics'].items():
            # Fetch the Biochemical object
            biochemical = biochemical_cache.get(biochemical_name)
            if not biochemical:
                self.stdout.write(self.style.WARNING(f'Biochemical {biochemical_name} not found in database.'))
                continue
            
            value = data['value']
            # Create or update Biometrics record
            biometrics, created = Biometrics.objects.update_or_create(
                user=user,
                biochemical=biochemical,
                defaults={'value': value}
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Created biometrics record for {user.first_name} - {biochemical.name}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Updated biometrics record for {user.first_name} - {biochemical.name}'))

        self.stdout.write(self.style.SUCCESS('Data has been successfully saved.'))
