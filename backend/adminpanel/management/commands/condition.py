# from django.core.management.base import BaseCommand
# import pandas as pd
# from adminpanel.models import Condition, Biochemical
 

# class Command(BaseCommand):
#     help = 'Adding condtions to db'

#     def handle(self, *args, **kwargs):
#         biochemicals_conditions = {
#                     "Blood Glucose": {
#                         "hypo_conditions": ["Hypoglycemia", "Insulinoma", "Adrenal insufficiency", "Liver disease"],
#                         "hyper_conditions": ["Diabetes mellitus", "Cushing's syndrome", "Pancreatitis", "Stress-induced hyperglycemia"],
#                     },
#                     "Hemoglobin A1c": {
#                         "hypo_conditions": ["Hemolytic anemia", "Blood loss", "Erythropoiesis"],
#                         "hyper_conditions": ["Diabetes mellitus", "Prediabetes", "Chronic kidney disease"],
#                     },
#                     "Glycated Albumin": {
#                         "hypo_conditions": ["Hyperthyroidism", "Nephrotic syndrome", "Liver cirrhosis"],
#                         "hyper_conditions": ["Diabetes mellitus", "Chronic kidney disease"],
#                     },
#                     "Total Cholesterol": {
#                         "hypo_conditions": ["Malnutrition", "Hyperthyroidism", "Liver disease", "Tangier disease"],
#                         "hyper_conditions": ["Familial hypercholesterolemia", "Hypothyroidism", "Nephrotic syndrome", "Cholestasis"],
#                     },
#                     "LDL Cholesterol": {
#                         "hypo_conditions": ["Abetalipoproteinemia", "Malnutrition", "Hyperthyroidism"],
#                         "hyper_conditions": ["Familial hypercholesterolemia", "Hypothyroidism", "Nephrotic syndrome", "Diabetes mellitus"],
#                     },
#                     "HDL Cholesterol": {
#                         "hypo_conditions": ["Metabolic syndrome", "Type 2 diabetes", "Chronic kidney disease", "Tangier disease"],
#                         "hyper_conditions": ["Hyperalphalipoproteinemia","Cardiovascular events","Liver disease"]
#                     },
#                     "Triglycerides": {
#                         "hypo_conditions": ["Malnutrition", "Hyperthyroidism", "Malabsorption syndromes"],
#                         "hyper_conditions": ["Obesity", "Diabetes mellitus", "Hypothyroidism", "Nephrotic syndrome", "Alcoholism"],
#                     },
#                     "Apolipoprotein A1": {
#                         "hypo_conditions": ["Coronary artery disease", "Tangier disease", "Severe liver disease"],
#                         "hyper_conditions": ["Cardiovascular events", "Cancer"]
#                     },
#                     "Apolipoprotein B": {
#                         "hypo_conditions": ["Abetalipoproteinemia", "Hypobetalipoproteinemia"],
#                         "hyper_conditions": ["Familial hypercholesterolemia", "Hypothyroidism", "Nephrotic syndrome"],
#                     },
#                     "Vitamin D": {
#                         "hypo_conditions": ["Rickets", "Osteomalacia", "Osteoporosis", "Autoimmune diseases"],
#                         "hyper_conditions": ["Hypervitaminosis D", "Sarcoidosis", "Hypercalcemia"],
#                     },
#                     "Vitamin C": {
#                         "hypo_conditions": ["Scurvy", "Impaired wound healing", "Weakened immune system"],
#                         "hyper_conditions": ["Kidney stones", "Gastrointestinal disturbances", "Iron overload"],
#                     },
#                     "Vitamin K": {
#                         "hypo_conditions": ["Bleeding disorders", "Osteoporosis", "Bruising easily"],
#                         "hyper_conditions": ["Rare, but can interfere with anticoagulant medications"],
#                     },
#                     "Vitamin B6 (Pyridoxine)": {
#                         "hypo_conditions": ["Anemia", "Depression", "Weakened immune system", "Peripheral neuropathy"],
#                         "hyper_conditions": ["Sensory neuropathy", "Photosensitivity", "Nausea"],
#                     },
#                     "Vitamin B1 (Thiamine)": {
#                         "hypo_conditions": ["Beriberi", "Wernicke-Korsakoff syndrome", "Cardiovascular disease", "Neurological disorders"],
#                         "hyper_conditions": ["Headaches", "Irritability", "Rapid pulse"],
#                     },
#                     "Vitamin B2 (Riboflavin)": {
#                         "hypo_conditions": ["Ariboflavinosis", "Anemia", "Skin disorders", "Mouth sores"],
#                         "hyper_conditions": ["Bright yellow urine", "Diarrhea", "Nausea"]
#                     },
#                     "Vitamin B3 (Niacin)": {
#                         "hypo_conditions": ["Pellagra", "Dermatitis", "Dementia", "Diarrhea"],
#                         "hyper_conditions": ["Skin flushing", "Liver damage", "Glucose intolerance"],
#                     },
#                     "Vitamin B5 (Pantothenic Acid)": {
#                         "hypo_conditions": ["Fatigue", "Insomnia", "Depression", "Numbness in hands and feet"],
#                         "hyper_conditions": ["Diarrhea", "Gastrointestinal disturbances"]
#                     },
#                     "Vitamin B7 (Biotin)": {
#                         "hypo_conditions": ["Hair loss", "Skin rashes", "Brittle nails", "Neurological symptoms"],
#                         "hyper_conditions": ["There are no well-documented cases of toxicity from high doses of biotin."]
#                     },
#                     "Vitamin B9 (Folate)": {
#                         "hypo_conditions": ["Anemia", "Neural tube defects", "Depression", "Cognitive impairment"],
#                         "hyper_conditions": ["Masks Vitamin B12 deficiency", "Can cause gastrointestinal issues in very high doses"]
#                     },
#                     "Vitamin B12 (Cobalamin)": {
#                         "hypo_conditions": ["Pernicious anemia", "Neurological disorders", "Cognitive decline", "Fatigue", "Megaloblastic anemia", "Malabsorption disorders", "Strict vegetarian or vegan diet"],
#                         "hyper_conditions": ["Excess supplementation", "Liver disease", "Myeloproliferative disorders", "Renal cell carcinoma"],
#                     },
#                     "Vitamin A": {
#                         "hypo_conditions": ["Night blindness", "Dry eyes", "Impaired immune function", "Growth retardation"],
#                         "hyper_conditions": ["Hypervitaminosis A", "Liver damage", "Bone abnormalities", "Birth defects"],
#                     },
#                     "Creatinine": {
#                         "hypo_conditions": ["Muscular dystrophy", "Myasthenia gravis", "Low muscle mass"],
#                         "hyper_conditions": ["Chronic kidney disease", "Acute kidney injury", "Dehydration", "Rhabdomyolysis"],
#                     },
#                     "Uric Acid": {
#                         "hypo_conditions": ["Wilson's disease", "Fanconi syndrome"],
#                         "hyper_conditions": ["Gout", "Kidney stones", "Metabolic syndrome", "Lesch-Nyhan syndrome"],
#                     },
#                     "Blood Urea Nitrogen": {
#                         "hypo_conditions": ["Severe liver disease", "Malnutrition", "Overhydration"],
#                         "hyper_conditions": ["Kidney disease", "Dehydration", "High protein diet", "Gastrointestinal bleeding"],
#                     },
#                     "Cystatin C": {
#                         "hypo_conditions": ["Rare, not typically associated with clinical conditions"],
#                         "hyper_conditions": ["Chronic kidney disease", "Acute kidney injury", "Thyroid disorders"],
#                     },
#                     "Sodium": {
#                         "hypo_conditions": ["Hyponatremia", "Addison's disease", "Heart failure"],
#                         "hyper_conditions": ["Hypernatremia", "Dehydration", "Cushing's syndrome", "Diabetes insipidus"],
#                     },
#                     "Potassium": {
#                         "hypo_conditions": ["Hypokalemia", "Cushing's syndrome", "Diuretic use", "Vomiting or diarrhea"],
#                         "hyper_conditions": ["Hyperkalemia", "Kidney failure", "Addison's disease", "Severe tissue damage"],
#                     },
#                     "Calcium": {
#                         "hypo_conditions": ["Hypocalcemia", "Hypoparathyroidism", "Vitamin D deficiency", "Renal failure"],
#                         "hyper_conditions": ["Hypercalcemia", "Hyperparathyroidism", "Certain cancers", "Sarcoidosis"],
#                     },
#                     "Magnesium": {
#                         "hypo_conditions": ["Hypomagnesemia", "Alcoholism", "Malabsorption", "Certain medications"],
#                         "hyper_conditions": ["Hypermagnesemia", "Kidney failure", "Addison's disease", "antacid use"],
#                     },
#                     "Phosphate": {
#                         "hypo_conditions": ["Hypophosphatemia", "Malnutrition", "Alcoholism", "Hyperparathyroidism"],
#                         "hyper_conditions": ["Hyperphosphatemia", "Chronic kidney disease", "Hypoparathyroidism", "Tumor lysis syndrome"],
#                     },
#                     "Chloride": {
#                         "hypo_conditions": ["Hypochloremia", "Vomiting", "Addison's disease", "Metabolic alkalosis"],
#                         "hyper_conditions": ["Hyperchloremia", "Dehydration", "Kidney dysfunction", "Metabolic acidosis"],
#                     },
#                     "Bicarbonate": {
#                         "hypo_conditions": ["Metabolic acidosis", "Diabetic ketoacidosis", "Severe diarrhea", "Renal tubular acidosis"],
#                         "hyper_conditions": ["Metabolic alkalosis", "Vomiting", "Cushing's syndrome"],
#                     },
#                     "Iron": {
#                         "hypo_conditions": ["Iron deficiency anemia", "Chronic blood loss", "Malabsorption", "Pregnancy"],
#                         "hyper_conditions": ["Hemochromatosis", "Hemosiderosis", "Frequent blood transfusions", "Iron supplementation"],
#                     },
#                     "Globulin": {
#                         "hypo_conditions": ["Immunodeficiency disorders", "Malnutrition", "Nephrotic syndrome"],
#                         "hyper_conditions": ["Chronic inflammatory diseases", "Multiple myeloma", "Liver disease", "Autoimmune disorders"],
#                     },
#                     "Albumin": {
#                         "hypo_conditions": ["Malnutrition", "Liver disease", "Nephrotic syndrome", "Inflammatory bowel disease"],
#                         "hyper_conditions": ["Dehydration", "Rare genetic disorders"],
#                     },
#                     "Total Protein": {
#                         "hypo_conditions": ["Malnutrition", "Liver disease", "Malabsorption", "Burns"],
#                         "hyper_conditions": ["Dehydration", "Multiple myeloma", "Chronic inflammatory conditions"],
#                     },
#                     "Albumin/Globulin Ratio": {
#                         "hypo_conditions": ["Liver disease", "Autoimmune disorders", "Chronic infections"],
#                         "hyper_conditions": ["Dehydration", "Some genetic disorders"],
#                     },
#                     "C-Reactive Protein": {
#                         "hypo_conditions": ["Genetic polymorphisms", "Liver failure", "Malnutrition"],
#                         "hyper_conditions": ["Inflammation", "Infections", "Cardiovascular disease", "Autoimmune disorders"],
#                     },
#                     "Haptoglobin": {
#                         "hypo_conditions": ["Hemolytic anemia", "Liver disease", "Malnutrition"],
#                         "hyper_conditions": ["Inflammatory conditions", "Tissue damage", "Certain cancers"],
#                     },
#                     "Transferrin": {
#                         "hypo_conditions": ["Iron overload", "Malnutrition", "Chronic illness"],
#                         "hyper_conditions": ["Iron deficiency anemia", "Pregnancy"],
#                     },
#                     "C-Peptide": {
#                         "hypo_conditions": ["Type 1 diabetes", "Pancreatic disease"],
#                         "hyper_conditions": ["Insulin resistance", "Insulinoma", "Kidney disease"],
#                     },
#                     "Testosterone": {
#                         "hypo_conditions": ["Hypogonadism", "Klinefelter syndrome", "Aging", "Obesity"],
#                         "hyper_conditions": ["Polycystic ovary syndrome", "Congenital adrenal hyperplasia", "Testicular tumors"],
#                     },
#                     "Estrogen": {
#                         "hypo_conditions": ["Menopause", "Turner syndrome", "Anorexia nervosa"],
#                         "hyper_conditions": ["Ovarian tumors", "Cirrhosis", "Obesity"],
#                     },
#                     "Progesterone": {
#                         "hypo_conditions": ["Anovulation", "Menopause", "Luteal phase defect"],
#                         "hyper_conditions": ["Ovarian cysts", "Congenital adrenal hyperplasia", "Some ovarian tumors"],
#                     },
#                     "Cortisol": {
#                         "hypo_conditions": ["Addison's disease", "Pituitary gland disorders", "Congenital adrenal hyperplasia"],
#                         "hyper_conditions": ["Cushing's syndrome", "Chronic stress", "Certain medications"],
#                     },
#                     "Aldosterone": {
#                         "hypo_conditions": ["Addison's disease", "Hypoaldosteronism", "Certain medications"],
#                         "hyper_conditions": ["Conn's syndrome", "Congestive heart failure", "Cirrhosis"],
#                     },
#                     "Thyroid-Stimulating Hormone (TSH)": {
#                         "hypo_conditions": ["Hyperthyroidism", "Pituitary dysfunction"],
#                         "hyper_conditions": ["Hypothyroidism", "Thyroid hormone resistance"],
#                     },
#                     "Free Thyroxine (Free T4)": {
#                         "hypo_conditions": ["Hypothyroidism", "Iodine deficiency"],
#                         "hyper_conditions": ["Hyperthyroidism", "Thyroiditis"],
#                     },
#                     "Free Triiodothyronine (Free T3)": {
#                         "hypo_conditions": ["Hypothyroidism", "Euthyroid sick syndrome"],
#                         "hyper_conditions": ["Hyperthyroidism", "T3 toxicosis"],
#                     },
#                     "Aspartate Aminotransferase": {
#                         "hypo_conditions": ["Vitamin B6 deficiency", "Uremia", "Chronic dialysis"],
#                         "hyper_conditions": ["Liver disease", "Muscle damage", "Heart attack", "Certain medications"],
#                     },
#                     "Alanine Aminotransferase": {
#                         "hypo_conditions": ["Vitamin B6 deficiency", "Chronic kidney disease"],
#                         "hyper_conditions": ["Liver disease", "Hepatitis", "Fatty liver", "Certain medications"],
#                     },
#                     "Alkaline Phosphatase": {
#                         "hypo_conditions": ["Hypophosphatasia", "Zinc deficiency", "Malnutrition"],
#                         "hyper_conditions": ["Liver disease", "Bone disorders", "Pregnancy", "Certain cancers"],
#                     },
#                     "Gamma-Glutamyl Transferase": {
#                         "hypo_conditions": ["Hypothyroidism", "Congenital deficiency"],
#                         "hyper_conditions": ["Liver disease", "Alcohol abuse", "Pancreatic disease", "Certain medications"],
#                     },
#                     "Bilirubin": {
#                         "hypo_conditions": ["Caffeine consumption", "Certain medications", "Oxidative stress"],
#                         "hyper_conditions": ["Jaundice", "Liver disease", "Hemolytic anemia", "Gilbert's syndrome"],
#                     },
#                     "Lactate Dehydrogenase": {
#                         "hypo_conditions": ["LDH deficiency","Genetic disorder", "Severe liver disease"],
#                         "hyper_conditions": ["Tissue damage", "Hemolysis", "Certain cancers", "Heart attack"],
#                     },
#                     "Prothrombin Time": {
#                         "hypo_conditions": ["Hypercoagulable states", "Thrombophilia"],
#                         "hyper_conditions": ["Liver disease", "Vitamin K deficiency", "Anticoagulant therapy"],
#                     },
#                     "Partial Thromboplastin Time": {
#                         "hypo_conditions": ["Hypercoagulable states", "Increased clotting factor levels"],
#                         "hyper_conditions": ["Hemophilia", "Von Willebrand disease", "Liver disease", "Heparin therapy"],
#                     },
#                     "Fibrinogen": {
#                         "hypo_conditions": ["Disseminated intravascular coagulation", "Severe liver disease"],
#                         "hyper_conditions": ["Inflammation", "Pregnancy", "Certain cancers"],
#                     },
#                 }
        
#         condition_cache = {condition.name: condition for condition in Condition.objects.all()}
            
#         for biochemical_name, conditions in biochemicals_conditions.items():
#                 # Retrieve or create the Biochemical object
#                 biochemical, created = Biochemical.objects.get_or_create(name=biochemical_name)
                
#                 # Retrieve conditions
#                 hypo_conditions = [condition_cache.get(condition_name) for condition_name in conditions["hypo_conditions"]]
#                 hyper_conditions = [condition_cache.get(condition_name) for condition_name in conditions["hyper_conditions"]]

#                 # Update conditions for the Biochemical object
#                 biochemical.hypo_conditions.set(filter(None, hypo_conditions))
#                 biochemical.hyper_conditions.set(filter(None, hyper_conditions))
                
#                 # Save changes
#                 biochemical.save()

#                 # Report status
#                 if created:
#                     self.stdout.write(self.style.SUCCESS(f'Created new biochemical: {biochemical_name}'))
#                 else:
#                     self.stdout.write(self.style.SUCCESS(f'Updated biochemical: {biochemical_name}'))

#         self.stdout.write(self.style.SUCCESS('Finished updating biochemicals and their conditions.'))
                

        
