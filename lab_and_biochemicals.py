import uuid

biochemicals = {
    "Blood Glucose": {
        "id": uuid.uuid4(),
        "category": "Carbohydrates",
    },
    "Hemoglobin A1c": {
        "id": uuid.uuid4(),
        "category": "Carbohydrates",
    },
    "Glycated Albumin": {
        "id": uuid.uuid4(),
        "category": "Carbohydrates",
    },
    "Total Cholesterol": {
        "id": uuid.uuid4(),
        "category": "Lipids",
    },
    "LDL Cholesterol": {
        "id": uuid.uuid4(),
        "category": "Lipids",
    },
    "HDL Cholesterol": {
        "id": uuid.uuid4(),
        "category": "Lipids",
    },
    "Triglycerides": {
        "id": uuid.uuid4(),
        "category": "Lipids",
    },
    "Apolipoprotein A1": {
        "id": uuid.uuid4(),
        "category": "Lipids",
    },
    "Apolipoprotein B": {
        "id": uuid.uuid4(),
        "category": "Lipids",
    },
    "Vitamin D": {
        "id": uuid.uuid4(),
        "category": "Vitamins",
    },
    "Vitamin C": {
        "id": uuid.uuid4(),
        "category": "Vitamins",
    },
    "Vitamin K": {
        "id": uuid.uuid4(),
        "category": "Vitamins",
    },
    "Vitamin B6 (Pyridoxine)": {
        "id": uuid.uuid4(),
        "category": "Vitamins",
    },
    "Vitamin B1 (Thiamine)": {
        "id": uuid.uuid4(),
        "category": "Vitamins",
    },
    "Vitamin B2 (Riboflavin)": {
        "id": uuid.uuid4(),
        "category": "Vitamins",
    },
    "Vitamin B3 (Niacin)": {
        "id": uuid.uuid4(),
        "category": "Vitamins",
    },
    "Vitamin B5 (Pantothenic Acid)": {
        "id": uuid.uuid4(),
        "category": "Vitamins",
    },
    "Vitamin B7 (Biotin)": {
        "id": uuid.uuid4(),
        "category": "Vitamins",
    },
    "Vitamin B9 (Folate)": {
        "id": uuid.uuid4(),
        "category": "Vitamins",
    },
    "Vitamin B12 (Cobalamin)": {
        "id": uuid.uuid4(),
        "category": "Vitamins",
    },
    "Vitamin A": {
        "id": uuid.uuid4(),
        "category": "Vitamins",
    },
    "Creatinine": {
        "id": uuid.uuid4(),
        "category": "Kidney Function",
    },
    "Uric Acid": {
        "id": uuid.uuid4(),
        "category": "Kidney Function",
    },
    "Blood Urea Nitrogen": {
        "id": uuid.uuid4(),
        "category": "Kidney Function",
    },
    "Cystatin C": {
        "id": uuid.uuid4(),
        "category": "Kidney Function",
    },
    "Sodium": {
        "id": uuid.uuid4(),
        "category": "Minerals",
    },
    "Potassium": {
        "id": uuid.uuid4(),
        "category": "Minerals",
    },
    "Calcium": {
        "id": uuid.uuid4(),
        "category": "Minerals",
    },
    "Magnesium": {
        "id": uuid.uuid4(),
        "category": "Minerals",
    },
    "Phosphate": {
        "id": uuid.uuid4(),
        "category": "Minerals",
    },
    "Chloride": {
        "id": uuid.uuid4(),
        "category": "Minerals",
    },
    "Bicarbonate": {
        "id": uuid.uuid4(),
        "category": "Minerals",
    },
    "Iron": {
        "id": uuid.uuid4(),
        "category": "Minerals",
    },
    "Globulin": {
        "id": uuid.uuid4(),
        "category": "Proteins",
    },
    "Albumin": {
        "id": uuid.uuid4(),
        "category": "Proteins",
    },
    "Total Protein": {
        "id": uuid.uuid4(),
        "category": "Proteins",
    },
    "Albumin/Globulin Ratio": {
        "id": uuid.uuid4(),
        "category": "Proteins",
    },
    "C-Reactive Protein": {
        "id": uuid.uuid4(),
        "category": "Proteins",
    },
    "Haptoglobin": {
        "id": uuid.uuid4(),
        "category": "Proteins",
    },
    "Transferrin": {
        "id": uuid.uuid4(),
        "category": "Proteins",
    },
    "C-Peptide": {
        "id": uuid.uuid4(),
        "category": "Hormones",
    },
    "Testosterone": {
        "id": uuid.uuid4(),
        "category": "Hormones",
    },
    "Estrogen": {
        "id": uuid.uuid4(),
        "category": "Hormones",
    },
    "Progesterone": {
        "id": uuid.uuid4(),
        "category": "Hormones",
    },
    "Cortisol": {
        "id": uuid.uuid4(),
        "category": "Hormones",
    },
    "Aldosterone": {
        "id": uuid.uuid4(),
        "category": "Hormones",
    },
    "Thyroid-Stimulating Hormone (TSH)": {
        "id": uuid.uuid4(),
        "category": "Hormones",
    },
    "Free Thyroxine (Free T4)": {
        "id": uuid.uuid4(),
        "category": "Hormones",
    },
    "Free Triiodothyronine (Free T3)": {
        "id": uuid.uuid4(),
        "category": "Hormones",
    },
    "Aspartate Aminotransferase": {
        "id": uuid.uuid4(),
        "category": "Liver Function",
    },
    "Alanine Aminotransferase": {
        "id": uuid.uuid4(),
        "category": "Liver Function",
    },
    "Alkaline Phosphatase": {
        "id": uuid.uuid4(),
        "category": "Liver Function",
    },
    "Gamma-Glutamyl Transferase": {
        "id": uuid.uuid4(),
        "category": "Liver Function",
    },
    "Bilirubin": {
        "id": uuid.uuid4(),
        "category": "Liver Function",
    },
    "Lactate Dehydrogenase": {
        "id": uuid.uuid4(),
        "category": "Liver Function",
    },
    "Prothrombin Time": {
        "id": uuid.uuid4(),
        "category": "Coagulation",
    },
    "Partial Thromboplastin Time": {
        "id": uuid.uuid4(),
        "category": "Coagulation",
    },
    "Fibrinogen": {
        "id": uuid.uuid4(),
        "category": "Coagulation",
    },
}

biochemicals_units = {
    "Blood Glucose": {
      "unit": "mg/dL",
      "healthy_range_female": [70, 100],
      "healthy_range_male": [70, 100],
    },
    "Hemoglobin A1c": {
      "unit": "%",
      "healthy_range_female": [4.0, 5.6],
      "healthy_range_male": [4.0, 5.6],
    },
    "Glycated Albumin": {
      "unit": "%",
      "healthy_range_female": [11, 16],
      "healthy_range_male": [11, 16],
    },
    "Total Cholesterol": {
      "unit": "mg/dL",
      "healthy_range_female": [125, 200],
      "healthy_range_male": [125, 200],
    },
    "LDL Cholesterol": {
      "unit": "mg/dL",
      "healthy_range_female": [50, 150],
      "healthy_range_male": [50, 150],
    },
    "HDL Cholesterol": {
      "unit": "mg/dL",
      "healthy_range_female": [50, 100],
      "healthy_range_male": [40, 60],
    },
    "Triglycerides": {
      "unit": "mg/dL",
      "healthy_range_female": [40, 190],
      "healthy_range_male": [40, 190],
    },
    "Apolipoprotein A1": {
      "unit": "mg/dL",
      "healthy_range_female": [115, 220],
      "healthy_range_male": [110, 205],
    },
    "Apolipoprotein B": {
      "unit": "mg/dL",
      "healthy_range_female": [55, 130],
      "healthy_range_male": [55, 140],
    },
    "Vitamin D": {
      "unit": "ng/mL",
      "healthy_range_female": [20, 50],
      "healthy_range_male": [20, 50],
    },
    "Vitamin C": {
      "unit": "mg/L",
      "healthy_range_female": [4, 20],
      "healthy_range_male": [4, 20],
    },
    "Vitamin K": {
      "unit": "ng/mL",
      "healthy_range_female": [0.2, 3.2],
      "healthy_range_male": [0.2, 3.2],
    },
    "Vitamin B6 (Pyridoxine)": {
      "unit": "ng/mL",
      "healthy_range_female": [5, 50],
      "healthy_range_male": [5, 50],
    },
    "Vitamin B1 (Thiamine)": {
      "unit": "nmol/L",
      "healthy_range_female": [70, 180],
      "healthy_range_male": [70, 180],
    },
    "Vitamin B2 (Riboflavin)": {
      "unit": "nmol/L",
      "healthy_range_female": [6.2, 39],
      "healthy_range_male": [6.2, 39],
    },
    "Vitamin B3 (Niacin)": {
      "unit": "µg/L",
      "healthy_range_female": [5, 50],
      "healthy_range_male": [5, 50],
    },
    "Vitamin B5 (Pantothenic Acid)": {
      "unit": "µg/L",
      "healthy_range_female": [100, 1000],
      "healthy_range_male": [100, 1000],
    },
    "Vitamin B7 (Biotin)": {
      "unit": "ng/L",
      "healthy_range_female": [200, 1000],
      "healthy_range_male": [200, 1000],
    },
    "Vitamin B9 (Folate)": {
      "unit": "ng/mL",
      "healthy_range_female": [2.7, 17],
      "healthy_range_male": [2.7, 17],
    },
    "Vitamin B12 (Cobalamin)": {
      "unit": "pg/mL",
      "healthy_range_female": [200, 900],
      "healthy_range_male": [200, 900],
    },
    "Vitamin A": {
      "unit": "µg/dL",
      "healthy_range_female": [30, 65],
      "healthy_range_male": [30, 65],
    },
    "Creatinine": {
      "unit": "mg/dL",
      "healthy_range_female": [0.5, 1.1],
      "healthy_range_male": [0.7, 1.3],
    },
    "Uric Acid": {
      "unit": "mg/dL",
      "healthy_range_female": [2.4, 6.0],
      "healthy_range_male": [3.4, 7.0],
    },
    "Blood Urea Nitrogen": {
      "unit": "mg/dL",
      "healthy_range_female": [7, 20],
      "healthy_range_male": [8, 24],
    },
    "Cystatin C": {
      "unit": "mg/L",
      "healthy_range_female": [0.51, 0.98],
      "healthy_range_male": [0.67, 1.15],
    },
    "Sodium": {
      "unit": "mEq/L",
      "healthy_range_female": [135, 145],
      "healthy_range_male": [135, 145],
    },
    "Potassium": {
      "unit": "mEq/L",
      "healthy_range_female": [3.5, 5.0],
      "healthy_range_male": [3.5, 5.0],
    },
    "Calcium": {
      "unit": "mg/dL",
      "healthy_range_female": [8.5, 10.5],
      "healthy_range_male": [8.5, 10.5],
    },
    "Magnesium": {
      "unit": "mg/dL",
      "healthy_range_female": [1.7, 2.2],
      "healthy_range_male": [1.7, 2.2],
    },
    "Phosphate": {
      "unit": "mg/dL",
      "healthy_range_female": [2.5, 4.5],
      "healthy_range_male": [2.5, 4.5],
    },
    "Chloride": {
      "unit": "mEq/L",
      "healthy_range_female": [98, 107],
      "healthy_range_male": [98, 107],
    },
    "Bicarbonate": {
      "unit": "mEq/L",
      "healthy_range_female": [23, 29],
      "healthy_range_male": [23, 29],
    },
    "Iron": {
      "unit": "µg/dL",
      "healthy_range_female": [50, 170],
      "healthy_range_male": [65, 175],
    },
    "Globulin": {
      "unit": "g/dL",
      "healthy_range_female": [2.0, 3.5],
      "healthy_range_male": [2.0, 3.5],
    },
    "Albumin": {
      "unit": "g/dL",
      "healthy_range_female": [3.5, 5.0],
      "healthy_range_male": [3.5, 5.0],
    },
    "Total Protein": {
      "unit": "g/dL",
      "healthy_range_female": [6.0, 8.3],
      "healthy_range_male": [6.0, 8.3],
    },
    "Albumin/Globulin Ratio": {
      "unit": "ratio",
      "healthy_range_female": [1.2, 2.2],
      "healthy_range_male": [1.2, 2.2],
    },
    "C-Reactive Protein": {
      "unit": "mg/L",
      "healthy_range_female": [0, 3],
      "healthy_range_male": [0, 3],
    },
    "Haptoglobin": {
      "unit": "mg/dL",
      "healthy_range_female": [30, 200],
      "healthy_range_male": [30, 200],
    },
    "Transferrin": {
      "unit": "mg/dL",
      "healthy_range_female": [200, 360],
      "healthy_range_male": [200, 360],
    },
    "C-Peptide": {
      "unit": "ng/mL",
      "healthy_range_female": [0.8, 3.9],
      "healthy_range_male": [0.8, 3.9],
    },
    "Testosterone": {
      "unit": "ng/dL",
      "healthy_range_female": [15, 70],
      "healthy_range_male": [280, 1100],
    },
    "Estrogen": {
      "unit": "pg/mL",
      "healthy_range_female": [15, 350],
      "healthy_range_male": [10, 40],
    },
    "Progesterone": {
      "unit": "ng/mL",
      "healthy_range_female": [0.1, 25],
      "healthy_range_male": [0.1, 0.5],
    },
    "Cortisol": {
      "unit": "µg/dL",
      "healthy_range_female": [6, 23],
      "healthy_range_male": [6, 23],
    },
    "Aldosterone": {
      "unit": "ng/dL",
      "healthy_range_female": [3, 16],
      "healthy_range_male": [3, 16],
    },
    "Thyroid-Stimulating Hormone (TSH)": {
      "unit": "mIU/L",
      "healthy_range_female": [0.4, 4.0],
      "healthy_range_male": [0.4, 4.0],
    },
    "Free Thyroxine (Free T4)": {
      "unit": "ng/dL",
      "healthy_range_female": [0.7, 1.9],
      "healthy_range_male": [0.7, 1.9],
    },
    "Free Triiodothyronine (Free T3)": {
      "unit": "pg/mL",
      "healthy_range_female": [2.3, 4.2],
      "healthy_range_male": [2.3, 4.2],
    },
    "Aspartate Aminotransferase": {
      "unit": "U/L",
      "healthy_range_female": [10, 35],
      "healthy_range_male": [10, 40],
    },
    "Alanine Aminotransferase": {
      "unit": "U/L",
      "healthy_range_female": [7, 35],
      "healthy_range_male": [7, 56],
    },
    "Alkaline Phosphatase": {
      "unit": "U/L",
      "healthy_range_female": [35, 104],
      "healthy_range_male": [40, 129],
    },
    "Gamma-Glutamyl Transferase": {
      "unit": "U/L",
      "healthy_range_female": [5, 36],
      "healthy_range_male": [8, 61],
    },
    "Bilirubin": {
      "unit": "mg/dL",
      "healthy_range_female": [0.2, 1.2],
      "healthy_range_male": [0.2, 1.2],
    },
    "Lactate Dehydrogenase": {
      "unit": "U/L",
      "healthy_range_female": [140, 280],
      "healthy_range_male": [140, 280],
    },
    "Prothrombin Time": {
      "unit": "seconds",
      "healthy_range_female": [11, 13.5],
      "healthy_range_male": [11, 13.5],
    },
    "Partial Thromboplastin Time": {
      "unit": "seconds",
      "healthy_range_female": [25, 35],
      "healthy_range_male": [25, 35],
    },
    "Fibrinogen": {
      "unit": "mg/dL",
      "healthy_range_female": [200, 400],
      "healthy_range_male": [200, 400],
    },
}

biochemicals_nutrients = {
    "Blood Glucose": {
      "increasing_nutrients": ["Carbohydrates", "Sucrose", "Glucose", "Fructose"],
      "decreasing_nutrients": ["Fiber", "Magnesium", "Antioxidants", "Omega-3 Fatty Acids", "Polyphenols", "Probiotics"]
    },
    "Hemoglobin A1c": {
      "increasing_nutrients": ["Carbohydrates", "Sucrose", "Glucose", "Fructose"],
      "decreasing_nutrients": ["Fiber", "Magnesium", "Antioxidants", "Omega-3 Fatty Acids", "Polyphenols", "Probiotics"]
    },
    "Glycated Albumin": {
      "increasing_nutrients": ["Carbohydrates", "Sucrose", "Glucose", "Fructose"],
      "decreasing_nutrients": ["Fiber", "Magnesium", "Antioxidants", "Omega-3 Fatty Acids", "Polyphenols", "Probiotics"]
    },
    "Total Cholesterol": {
      "increasing_nutrients": ["Saturated Fatty Acids", "Trans Fatty Acids", "Cholesterol"],
      "decreasing_nutrients": ["Fiber", "Omega-3 Fatty Acids", "Monounsaturated Fatty Acids", "Polyunsaturated Fatty Acids", "Phytosterols", "Antioxidants"]
    },
    "LDL Cholesterol": {
      "increasing_nutrients": ["Saturated Fatty Acids", "Trans Fatty Acids", "Cholesterol"],
      "decreasing_nutrients": ["Fiber", "Omega-3 Fatty Acids", "Monounsaturated Fatty Acids", "Polyunsaturated Fatty Acids", "Phytosterols", "Antioxidants"]
    },
    "HDL Cholesterol": {
      "increasing_nutrients": ["Monounsaturated Fatty Acids", "Polyunsaturated Fatty Acids", "Omega-3 Fatty Acids"],
      "decreasing_nutrients": ["Trans Fatty Acids"]
    },
    "Triglycerides": {
      "increasing_nutrients": ["Carbohydrates", "Sucrose", "Glucose", "Fructose", "Alcohol", "Saturated Fatty Acids", "Trans Fatty Acids"],
      "decreasing_nutrients": ["Fiber", "Omega-3 Fatty Acids", "Monounsaturated Fatty Acids", "Polyunsaturated Fatty Acids", "Antioxidants"]
    },
    "Apolipoprotein A1": {
      "increasing_nutrients": ["Monounsaturated Fatty Acids", "Polyunsaturated Fatty Acids", "Omega-3 Fatty Acids"],
      "decreasing_nutrients": ["Trans Fatty Acids"]
    },
    "Apolipoprotein B": {
      "increasing_nutrients": ["Saturated Fatty Acids", "Trans Fatty Acids", "Cholesterol"],
      "decreasing_nutrients": ["Fiber", "Omega-3 Fatty Acids", "Monounsaturated Fatty Acids", "Polyunsaturated Fatty Acids", "Antioxidants"]
    },
    "Vitamin D": {
      "increasing_nutrients": ["Calcium", "Phosphorus", "Vitamin K", "Magnesium"],
      "decreasing_nutrients": ["Phytic Acid", "Oxalates", "Fiber"]
    },
    "Vitamin C": {
      "increasing_nutrients": ["Flavonoids", "Polyphenols", "Iron"],
      "decreasing_nutrients": ["Alcohol", "Caffeine", "Tannins", "Copper", "Sodium"]
    },
    "Vitamin K": {
      "increasing_nutrients": ["Vitamin D", "Calcium", "Magnesium"],
      "decreasing_nutrients": ["Vitamin E", "Omega-3 Fatty Acids", "Omega-6 Fatty Acids"]
    },
    "Vitamin B6 (Pyridoxine)": {
      "increasing_nutrients": ["Magnesium", "Zinc", "Vitamin B2"],
      "decreasing_nutrients": ["Alcohol", "Proteins"]
    },
    "Vitamin B1 (Thiamine)": {
      "increasing_nutrients": ["Magnesium", "Vitamin C"],
      "decreasing_nutrients": ["Alcohol", "Tannins"]
    },
    "Vitamin B2 (Riboflavin)": {
      "increasing_nutrients": ["Magnesium", "Vitamin B6"],
      "decreasing_nutrients": ["Alcohol", "Caffeine"]
    },
    "Vitamin B3 (Niacin)": {
      "increasing_nutrients": ["Tryptophan", "Vitamin B6", "Iron"],
      "decreasing_nutrients": ["Alcohol", "Carbohydrates"]
    },
    "Vitamin B5  (Pantothenic Acid)": {
      "increasing_nutrients": ["Vitamin B7"],
      "decreasing_nutrients": ["Alcohol", "Caffeine"]
    },
    "Vitamin B7 (Biotin)": {
      "increasing_nutrients": ["Magnesium", "Vitamin B5"],
      "decreasing_nutrients": ["Alcohol"]
    },
    "Vitamin B9 (Folate)": {
      "increasing_nutrients": ["Vitamin B12", "Vitamin C"],
      "decreasing_nutrients": ["Alcohol", "Zinc"]
    },
    "Vitamin B12 (Cobalamin)": {
      "increasing_nutrients": ["Calcium", "Vitamin B9"],
      "decreasing_nutrients": ["Alcohol", "Vitamin C"]
    },
    "Vitamin A": {
      "increasing_nutrients": ["Carotenoids", "Zinc", "Vitamin E"],
      "decreasing_nutrients": ["Alcohol", "Fiber", "Iron"]
    },
    "Creatinine": {
      "increasing_nutrients": ["Proteins", "Alanine", "Arginine", "Aspartic Acid", "Glutamic Acid", "Glycine", "Histidine", "Isoleucine", "Leucine", "Lysine", "Methionine", "Phenylalanine", "Serine", "Threonine", "Valine"],
      "decreasing_nutrients": []
    },
    "Uric Acid": {
      "increasing_nutrients": ["Proteins", "Alanine", "Arginine", "Aspartic Acid", "Cysteine", "Glutamic Acid", "Glycine", "Histidine", "Isoleucine", "Leucine", "Lysine", "Methionine", "Phenylalanine", "Serine", "Threonine", "Valine", "Fructose"],
      "decreasing_nutrients": ["Vitamin C", "Fiber", "Antioxidants"]
    },
    "Blood Urea Nitrogen": {
      "increasing_nutrients": ["Proteins", "Alanine", "Arginine", "Aspartic Acid", "Glutamic Acid", "Glycine", "Histidine", "Isoleucine", "Leucine", "Lysine", "Methionine", "Phenylalanine", "Serine", "Threonine", "Valine", "Sodium"],
      "decreasing_nutrients": ["Water"]
    },
    "Cystatin C": {
      "increasing_nutrients": [],
      "decreasing_nutrients": ["Vitamin D"]
    },
    "Sodium": {
      "increasing_nutrients": ["Sodium"],
      "decreasing_nutrients": ["Water", "Potassium", "Fiber", "Calcium", "Magnesium", "Vitamin D"]
    },
    "Potassium": {
      "increasing_nutrients": ["Potassium"],
      "decreasing_nutrients": ["Sodium"]
    },
    "Calcium": {
      "increasing_nutrients": ["Calcium", "Vitamin D", "Vitamin K", "Phosphorus"],
      "decreasing_nutrients": ["Phytic Acid", "Oxalates", "Sodium", "Caffeine"]
    },
    "Magnesium": {
      "increasing_nutrients": ["Magnesium", "Vitamin D"],
      "decreasing_nutrients": ["Calcium", "Phytic Acid", "Oxalates"]
    },
    "Phosphate": {
      "increasing_nutrients": ["Phosphorus"],
      "decreasing_nutrients": ["Calcium"]
    },
    "Chloride": {
      "increasing_nutrients": ["Sodium"],
      "decreasing_nutrients": ["Water", "Potassium"]
    },
    "Bicarbonate": {
      "increasing_nutrients": ["Sodium", "Potassium"],
      "decreasing_nutrients": []
    },
    "Iron": {
      "increasing_nutrients": ["Iron", "Vitamin C", "Proteins", "Copper"],
      "decreasing_nutrients": ["Calcium", "Phytic Acid", "Oxalates", "Tannins"]
    },
    "Globulin": {
      "increasing_nutrients": ["Proteins", "Vitamin C", "Vitamin B6", "Vitamin B12", "Iron", "Zinc", "Copper", "Magnesium"],
      "decreasing_nutrients": ["Alcohol", "Caffeine", "Oxalates", "Phytic Acid", "Tannins"]
    },
    "Albumin": {
      "increasing_nutrients": ["Proteins", "Vitamin B6", "Vitamin B12", "Zinc", "Copper", "Magnesium", "Iron"],
      "decreasing_nutrients": ["Alcohol", "Caffeine", "Oxalates", "Phytic Acid", "Tannins"]
    },
    "Total Protein": {
      "increasing_nutrients": ["Proteins", "Vitamin B6", "Vitamin B12", "Iron", "Zinc", "Copper", "Magnesium", "Vitamin C"],
      "decreasing_nutrients": ["Alcohol", "Caffeine", "Oxalates", "Phytic Acid", "Tannins"]
    },
    "Albumin/Globulin Ratio": {
      "increasing_nutrients": ["Proteins", "Vitamin B6", "Vitamin B12", "Zinc", "Copper", "Magnesium", "Iron"],
      "decreasing_nutrients": ["Alcohol", "Caffeine", "Oxalates", "Phytic Acid", "Tannins"]
    },
    "C-Reactive Protein": {
      "increasing_nutrients": ["Alcohol", "Caffeine", "Trans Fatty Acids", "Oxalates", "Phytic Acid"],
      "decreasing_nutrients": ["Vitamin C", "Omega-3 Fatty Acids", "Fiber", "Antioxidants", "Flavonoids", "Polyphenols", "Probiotics", "Prebiotics"]
    },
    "Haptoglobin": {
      "increasing_nutrients": ["Proteins", "Vitamin C", "Vitamin B6", "Iron", "Zinc", "Copper"],
      "decreasing_nutrients": ["Alcohol", "Caffeine", "Oxalates", "Phytic Acid"]
    },
    "Transferrin": {
      "increasing_nutrients": ["Proteins", "Vitamin C", "Iron", "Vitamin B12", "Copper", "Zinc"],
      "decreasing_nutrients": ["Alcohol", "Caffeine", "Oxalates", "Phytic Acid", "Tannins"]
    },
    "C-Peptide": {
      "increasing_nutrients": ["Proteins", "Vitamin B12", "Magnesium", "Vitamin C", "Zinc"],
      "decreasing_nutrients": ["Alcohol", "Caffeine", "Oxalates", "Phytic Acid"]
    },
    "Testosterone": {
      "increasing_nutrients": ["Zinc", "Vitamin D", "Magnesium", "Vitamin B6", "Omega-3 Fatty Acids", "Vitamin B12", "Saturated Fatty Acids", "Monounsaturated Fatty Acids", "Vitamin C", "Copper", "Proteins"],
      "decreasing_nutrients": ["Alcohol", "Trans Fatty Acids", "Sodium", "Phytic Acid", "Oxalates", "Lectins"]
    },
    "Estrogen": {
      "increasing_nutrients": ["Vitamin B6", "Vitamin C", "Omega-3 Fatty Acids", "Vitamin E", "Flavonoids", "Carotenoids", "Magnesium", "Proteins"],
      "decreasing_nutrients": ["Alcohol", "Trans Fatty Acids", "Caffeine", "Sodium", "Oxalates", "Phytic Acid"]
    },
    "Progesterone": {
      "increasing_nutrients": ["Vitamin B6", "Vitamin C", "Magnesium", "Zinc", "Omega-3 Fatty Acids", "Proteins", "Vitamin E"],
      "decreasing_nutrients": ["Alcohol", "Caffeine", "Sodium", "Trans Fatty Acids", "Phytic Acid", "Oxalates"]
    },
    "Cortisol": {
      "increasing_nutrients": ["Vitamin C", "Magnesium", "Omega-3 Fatty Acids", "Vitamin B5", "Probiotics", "Proteins"],
      "decreasing_nutrients": ["Alcohol", "Caffeine", "Sodium", "Trans Fatty Acids", "Oxalates"]
    },
    "Aldosterone": {
      "increasing_nutrients": ["Potassium", "Magnesium", "Vitamin D", "Omega-3 Fatty Acids", "Proteins"],
      "decreasing_nutrients": ["Sodium", "Trans Fatty Acids", "Alcohol", "Phytic Acid", "Oxalates"]
    },
    "Thyroid-Stimulating Hormone (TSH)": {
      "increasing_nutrients": ["Iodine", "Selenium", "Zinc", "Vitamin B12", "Vitamin D", "Proteins", "Magnesium"],
      "decreasing_nutrients": ["Sodium", "Alcohol", "Oxalates", "Phytic Acid"]
    },
    "Free Thyroxine (Free T4)": {
      "increasing_nutrients": ["Iodine", "Selenium", "Zinc", "Vitamin B12", "Vitamin D", "Proteins", "Magnesium"],
      "decreasing_nutrients": ["Sodium", "Alcohol", "Oxalates", "Phytic Acid"]
    },
    "Free Triiodothyronine (Free T3)": {
      "increasing_nutrients": ["Iodine", "Selenium", "Zinc", "Vitamin B12", "Vitamin D", "Proteins", "Magnesium"],
      "decreasing_nutrients": ["Sodium", "Alcohol", "Oxalates", "Phytic Acid"]
    },    
    "Aspartate Aminotransferase": {
      "increasing_nutrients": ["Carbohydrates", "Proteins", "Fats", "Vitamin B6", "Vitamin B12", "Magnesium", "Iron"],
      "decreasing_nutrients": ["Vitamin B1", "Vitamin B2", "Vitamin B3", "Vitamin B5", "Vitamin B7", "Vitamin B9", "Vitamin C", "Calcium", "Phosphorus"]
    },
    "Alanine Aminotransferase": {
      "increasing_nutrients": ["Proteins", "Fats", "Vitamin B6", "Vitamin B12", "Magnesium", "Iron"],
      "decreasing_nutrients": ["Vitamin B1", "Vitamin B2", "Vitamin B3", "Vitamin B5", "Vitamin B7", "Vitamin B9", "Vitamin C", "Calcium", "Phosphorus"]
    },
    "Alkaline Phosphatase": {
      "increasing_nutrients": ["Vitamin D", "Calcium", "Magnesium", "Phosphorus", "Vitamin K", "Proteins", "Fats"],
      "decreasing_nutrients": ["Sodium"]
    },
    "Gamma-Glutamyl Transferase": {
      "increasing_nutrients": ["Alcohol", "Caffeine", "Theobromine", "Vitamin B6", "Vitamin B12", "Fats", "Proteins"],
      "decreasing_nutrients": ["Vitamin C", "Magnesium"]
    },
    "Bilirubin": {
      "increasing_nutrients": ["Vitamin B12", "Iron", "Proteins", "Fats", "Magnesium"],
      "decreasing_nutrients": ["Vitamin C", "Calcium", "Phosphorus"]
    },
    "Lactate Dehydrogenase": {
      "increasing_nutrients": ["Carbohydrates", "Proteins", "Fats", "Vitamin B6", "Magnesium", "Iron", "Vitamin B12"],
      "decreasing_nutrients": ["Vitamin C"]
    },
    "Prothrombin Time": {
      "increasing_nutrients": ["Vitamin K", "Calcium", "Proteins", "Fats", "Phosphorus"],
      "decreasing_nutrients": ["Vitamin C", "Magnesium"]
    },
    "Partial Thromboplastin Time": {
      "increasing_nutrients": ["Vitamin K", "Calcium", "Phosphorus", "Proteins", "Fats"],
      "decreasing_nutrients": ["Vitamin C", "Sodium"]
    },
    "Fibrinogen": {
      "increasing_nutrients": ["Vitamin K", "Calcium", "Phosphorus", "Proteins", "Fats", "Iron"],
      "decreasing_nutrients": ["Vitamin C", "Magnesium"]
    }

}

biochemicals_conditions = {
    "Blood Glucose": {
        "hypo_conditions": ["Hypoglycemia", "Insulinoma", "Adrenal insufficiency", "Liver disease"],
        "hyper_conditions": ["Diabetes mellitus", "Cushing's syndrome", "Pancreatitis", "Stress-induced hyperglycemia"],
    },
    "Hemoglobin A1c": {
        "hypo_conditions": ["Hemolytic anemia", "Blood loss", "Erythropoiesis"],
        "hyper_conditions": ["Diabetes mellitus", "Prediabetes", "Chronic kidney disease"],
    },
    "Glycated Albumin": {
        "hypo_conditions": ["Hyperthyroidism", "Nephrotic syndrome", "Liver cirrhosis"],
        "hyper_conditions": ["Diabetes mellitus", "Chronic kidney disease"],
    },
    "Total Cholesterol": {
        "hypo_conditions": ["Malnutrition", "Hyperthyroidism", "Liver disease", "Tangier disease"],
        "hyper_conditions": ["Familial hypercholesterolemia", "Hypothyroidism", "Nephrotic syndrome", "Cholestasis"],
    },
    "LDL Cholesterol": {
        "hypo_conditions": ["Abetalipoproteinemia", "Malnutrition", "Hyperthyroidism"],
        "hyper_conditions": ["Familial hypercholesterolemia", "Hypothyroidism", "Nephrotic syndrome", "Diabetes mellitus"],
    },
    "HDL Cholesterol": {
        "hypo_conditions": ["Metabolic syndrome", "Type 2 diabetes", "Chronic kidney disease", "Tangier disease"],
        "hyper_conditions": ["Hyperalphalipoproteinemia","Cardiovascular events","Liver disease"]
    },
    "Triglycerides": {
        "hypo_conditions": ["Malnutrition", "Hyperthyroidism", "Malabsorption syndromes"],
        "hyper_conditions": ["Obesity", "Diabetes mellitus", "Hypothyroidism", "Nephrotic syndrome", "Alcoholism"],
    },
    "Apolipoprotein A1": {
        "hypo_conditions": ["Coronary artery disease", "Tangier disease", "Severe liver disease"],
        "hyper_conditions": ["Cardiovascular events", "Cancer"]
    },
    "Apolipoprotein B": {
        "hypo_conditions": ["Abetalipoproteinemia", "Hypobetalipoproteinemia"],
        "hyper_conditions": ["Familial hypercholesterolemia", "Hypothyroidism", "Nephrotic syndrome"],
    },
    "Vitamin D": {
        "hypo_conditions": ["Rickets", "Osteomalacia", "Osteoporosis", "Autoimmune diseases"],
        "hyper_conditions": ["Hypervitaminosis D", "Sarcoidosis", "Hypercalcemia"],
    },
    "Vitamin C": {
        "hypo_conditions": ["Scurvy", "Impaired wound healing", "Weakened immune system"],
        "hyper_conditions": ["Kidney stones", "Gastrointestinal disturbances", "Iron overload"],
    },
    "Vitamin K": {
        "hypo_conditions": ["Bleeding disorders", "Osteoporosis", "Bruising easily"],
        "hyper_conditions": ["Rare, but can interfere with anticoagulant medications"],
    },
    "Vitamin B6 (Pyridoxine)": {
        "hypo_conditions": ["Anemia", "Depression", "Weakened immune system", "Peripheral neuropathy"],
        "hyper_conditions": ["Sensory neuropathy", "Photosensitivity", "Nausea"],
    },
    "Vitamin B1 (Thiamine)": {
        "hypo_conditions": ["Beriberi", "Wernicke-Korsakoff syndrome", "Cardiovascular disease", "Neurological disorders"],
        "hyper_conditions": ["Headaches", "Irritability", "Rapid pulse"],
    },
    "Vitamin B2 (Riboflavin)": {
        "hypo_conditions": ["Ariboflavinosis", "Anemia", "Skin disorders", "Mouth sores"],
        "hyper_conditions": ["Bright yellow urine", "Diarrhea", "Nausea"]
    },
    "Vitamin B3 (Niacin)": {
        "hypo_conditions": ["Pellagra", "Dermatitis", "Dementia", "Diarrhea"],
        "hyper_conditions": ["Skin flushing", "Liver damage", "Glucose intolerance"],
    },
    "Vitamin B5 (Pantothenic Acid)": {
        "hypo_conditions": ["Fatigue", "Insomnia", "Depression", "Numbness in hands and feet"],
        "hyper_conditions": ["Diarrhea", "Gastrointestinal disturbances"]
    },
    "Vitamin B7 (Biotin)": {
        "hypo_conditions": ["Hair loss", "Skin rashes", "Brittle nails", "Neurological symptoms"],
        "hyper_conditions": ["There are no well-documented cases of toxicity from high doses of biotin."]
    },
    "Vitamin B9 (Folate)": {
        "hypo_conditions": ["Anemia", "Neural tube defects", "Depression", "Cognitive impairment"],
        "hyper_conditions": ["Masks Vitamin B12 deficiency", "Can cause gastrointestinal issues in very high doses"]
    },
    "Vitamin B12 (Cobalamin)": {
        "hypo_conditions": ["Pernicious anemia", "Neurological disorders", "Cognitive decline", "Fatigue", "Megaloblastic anemia", "Malabsorption disorders", "Strict vegetarian or vegan diet"],
        "hyper_conditions": ["Excess supplementation", "Liver disease", "Myeloproliferative disorders", "Renal cell carcinoma"],
    },
    "Vitamin A": {
        "hypo_conditions": ["Night blindness", "Dry eyes", "Impaired immune function", "Growth retardation"],
        "hyper_conditions": ["Hypervitaminosis A", "Liver damage", "Bone abnormalities", "Birth defects"],
    },
    "Creatinine": {
        "hypo_conditions": ["Muscular dystrophy", "Myasthenia gravis", "Low muscle mass"],
        "hyper_conditions": ["Chronic kidney disease", "Acute kidney injury", "Dehydration", "Rhabdomyolysis"],
    },
    "Uric Acid": {
        "hypo_conditions": ["Wilson's disease", "Fanconi syndrome"],
        "hyper_conditions": ["Gout", "Kidney stones", "Metabolic syndrome", "Lesch-Nyhan syndrome"],
    },
    "Blood Urea Nitrogen": {
        "hypo_conditions": ["Severe liver disease", "Malnutrition", "Overhydration"],
        "hyper_conditions": ["Kidney disease", "Dehydration", "High protein diet", "Gastrointestinal bleeding"],
    },
    "Cystatin C": {
        "hypo_conditions": ["Rare, not typically associated with clinical conditions"],
        "hyper_conditions": ["Chronic kidney disease", "Acute kidney injury", "Thyroid disorders"],
    },
    "Sodium": {
        "hypo_conditions": ["Hyponatremia", "Addison's disease", "Heart failure"],
        "hyper_conditions": ["Hypernatremia", "Dehydration", "Cushing's syndrome", "Diabetes insipidus"],
    },
    "Potassium": {
        "hypo_conditions": ["Hypokalemia", "Cushing's syndrome", "Diuretic use", "Vomiting or diarrhea"],
        "hyper_conditions": ["Hyperkalemia", "Kidney failure", "Addison's disease", "Severe tissue damage"],
    },
    "Calcium": {
        "hypo_conditions": ["Hypocalcemia", "Hypoparathyroidism", "Vitamin D deficiency", "Renal failure"],
        "hyper_conditions": ["Hypercalcemia", "Hyperparathyroidism", "Certain cancers", "Sarcoidosis"],
    },
    "Magnesium": {
        "hypo_conditions": ["Hypomagnesemia", "Alcoholism", "Malabsorption", "Certain medications"],
        "hyper_conditions": ["Hypermagnesemia", "Kidney failure", "Addison's disease", "antacid use"],
    },
    "Phosphate": {
        "hypo_conditions": ["Hypophosphatemia", "Malnutrition", "Alcoholism", "Hyperparathyroidism"],
        "hyper_conditions": ["Hyperphosphatemia", "Chronic kidney disease", "Hypoparathyroidism", "Tumor lysis syndrome"],
    },
    "Chloride": {
        "hypo_conditions": ["Hypochloremia", "Vomiting", "Addison's disease", "Metabolic alkalosis"],
        "hyper_conditions": ["Hyperchloremia", "Dehydration", "Kidney dysfunction", "Metabolic acidosis"],
    },
    "Bicarbonate": {
        "hypo_conditions": ["Metabolic acidosis", "Diabetic ketoacidosis", "Severe diarrhea", "Renal tubular acidosis"],
        "hyper_conditions": ["Metabolic alkalosis", "Vomiting", "Cushing's syndrome"],
    },
    "Iron": {
        "hypo_conditions": ["Iron deficiency anemia", "Chronic blood loss", "Malabsorption", "Pregnancy"],
        "hyper_conditions": ["Hemochromatosis", "Hemosiderosis", "Frequent blood transfusions", "Iron supplementation"],
    },
    "Globulin": {
        "hypo_conditions": ["Immunodeficiency disorders", "Malnutrition", "Nephrotic syndrome"],
        "hyper_conditions": ["Chronic inflammatory diseases", "Multiple myeloma", "Liver disease", "Autoimmune disorders"],
    },
    "Albumin": {
        "hypo_conditions": ["Malnutrition", "Liver disease", "Nephrotic syndrome", "Inflammatory bowel disease"],
        "hyper_conditions": ["Dehydration", "Rare genetic disorders"],
    },
    "Total Protein": {
        "hypo_conditions": ["Malnutrition", "Liver disease", "Malabsorption", "Burns"],
        "hyper_conditions": ["Dehydration", "Multiple myeloma", "Chronic inflammatory conditions"],
    },
    "Albumin/Globulin Ratio": {
        "hypo_conditions": ["Liver disease", "Autoimmune disorders", "Chronic infections"],
        "hyper_conditions": ["Dehydration", "Some genetic disorders"],
    },
    "C-Reactive Protein": {
        "hypo_conditions": ["Genetic polymorphisms", "Liver failure", "Malnutrition"],
        "hyper_conditions": ["Inflammation", "Infections", "Cardiovascular disease", "Autoimmune disorders"],
    },
    "Haptoglobin": {
        "hypo_conditions": ["Hemolytic anemia", "Liver disease", "Malnutrition"],
        "hyper_conditions": ["Inflammatory conditions", "Tissue damage", "Certain cancers"],
    },
    "Transferrin": {
        "hypo_conditions": ["Iron overload", "Malnutrition", "Chronic illness"],
        "hyper_conditions": ["Iron deficiency anemia", "Pregnancy"],
    },
    "C-Peptide": {
        "hypo_conditions": ["Type 1 diabetes", "Pancreatic disease"],
        "hyper_conditions": ["Insulin resistance", "Insulinoma", "Kidney disease"],
    },
    "Testosterone": {
        "hypo_conditions": ["Hypogonadism", "Klinefelter syndrome", "Aging", "Obesity"],
        "hyper_conditions": ["Polycystic ovary syndrome", "Congenital adrenal hyperplasia", "Testicular tumors"],
    },
    "Estrogen": {
        "hypo_conditions": ["Menopause", "Turner syndrome", "Anorexia nervosa"],
        "hyper_conditions": ["Ovarian tumors", "Cirrhosis", "Obesity"],
    },
    "Progesterone": {
        "hypo_conditions": ["Anovulation", "Menopause", "Luteal phase defect"],
        "hyper_conditions": ["Ovarian cysts", "Congenital adrenal hyperplasia", "Some ovarian tumors"],
    },
    "Cortisol": {
        "hypo_conditions": ["Addison's disease", "Pituitary gland disorders", "Congenital adrenal hyperplasia"],
        "hyper_conditions": ["Cushing's syndrome", "Chronic stress", "Certain medications"],
    },
    "Aldosterone": {
        "hypo_conditions": ["Addison's disease", "Hypoaldosteronism", "Certain medications"],
        "hyper_conditions": ["Conn's syndrome", "Congestive heart failure", "Cirrhosis"],
    },
    "Thyroid-Stimulating Hormone (TSH)": {
        "hypo_conditions": ["Hyperthyroidism", "Pituitary dysfunction"],
        "hyper_conditions": ["Hypothyroidism", "Thyroid hormone resistance"],
    },
    "Free Thyroxine (Free T4)": {
        "hypo_conditions": ["Hypothyroidism", "Iodine deficiency"],
        "hyper_conditions": ["Hyperthyroidism", "Thyroiditis"],
    },
    "Free Triiodothyronine (Free T3)": {
        "hypo_conditions": ["Hypothyroidism", "Euthyroid sick syndrome"],
        "hyper_conditions": ["Hyperthyroidism", "T3 toxicosis"],
    },
    "Aspartate Aminotransferase": {
        "hypo_conditions": ["Vitamin B6 deficiency", "Uremia", "Chronic dialysis"],
        "hyper_conditions": ["Liver disease", "Muscle damage", "Heart attack", "Certain medications"],
    },
    "Alanine Aminotransferase": {
        "hypo_conditions": ["Vitamin B6 deficiency", "Chronic kidney disease"],
        "hyper_conditions": ["Liver disease", "Hepatitis", "Fatty liver", "Certain medications"],
    },
    "Alkaline Phosphatase": {
        "hypo_conditions": ["Hypophosphatasia", "Zinc deficiency", "Malnutrition"],
        "hyper_conditions": ["Liver disease", "Bone disorders", "Pregnancy", "Certain cancers"],
    },
    "Gamma-Glutamyl Transferase": {
        "hypo_conditions": ["Hypothyroidism", "Congenital deficiency"],
        "hyper_conditions": ["Liver disease", "Alcohol abuse", "Pancreatic disease", "Certain medications"],
    },
    "Bilirubin": {
        "hypo_conditions": ["Caffeine consumption", "Certain medications", "Oxidative stress"],
        "hyper_conditions": ["Jaundice", "Liver disease", "Hemolytic anemia", "Gilbert's syndrome"],
    },
    "Lactate Dehydrogenase": {
        "hypo_conditions": ["LDH deficiency","Genetic disorder", "Severe liver disease"],
        "hyper_conditions": ["Tissue damage", "Hemolysis", "Certain cancers", "Heart attack"],
    },
    "Prothrombin Time": {
        "hypo_conditions": ["Hypercoagulable states", "Thrombophilia"],
        "hyper_conditions": ["Liver disease", "Vitamin K deficiency", "Anticoagulant therapy"],
    },
    "Partial Thromboplastin Time": {
        "hypo_conditions": ["Hypercoagulable states", "Increased clotting factor levels"],
        "hyper_conditions": ["Hemophilia", "Von Willebrand disease", "Liver disease", "Heparin therapy"],
    },
    "Fibrinogen": {
        "hypo_conditions": ["Disseminated intravascular coagulation", "Severe liver disease"],
        "hyper_conditions": ["Inflammation", "Pregnancy", "Certain cancers"],
    },
}


    
biochemichals_fruits = {
  "Blood Glucose": {
    "increasing": ["Banana", "Mango", "Pineapple"],
    "decreasing": ["Strawberry", "Blueberry", "Raspberry", "Orange", "Lime", "Apple", "Pear"]
  },
  "Hemoglobin A1c": {
    "increasing": ["Banana", "Mango", "Pineapple"],
    "decreasing": ["Strawberry", "Blueberry", "Raspberry", "Orange", "Lime", "Apple", "Pear"]
  },
  "Glycated Albumin": {
    "increasing": ["Banana", "Mango", "Pineapple"],
    "decreasing": ["Strawberry", "Blueberry", "Raspberry", "Orange", "Lime", "Apple", "Pear"]
  },
  "Total Cholesterol": {
    "increasing": ["Banana", "Mango", "Pineapple"],
    "decreasing": ["Strawberry", "Blueberry", "Raspberry", "Orange", "Lime", "Apple", "Pear"]
  },
  "LDL Cholesterol": {
    "increasing": ["Banana", "Mango", "Pineapple"],
    "decreasing": ["Strawberry", "Blueberry", "Raspberry", "Orange", "Lime", "Apple", "Pear"]
  },
  "HDL Cholesterol": {
    "increasing": ["Strawberry", "Blueberry", "Raspberry", "Orange", "Lime", "Apple", "Pear"],
    "decreasing": ["Banana", "Mango", "Pineapple"]
  },
  "Triglycerides": {
    "increasing": ["Banana", "Mango", "Pineapple"],
    "decreasing": ["Strawberry", "Blueberry", "Raspberry", "Orange", "Lime", "Apple", "Pear"]
  },
  "Apolipoprotein A1": {
    "increasing": ["Strawberry", "Blueberry", "Raspberry", "Orange", "Lime", "Apple", "Pear"],
    "decreasing": ["Banana", "Mango", "Pineapple"]
  },
  "Apolipoprotein B": {
    "increasing": ["Banana", "Mango", "Pineapple"],
    "decreasing": ["Strawberry", "Blueberry", "Raspberry", "Orange", "Lime", "Apple", "Pear"]
  },
  "Vitamin D": {
    "increasing": [],
    "decreasing": []
  },
  "Vitamin C": {
    "increasing": ["Strawberry", "Blueberry", "Raspberry", "Orange", "Lime", "Mandarin", "Mango", "Pineapple", "Kiwi", "Peach", "Plum", "Cherry"],
    "decreasing": []
  },
  "Vitamin K": {
    "increasing": ["Strawberry", "Blueberry", "Raspberry", "Kiwi", "Peach", "Plum", "Mango"],
    "decreasing": []
  },
  "Vitamin B6 (Pyridoxine)": {
    "increasing": ["Banana", "Mango", "Pineapple", "Guava", "Plum", "Watermelon"],
    "decreasing": []
  },
  "Vitamin B1 (Thiamine)": {
    "increasing": ["Orange", "Mandarin", "Mango", "Pineapple", "Guava", "Watermelon"],
    "decreasing": []
  },
  "Vitamin B2 (Riboflavin)": {
    "increasing": ["Banana", "Mango", "Guava", "Apricot"],
    "decreasing": []
  },
  "Vitamin B3 (Niacin)": {
    "increasing": ["Banana", "Mango", "Pineapple", "Guava", "Peach", "Plum"],
    "decreasing": []
  },
  "Vitamin B5 (Pantothenic Acid)": {
    "increasing": ["Strawberry", "Orange", "Banana", "Mango", "Pineapple", "Guava", "Peach", "Plum", "Watermelon"],
    "decreasing": []
  },
  "Vitamin B7 (Biotin)": {
    "increasing": ["Strawberry", "Banana", "Guava"],
    "decreasing": []
  },
  "Vitamin B9 (Folate)": {
    "increasing": ["Strawberry", "Orange", "Mandarin", "Banana", "Mango", "Guava", "Kiwi", "Peach", "Plum"],
    "decreasing": []
  },
  "Vitamin B12 (Cobalamin)": {
    "increasing": [],
    "decreasing": []
  },
  "Vitamin A": {
    "increasing": ["Mango", "Apricot", "Watermelon", "Muskmelon"],
    "decreasing": []
  },
  "Creatinine": {
    "increasing": [],
    "decreasing": ["Apple", "Pear", "Blueberry", "Strawberry", "Watermelon"]
  },
  "Uric Acid": {
    "increasing": ["Cherry"],
    "decreasing": ["Blueberry", "Strawberry", "Orange", "Lime", "Mandarin", "Apple", "Pear", "Peach", "Plum", "Kiwi"]
  },
  "Blood Urea Nitrogen": {
    "increasing": [],
    "decreasing": ["Blueberry", "Strawberry", "Orange", "Apple", "Kiwi", "Watermelon"]
  },
  "Cystatin C": {
    "increasing": [],
    "decreasing": ["Blueberry", "Strawberry", "Apple", "Pear", "Kiwi"]
  },
  "Sodium": {
    "increasing": [],
    "decreasing": ["Blueberry", "Strawberry", "Apple", "Pear", "Orange", "Kiwi", "Watermelon"]
  },
  "Potassium": {
    "increasing": ["Banana", "Kiwi", "Guava", "Orange", "Peach", "Pineapple", "Muskmelon"],
    "decreasing": []
  },
  "Calcium": {
    "increasing": ["Orange", "Kiwi", "Mandarin", "Guava"],
    "decreasing": []
  },
  "Magnesium": {
    "increasing": ["Guava", "Kiwi", "Banana", "Orange", "Pineapple"],
    "decreasing": []
  },
  "Phosphate": {
    "increasing": ["Guava", "Pineapple"],
    "decreasing": []
  },
  "Chloride": {
    "increasing": [],
    "decreasing": []
  },
  "Bicarbonate": {
    "increasing": ["Orange", "Guava"],
    "decreasing": []
  },
  "Iron": {
    "increasing": ["Guava", "Kiwi", "Peach", "Apricot"],
    "decreasing": []
  },
  "Globulin": {
    "increasing": ["Orange", "Guava", "Kiwi", "Apple", "Pineapple", "Blueberry"],
    "decreasing": ["Banana", "Mango", "Muskmelon", "Plum"]
  },
  "Albumin": {
    "increasing": ["Apple", "Kiwi", "Orange", "Guava", "Peach", "Plum"],
    "decreasing": ["Banana", "Watermelon", "Muskmelon", "Pineapple"]
  },
  "Total Protein": {
    "increasing": ["Guava", "Kiwi", "Orange", "Apple", "Pineapple", "Blueberry"],
    "decreasing": ["Banana", "Muskmelon", "Plum", "Watermelon"]
  },
  "Albumin/Globulin Ratio": {
    "increasing": ["Apple", "Kiwi", "Orange", "Guava", "Peach"],
    "decreasing": ["Banana", "Pineapple", "Plum", "Mango"]
  },
  "C-Reactive Protein": {
    "increasing": ["Blueberry", "Guava", "Pineapple"],
    "decreasing": ["Orange", "Kiwi", "Strawberry", "Cherry"]
  },
  "Haptoglobin": {
    "increasing": ["Guava", "Kiwi", "Peach", "Cherry"],
    "decreasing": ["Pineapple", "Mango", "Plum", "Banana"]
  },
  "Transferrin": {
    "increasing": ["Orange", "Kiwi", "Guava", "Apple", "Pear"],
    "decreasing": ["Banana", "Pineapple", "Muskmelon", "Plum"]
  },
  "C-Peptide": {
    "increasing": ["Guava", "Apple", "Kiwi", "Peach", "Pear"],
    "decreasing": ["Banana", "Pineapple", "Plum", "Watermelon"]
  },
  "Testosterone": {
    "increasing": ["Banana", "Guava", "Kiwi"],
    "decreasing": ["Blueberry", "Strawberry"]
  },
  "Estrogen": {
    "increasing": ["Peach", "Plum", "Apricot"],
    "decreasing": ["Lime", "Orange"]
  },
  "Progesterone": {
    "increasing": ["Cherry", "Peach"],
    "decreasing": ["Mango", "Pineapple"]
  },
  "Cortisol": {
    "increasing": ["Orange", "Kiwi", "Banana"],
    "decreasing": ["Blueberry", "Strawberry", "Pear"]
  },
  "Aldosterone": {
    "increasing": ["Guava", "Apple"],
    "decreasing": ["Watermelon", "Muskmelon"]
  },
  "Thyroid-Stimulating Hormone (TSH)": {
    "increasing": ["Apple", "Banana"],
    "decreasing": ["Kiwi", "Guava"]
  },
  "Free Thyroxine (Free T4)": {
    "increasing": ["Guava", "Orange"],
    "decreasing": ["Pineapple", "Plum"]
  },
  "Free Triiodothyronine (Free T3)": {
    "increasing": ["Kiwi", "Peach"],
    "decreasing": ["Mango", "Apricot"]
  },
  "Aspartate Aminotransferase": {
        "increasing": ["Orange", "Banana"],
        "decreasing": ["Blueberry", "Guava", "Apple"]
    },
    "Alanine Aminotransferase": {
        "increasing": ["Mango", "Pineapple"],
        "decreasing": ["Blueberry", "Guava", "Pear"]
    },
    "Alkaline Phosphatase": {
        "increasing": ["Pineapple", "Mango"],
        "decreasing": ["Blueberry", "Guava", "Apple"]
    },
    "Gamma-Glutamyl Transferase": {
        "increasing": ["Orange", "Peach"],
        "decreasing": ["Blueberry", "Guava", "Apple"]
    },
    "Bilirubin": {
        "increasing": ["Orange", "Peach"],
        "decreasing": ["Blueberry", "Guava", "Kiwi"]
    },
    "Lactate Dehydrogenase": {
        "increasing": ["Pineapple", "Mango"],
        "decreasing": ["Blueberry", "Guava", "Apple"]
    },
    "Prothrombin Time": {
        "increasing": ["Orange", "Banana"],
        "decreasing": ["Blueberry", "Guava", "Pear"]
    },
    "Partial Thromboplastin Time": {
        "increasing": ["Mango", "Peach"],
        "decreasing": ["Blueberry", "Guava", "Apple"]
    },
    "Fibrinogen": {
        "increasing": ["Orange", "Peach"],
        "decreasing": ["Blueberry", "Guava", "Kiwi"]
    }
}

biochemichals_vegetables = {
  "Blood Glucose": {
    "increasing": ["Potatoes", "Sweet Potatoes", "Yams", "Cassava", "Beets"],
    "decreasing": ["Spinach", "Kale", "Lettuce", "Broccoli", "Cauliflower", "Cabbage", "Green Peas", "Pumpkin", "Cucumber","Tomatoes", "Asparagus", "Parsley", "Mint", "Thyme", "Rosemary", "Oregano", "Button Mushrooms", "Shiitake Mushrooms", "Portobello Mushrooms", "Bean Sprouts", "Broccoli Sprouts"]
  },
  "Hemoglobin A1c": {
    "increasing": ["Potatoes", "Sweet Potatoes", "Yams", "Cassava", "Beets"],
    "decreasing": ["Spinach", "Kale", "Lettuce", "Broccoli", "Cauliflower", "Cabbage", "Green Peas", "Pumpkin", "Cucumber","Tomatoes", "Asparagus", "Parsley", "Mint", "Thyme", "Rosemary", "Oregano", "Button Mushrooms", "Shiitake Mushrooms", "Portobello Mushrooms", "Bean Sprouts", "Broccoli Sprouts"]
  },
  "Glycated Albumin": {
    "increasing": ["Potatoes", "Sweet Potatoes", "Yams", "Cassava", "Beets"],
    "decreasing": ["Spinach", "Kale", "Lettuce", "Broccoli", "Cauliflower", "Cabbage", "Green Peas", "Pumpkin", "Cucumber","Tomatoes", "Asparagus", "Parsley", "Mint", "Thyme", "Rosemary", "Oregano", "Button Mushrooms", "Shiitake Mushrooms", "Portobello Mushrooms", "Bean Sprouts", "Broccoli Sprouts"]
  },
  "Total Cholesterol": {
    "increasing": ["Beets", "Potatoes", "Sweet Potatoes", "Yams", "Cassava"],
    "decreasing": ["Spinach", "Kale", "Lettuce", "Broccoli", "Cauliflower", "Cabbage", "Green Peas", "Pumpkin", "Cucumber","Tomatoes", "Asparagus", "Parsley", "Mint", "Thyme", "Rosemary", "Oregano", "Button Mushrooms", "Shiitake Mushrooms", "Portobello Mushrooms", "Bean Sprouts", "Broccoli Sprouts"]
  },
  "LDL Cholesterol": {
    "increasing": ["Beets", "Potatoes", "Sweet Potatoes", "Yams", "Cassava"],
    "decreasing": ["Spinach", "Kale", "Lettuce", "Broccoli", "Cauliflower", "Cabbage", "Green Peas", "Pumpkin", "Cucumber","Tomatoes", "Asparagus", "Parsley", "Mint", "Thyme", "Rosemary", "Oregano", "Button Mushrooms", "Shiitake Mushrooms", "Portobello Mushrooms", "Bean Sprouts", "Broccoli Sprouts"]
  },
  "HDL Cholesterol": {
    "increasing": ["Spinach", "Kale", "Lettuce", "Broccoli", "Cauliflower", "Cabbage", "Green Peas", "Pumpkin", "Cucumber","Tomatoes", "Asparagus", "Parsley", "Mint", "Thyme", "Rosemary", "Oregano", "Button Mushrooms", "Shiitake Mushrooms", "Portobello Mushrooms", "Bean Sprouts", "Broccoli Sprouts"],
    "decreasing": ["Beets", "Potatoes", "Sweet Potatoes", "Yams", "Cassava"]
  },
  "Triglycerides": {
    "increasing": ["Potatoes", "Sweet Potatoes", "Yams", "Cassava", "Beets"],
    "decreasing": ["Spinach", "Kale", "Lettuce", "Broccoli", "Cauliflower", "Cabbage", "Green Peas", "Pumpkin", "Cucumber","Tomatoes", "Asparagus", "Parsley", "Mint", "Thyme", "Rosemary", "Oregano", "Button Mushrooms", "Shiitake Mushrooms", "Portobello Mushrooms", "Bean Sprouts", "Broccoli Sprouts"]
  },
  "Apolipoprotein A1": {
    "increasing": ["Spinach", "Kale", "Lettuce", "Broccoli", "Cauliflower", "Cabbage", "Green Peas", "Pumpkin", "Cucumber","Tomatoes", "Asparagus", "Parsley", "Mint", "Thyme", "Rosemary", "Oregano", "Button Mushrooms", "Shiitake Mushrooms", "Portobello Mushrooms", "Bean Sprouts", "Broccoli Sprouts"],
    "decreasing": ["Beets", "Potatoes", "Sweet Potatoes", "Yams", "Cassava"]
  },
  "Apolipoprotein B": {
    "increasing": ["Beets", "Potatoes", "Sweet Potatoes", "Yams", "Cassava"],
    "decreasing": ["Spinach", "Kale", "Lettuce", "Broccoli", "Cauliflower", "Cabbage", "Green Peas", "Pumpkin", "Cucumber","Tomatoes", "Asparagus", "Parsley", "Mint", "Thyme", "Rosemary", "Oregano", "Button Mushrooms", "Shiitake Mushrooms", "Portobello Mushrooms", "Bean Sprouts", "Broccoli Sprouts"]
  },
  "Vitamin D": {
    "increasing": [],
    "decreasing": []
  },
  "Vitamin C": {
    "increasing": ["Bell Peppers", "Broccoli", "Cauliflower", "Kale", "Spinach", "Tomatoes"],
    "decreasing": []
  },
  "Vitamin K": {
    "increasing": ["Kale", "Spinach", "Broccoli", "Green Peas"],
    "decreasing": []
  },
  "Vitamin B6 (Pyridoxine)": {
    "increasing": ["Spinach", "Kale", "Green Peas", "Bell Peppers", "Garlic"],
    "decreasing": []
  },
  "Vitamin B1 (Thiamine)": {
    "increasing": ["Green Peas", "Lentils", "Kidney Beans"],
    "decreasing": []
  },
  "Vitamin B2 (Riboflavin)": {
    "increasing": ["Spinach", "Asparagus", "Broccoli", "Kale", "Lettuce", "Green Peas", "Button Mushrooms", "Shiitake Mushrooms", "Portobello Mushrooms", "Oyster Mushrooms"],
    "decreasing": []
  },
  "Vitamin B3 (Niacin)": {
    "increasing": ["Green Peas", "Spinach", "Asparagus", "Bell Peppers", "Button Mushrooms", "Shiitake Mushrooms", "Portobello Mushrooms", "Oyster Mushrooms"],
    "decreasing": []
  },
  "Vitamin B5 (Pantothenic Acid)": {
    "increasing": ["Spinach", "Broccoli", "Avocado", "Button Mushrooms", "Shiitake Mushrooms", "Portobello Mushrooms", "Oyster Mushrooms", "Sweet Potatoes", "Green Peas"],
    "decreasing": []
  },
  "Vitamin B7 (Biotin)": {
    "increasing": ["Spinach", "Broccoli", "Sweet Potatoes", "Button Mushrooms", "Shiitake Mushrooms", "Portobello Mushrooms", "Oyster Mushrooms", "Cauliflower", "Green Peas"],
    "decreasing": []
  },
  "Vitamin B9 (Folate)": {
    "increasing": ["Spinach", "Kale", "Lettuce", "Broccoli", "Green Peas"],
    "decreasing": []
  },
  "Vitamin B12 (Cobalamin)": {
    "increasing": [],
    "decreasing": []
  },
  "Vitamin A": {
    "increasing": ["Carrots", "Sweet Potatoes", "Butternut Squash", "Spinach", "Kale"],
    "decreasing": []
  },
  "Vitamin D": {
    "increasing": [],
    "decreasing": []
  },
  "Vitamin C": {
    "increasing": ["Bell Peppers", "Broccoli", "Cauliflower", "Kale", "Spinach", "Tomatoes"],
    "decreasing": []
  },
  "Vitamin K": {
    "increasing": ["Kale", "Spinach", "Broccoli", "Green Peas"],
    "decreasing": ["Cauliflower", "Potatoes", "Sweet Potatoes"]
  },
  "Vitamin B6 (Pyridoxine)": {
    "increasing": ["Spinach", "Kale", "Green Peas", "Bell Peppers", "Garlic"],
    "decreasing": []
  },
  "Vitamin B1 (Thiamine)": {
    "increasing": ["Green Peas", "Lentils", "Kidney Beans"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Yams"]
  },
  "Vitamin B2 (Riboflavin)": {
    "increasing": ["Spinach", "Asparagus", "Broccoli", ],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Beets"]
  },
  "Vitamin B3 (Niacin)": {
    "increasing": ["Green Peas", "Spinach"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Yams"]
  },
  "Vitamin B5 (Pantothenic Acid)": {
    "increasing": ["Spinach"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Beets"]
  },
  "Vitamin B7 (Biotin)": {
    "increasing": ["Spinach", "Broccoli", ],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Yams"]
  },
  "Vitamin B9 (Folate)": {
    "increasing": ["Spinach", "Kale", "Lettuce", "Broccoli", "Green Peas"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Yams"]
  },
  "Vitamin B12 (Cobalamin)": {
    "increasing": [],
    "decreasing": []
  },
  "Vitamin A": {
    "increasing": ["Carrots", "Sweet Potatoes", "Butternut Squash", "Spinach", "Kale"],
    "decreasing": ["Potatoes", "Cauliflower", "Zucchini"]
  },
  "Creatinine": {
    "increasing": ["Beets", "Potatoes", "Sweet Potatoes"],
    "decreasing": ["Spinach", "Kale", "Broccoli", "Green Peas", "Cauliflower"]
  },
  "Uric Acid": {
    "increasing": ["Beets", "Spinach", "Green Peas"],
    "decreasing": ["Celery", "Cucumber", "Bell Peppers", "Chickpeas"]
  },
  "Blood Urea Nitrogen": {
    "increasing": ["Beets", "Potatoes", "Sweet Potatoes"],
    "decreasing": ["Spinach", "Kale", "Broccoli", "Green Peas", "Cauliflower"]
  },
  "Cystatin C": {
    "increasing": ["Potatoes", "Beets"],
    "decreasing": ["Spinach", "Kale", "Broccoli", "Green Peas"]
  },
  "Sodium": {
    "increasing": ["Beets", "Celery"],
    "decreasing": ["Cucumber", "Tomatoes", "Bell Peppers", "Spinach"]
  },
  "Potassium": {
    "increasing": ["Spinach", "Sweet Potatoes", "Potatoes", "Green Peas"],
    "decreasing": ["Cauliflower", "Cucumber", "Bell Peppers"]
  },
  "Calcium": {
    "increasing": ["Broccoli", "Kale", "Spinach"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Beets"]
  },
  "Magnesium": {
    "increasing": ["Spinach", "Kale", "Pumpkin", "Beets"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Butternut Squash"]
  },
  "Phosphate": {
    "increasing": ["Beets", "Potatoes", "Sweet Potatoes"],
    "decreasing": ["Spinach", "Kale", "Broccoli", "Cauliflower"]
  },
  "Chloride": {
    "increasing": ["Celery", "Beets"],
    "decreasing": ["Cucumber", "Spinach", "Tomatoes"]
  },
  "Bicarbonate": {
    "increasing": ["Spinach", "Beets", "Potatoes"],
    "decreasing": ["Celery", "Cucumber", "Bell Peppers"]
  },
  "Iron": {
    "increasing": ["Spinach", "Beets", "Green Peas", "Broccoli"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Cauliflower"]
  },
  "Globulin": {
    "increasing": ["Lentils", "Chickpeas", "Kidney Beans", "Green Peas", "Spinach", "Kale"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Cassava", "Yams"]
  },
  "Albumin": {
    "increasing": ["Lentils", "Chickpeas", "Kidney Beans", "Spinach", "Kale"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Yams"]
  },
  "Total Protein": {
    "increasing": ["Lentils", "Chickpeas", "Kidney Beans", "Green Peas", "Spinach", "Kale"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Cassava", "Yams"]
  },
  "Albumin/Globulin Ratio": {
    "increasing": ["Lentils", "Chickpeas", "Kidney Beans", "Spinach", "Kale"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Cassava", "Yams"]
  },
  "C-Reactive Protein": {
    "increasing": ["Potatoes", "Sweet Potatoes", "Cassava", "Yams"],
    "decreasing": ["Spinach", "Kale", "Broccoli", "Green Peas", "Bell Peppers"]
  },
  "Haptoglobin": {
    "increasing": ["Lentils", "Chickpeas", "Kidney Beans", "Green Peas", "Spinach"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Yams"]
  },
  "Transferrin": {
    "increasing": ["Spinach", "Kale", "Green Peas", "Lentils", "Chickpeas"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Cassava"]
  },
  "C-Peptide": {
    "increasing": ["Lentils", "Chickpeas", "Green Peas", "Spinach", "Kale"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Yams"]
  },
  "Testosterone": {
    "increasing": ["Spinach", "Kale", "Garlic"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Yams"]
  },
  "Estrogen": {
    "increasing": ["Spinach", "Kale", "Broccoli", "Bell Peppers"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Yams"]
  },
  "Progesterone": {
    "increasing": ["Spinach", "Kale", "Lentils", "Chickpeas"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Cassava"]
  },
  "Cortisol": {
    "increasing": ["Potatoes", "Sweet Potatoes", "Yams"],
    "decreasing": ["Spinach", "Kale", "Green Peas", "Broccoli"]
  },
  "Aldosterone": {
    "increasing": ["Spinach", "Kale", "Lentils", "Chickpeas"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Yams"]
  },
  "Thyroid-Stimulating Hormone (TSH)": {
    "increasing": ["Spinach", "Kale", "Broccoli", "Green Peas"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Yams"]
  },
  "Free Thyroxine (Free T4)": {
    "increasing": ["Spinach", "Kale", "Broccoli", "Green Peas"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Yams"]
  },
  "Free Triiodothyronine (Free T3)": {
    "increasing": ["Spinach", "Kale", "Broccoli", "Green Peas"],
    "decreasing": ["Potatoes", "Sweet Potatoes", "Yams"]
  },
  "Aspartate Aminotransferase": {
    "increasing": [],
    "decreasing": ["Broccoli", "Spinach", "Kale", "Asparagus", "Garlic"]
  },
  "Alanine Aminotransferase": {
    "increasing": [],
    "decreasing": ["Broccoli", "Spinach", "Kale", "Garlic", "Onion"]
  },
  "Alkaline Phosphatase": {
    "increasing": [],
    "decreasing": ["Spinach", "Kale", "Broccoli", "Asparagus", "Garlic"]
  },
  "Gamma-Glutamyl Transferase": {
    "increasing": [],
    "decreasing": ["Spinach", "Kale", "Broccoli", "Garlic", "Onion"]
  },
  "Bilirubin": {
    "increasing": [],
    "decreasing": ["Spinach", "Kale", "Broccoli", "Garlic", "Beets"]
  },
  "Lactate Dehydrogenase": {
    "increasing": [],
    "decreasing": ["Spinach", "Kale", "Broccoli", "Garlic", "Beets"]
  },
  "Prothrombin Time": {
    "increasing": [],
    "decreasing": ["Spinach", "Kale", "Broccoli", "Green Peas", "Asparagus"]
  },
  "Partial Thromboplastin Time": {
    "increasing": [],
    "decreasing": ["Spinach", "Kale", "Broccoli", "Green Peas", "Asparagus"]
  },
  "Fibrinogen": {
    "increasing": [],
    "decreasing": ["Spinach", "Kale", "Broccoli", "Garlic", "Green Peas"]
  }
}

biochemicals_seeds = {
    "Blood Glucose": {
    "increasing": ["Wheat", "Rice", "Corn", "Barley", "Oats", "Millet"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed"]
  },
  "Hemoglobin A1c": {
    "increasing": ["Wheat", "Rice", "Corn", "Barley", "Oats", "Millet"],
    "decreasing": ["Almond", "Cashew", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed"]
  },
  "Glycated Albumin": {
    "increasing": ["Wheat", "Rice", "Corn", "Barley", "Oats", "Millet"],
    "decreasing": ["Almond", "Cashew", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed"]
  },
  "Total Cholesterol": {
    "increasing": ["Cashew", "Pistachio", "Pine Nut"],
    "decreasing": ["Almond", "Chestnut", "Hazelnut", "Walnut", "Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed", "Oats", "Barley"]
  },
  "LDL Cholesterol": {
    "increasing": ["Cashew", "Pistachio", "Pine Nut"],
    "decreasing": ["Almond", "Chestnut", "Hazelnut", "Walnut", "Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed", "Oats", "Barley"]
  },
  "HDL Cholesterol": {
    "increasing": ["Almond", "Cashew", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed"],
    "decreasing": ["Wheat", "Rice", "Corn", "Millet"]
  },
  "Triglycerides": {
    "increasing": ["Wheat", "Rice", "Corn", "Millet"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed", "Oats", "Barley"]
  },
  "Apolipoprotein A1": {
    "increasing": ["Almond", "Cashew", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed"],
    "decreasing": ["Wheat", "Rice", "Corn", "Millet"]
  },
  "Apolipoprotein B": {
    "increasing": ["Wheat", "Rice", "Corn", "Millet"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed", "Oats", "Barley"]
  },
  "Vitamin D": {
    "increasing": ["Sunflower Seed", "Pumpkin Seed", "Almond", "Chestnut", "Hazelnut", "Pistachio", "Walnut"],
    "decreasing": []
  },
  "Vitamin C": {
    "increasing": ["Chestnut", "Almond", "Pistachio", "Sunflower Seed", "Pumpkin Seed"],
    "decreasing": []
  },
  "Vitamin K": {
    "increasing": ["Pine Nut", "Pumpkin Seed", "Cashew", "Hazelnut", "Pistachio", "Almond", "Walnut", "Sunflower Seed", "Sesame Seed"],
    "decreasing": []
  },
  "Vitamin B6 (Pyridoxine)": {
    "increasing": ["Sunflower Seed", "Pistachio", "Sesame Seed", "Wheat", "Rice", "Corn", "Barley", "Oats", "Millet", "Almond", "Cashew", "Hazelnut", "Walnut", "Pine Nut", "Pumpkin Seed", "Flax Seed"],
    "decreasing": []
  },
  "Vitamin B1 (Thiamine)": {
    "increasing": ["Sunflower Seed", "Pistachio", "Pine Nut", "Flax Seed", "Oats", "Wheat", "Rice", "Corn", "Barley", "Millet", "Almond", "Cashew", "Hazelnut", "Walnut", "Pumpkin Seed", "Chia Seed", "Sesame Seed"],
    "decreasing": []
  },
  "Vitamin B2 (Riboflavin)": {
    "increasing": ["Almond", "Sunflower Seed", "Sesame Seed", "Wheat", "Oats", "Cashew", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Pumpkin Seed", "Flax Seed", "Rice", "Corn", "Barley", "Millet"],
    "decreasing": []
  },
  "Vitamin B3 (Niacin)": {
    "increasing": ["Sunflower Seed", "Wheat", "Rice", "Corn", "Barley", "Oats", "Millet", "Almond", "Cashew", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Pumpkin Seed", "Sesame Seed"],
    "decreasing": []
  },
  "Vitamin B5 (Pantothenic Acid)": {
    "increasing": ["Sunflower Seed", "Wheat", "Oats", "Almond", "Cashew", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Pumpkin Seed", "Flax Seed", "Sesame Seed", "Rice", "Corn", "Barley", "Millet"],
    "decreasing": []
  },
  "Vitamin B7 (Biotin)": {
    "increasing": ["Sunflower Seed", "Almond", "Walnut", "Oats", "Pumpkin Seed", "Sesame Seed", "Wheat", "Rice", "Corn", "Barley", "Millet"],
    "decreasing": []
  },
  "Vitamin B9 (Folate)": {
    "increasing": ["Sunflower Seed", "Flax Seed", "Wheat", "Corn", "Oats", "Almond", "Cashew", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Pumpkin Seed", "Chia Seed", "Sesame Seed", "Rice", "Barley", "Millet"],
    "decreasing": []
  },
  "Vitamin B12 (Cobalamin)": {
    "increasing": [],
    "decreasing": []
  },
  "Vitamin A": {
    "increasing": ["Pumpkin Seed", "Sunflower Seed", "Almond", "Pistachio", "Sesame Seed"],
    "decreasing": []
  },
    "Creatinine": {
    "increasing": ["Almond", "Cashew", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Sunflower Seed", "Pumpkin Seed"],
    "decreasing": ["Chia Seed", "Flax Seed", "Sesame Seed"]
  },
  "Uric Acid": {
    "increasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Sunflower Seed"],
    "decreasing": ["Chia Seed", "Flax Seed", "Sesame Seed"]
  },
  "Blood Urea Nitrogen": {
    "increasing": ["Almond", "Cashew", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Sunflower Seed"],
    "decreasing": ["Chia Seed", "Flax Seed", "Sesame Seed"]
  },
  "Cystatin C": {
    "increasing": ["Pistachio", "Walnut"],
    "decreasing": ["Chia Seed", "Flax Seed"]
  },
  "Sodium": {
    "increasing": ["Sunflower Seed", "Pumpkin Seed"],
    "decreasing": ["Chia Seed", "Flax Seed"]
  },
  "Potassium": {
    "increasing": ["Almond", "Cashew", "Pistachio", "Walnut", "Pumpkin Seed"],
    "decreasing": ["Chia Seed", "Flax Seed"]
  },
  "Calcium": {
    "increasing": ["Almond", "Sesame Seed"],
    "decreasing": ["Chia Seed"]
  },
  "Magnesium": {
    "increasing": ["Almond", "Cashew", "Hazelnut", "Pistachio", "Walnut", "Pumpkin Seed", "Chia Seed", "Flax Seed"],
    "decreasing": []
  },
  "Phosphate": {
    "increasing": ["Almond", "Cashew", "Hazelnut", "Pistachio", "Walnut", "Pumpkin Seed"],
    "decreasing": ["Chia Seed", "Flax Seed"]
  },
  "Chloride": {
    "increasing": ["Sunflower Seed"],
    "decreasing": ["Chia Seed", "Flax Seed"]
  },
  "Bicarbonate": {
    "increasing": ["Almond"],
    "decreasing": ["Chia Seed", "Flax Seed"]
  },
  "Iron": {
    "increasing": ["Pumpkin Seed", "Sunflower Seed", "Sesame Seed"],
    "decreasing": ["Chia Seed", "Flax Seed"]
  },
  "Globulin": {
    "increasing": ["Sunflower Seed", "Pumpkin Seed", "Flax Seed", "Sesame Seed", "Chia Seed"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut", "Pine Nut"]
  },
  "Albumin": {
    "increasing": ["Pumpkin Seed", "Flax Seed", "Sesame Seed", "Chia Seed", "Sunflower Seed"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut"]
  },
  "Total Protein": {
    "increasing": ["Almond", "Cashew", "Pumpkin Seed", "Sunflower Seed", "Chia Seed", "Flax Seed", "Sesame Seed", "Pistachio", "Walnut"],
    "decreasing": ["Rice", "Corn", "Barley", "Oats", "Millet"]
  },
  "Albumin/Globulin Ratio": {
    "increasing": ["Pumpkin Seed", "Flax Seed", "Sesame Seed", "Chia Seed", "Sunflower Seed"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut"]
  },
  "C-Reactive Protein": {
    "increasing": ["Corn", "Barley"],
    "decreasing": ["Almond", "Cashew", "Walnut", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed"]
  },
  "Haptoglobin": {
    "increasing": ["Corn", "Barley"],
    "decreasing": ["Almond", "Cashew", "Walnut", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed"]
  },
  "Transferrin": {
    "increasing": ["Pumpkin Seed", "Chia Seed", "Flax Seed", "Sunflower Seed", "Pistachio"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Walnut", "Pine Nut"]
  },
  "C-Peptide": {
    "increasing": ["Pumpkin Seed", "Chia Seed", "Flax Seed", "Sunflower Seed", "Pistachio"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Walnut", "Pine Nut"]
  },
  "Testosterone": {
    "increasing": ["Pumpkin Seed", "Pistachio", "Chia Seed", "Sunflower Seed"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Walnut", "Pine Nut"]
  },
  "Estrogen": {
    "increasing": ["Flax Seed", "Sesame Seed", "Chia Seed"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut", "Pine Nut"]
  },
  "Progesterone": {
    "increasing": ["Flax Seed", "Sesame Seed", "Chia Seed"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut", "Pine Nut"]
  },
  "Cortisol": {
    "increasing": ["Corn", "Barley"],
    "decreasing": ["Almond", "Cashew", "Walnut", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed"]
  },
  "Aldosterone": {
    "increasing": ["Corn", "Barley"],
    "decreasing": ["Almond", "Cashew", "Walnut", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed"]
  },
  "Thyroid-Stimulating Hormone (TSH)": {
    "increasing": ["Corn", "Barley"],
    "decreasing": ["Almond", "Cashew", "Walnut", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed"]
  },
  "Free Thyroxine (Free T4)": {
    "increasing": ["Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut"]
  },
  "Free Triiodothyronine (Free T3)": {
    "increasing": ["Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut"]
  },
    "Aspartate Aminotransferase": {
    "increasing": ["Corn", "Barley"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed", "Wheat", "Oats"]
  },
  "Alanine Aminotransferase": {
    "increasing": ["Corn", "Barley"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed", "Wheat", "Oats"]
  },
  "Alkaline Phosphatase": {
    "increasing": ["Corn", "Barley", "Rice"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed", "Wheat", "Oats"]
  },
  "Gamma-Glutamyl Transferase": {
    "increasing": ["Corn", "Barley"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed", "Wheat", "Oats"]
  },
  "Bilirubin": {
    "increasing": ["Corn", "Barley"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed", "Wheat", "Oats"]
  },
  "Lactate Dehydrogenase": {
    "increasing": ["Corn", "Barley"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed", "Wheat", "Oats"]
  },
  "Prothrombin Time": {
    "increasing": ["Corn", "Barley", "Rice"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed", "Wheat", "Oats"]
  },
  "Partial Thromboplastin Time": {
    "increasing": ["Corn", "Barley"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed", "Wheat", "Oats"]
  },
  "Fibrinogen": {
    "increasing": ["Corn", "Barley"],
    "decreasing": ["Almond", "Cashew", "Chestnut", "Hazelnut", "Pistachio", "Walnut", "Pine Nut", "Sunflower Seed", "Pumpkin Seed", "Chia Seed", "Flax Seed", "Sesame Seed", "Wheat", "Oats"]
  }
}

biochemicals_seafoods = {
  "Blood Glucose": {
    "increasing": ["Oysters"],
    "decreasing": ["Salmon", "Mackerel", "Sardines", "Cod", "Haddock", "Halibut", "Pollock"]
  },
  "Hemoglobin A1c": {
    "increasing": [],
    "decreasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Halibut"]
  },
  "Glycated Albumin": {
    "increasing": [],
    "decreasing": ["Salmon", "Mackerel", "Sardines", "Tuna"]
  },
  "Total Cholesterol": {
    "increasing": ["Shrimp", "Crab", "Lobster"],
    "decreasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Halibut", "Tilapia", "Pollock", "Oysters", "Mussels"]
  },
  "LDL Cholesterol": {
    "increasing": ["Shrimp", "Crab", "Lobster"],
    "decreasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Halibut", "Tilapia", "Pollock"]
  },
  "HDL Cholesterol": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Oysters"],
    "decreasing": []
  },
  "Triglycerides": {
    "increasing": ["Tilapia"],
    "decreasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Halibut", "Pollock", "Oysters"]
  },
  "Apolipoprotein A1": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna"],
    "decreasing": []
  },
  "Apolipoprotein B": {
    "increasing": ["Shrimp", "Crab", "Lobster"],
    "decreasing": ["Salmon", "Mackerel", "Sardines", "Tuna"]
  },
  "Vitamin D": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Halibut", "Oysters"],
    "decreasing": []
  },
  "Vitamin C": {
    "increasing": ["Oysters"],
    "decreasing": []
  },
  "Vitamin K": {
    "increasing": ["Salmon", "Tuna", "Shrimp"],
    "decreasing": []
  },
  "Vitamin B6 (Pyridoxine)": {
    "increasing": ["Salmon", "Tuna", "Cod", "Halibut", "Tilapia", "Shrimp"],
    "decreasing": []
  },
  "Vitamin B1 (Thiamine)": {
    "increasing": ["Tuna", "Mackerel", "Mussels", "Oysters"],
    "decreasing": []
  },
  "Vitamin B2 (Riboflavin)": {
    "increasing": ["Mackerel", "Salmon", "Tuna", "Oysters", "Mussels"],
    "decreasing": []
  },
  "Vitamin B3 (Niacin)": {
    "increasing": ["Tuna", "Salmon", "Mackerel", "Sardines", "Halibut", "Tilapia"],
    "decreasing": []
  },
  "Vitamin B5 (Pantothenic Acid)": {
    "increasing": ["Salmon", "Tuna", "Oysters", "Lobster"],
    "decreasing": []
  },
  "Vitamin B7 (Biotin)": {
    "increasing": ["Salmon", "Tuna", "Oysters"],
    "decreasing": []
  },
  "Vitamin B9 (Folate)": {
    "increasing": ["Salmon", "Tuna", "Cod", "Halibut", "Crab", "Shrimp", "Mussels"],
    "decreasing": []
  },
  "Vitamin B12 (Cobalamin)": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Haddock", "Halibut", "Pollock", "Crab", "Oysters", "Lobster", "Mussels"],
    "decreasing": []
  },
  "Vitamin A": {
    "increasing": ["Salmon", "Mackerel", "Tuna", "Cod", "Halibut", "Oysters"],
    "decreasing": []
  },
  "Creatinine": {
    "increasing": ["Tuna", "Shrimp", "Crab", "Lobster"],
    "decreasing": ["Salmon", "Mackerel", "Sardines", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Oysters", "Mussels"]
  },
  "Uric Acid": {
    "increasing": ["Tuna", "Shrimp", "Crab", "Lobster"],
    "decreasing": ["Salmon", "Mackerel", "Sardines", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Oysters", "Mussels"]
  },
  "Blood Urea Nitrogen": {
    "increasing": ["Tuna", "Shrimp", "Crab", "Lobster"],
    "decreasing": ["Salmon", "Mackerel", "Sardines", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Oysters", "Mussels"]
  },
  "Cystatin C": {
    "increasing": ["Tuna", "Shrimp", "Crab", "Lobster"],
    "decreasing": ["Salmon", "Mackerel", "Sardines", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Oysters", "Mussels"]
  },
  "Sodium": {
    "increasing": ["Shrimp", "Crab", "Lobster"],
    "decreasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Oysters", "Mussels"]
  },
  "Potassium": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Halibut"],
    "decreasing": []
  },
  "Calcium": {
    "increasing": ["Sardines", "Mackerel", "Salmon", "Oysters", "Shrimp"],
    "decreasing": []
  },
  "Magnesium": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna"],
    "decreasing": []
  },
  "Phosphate": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Shrimp", "Oysters"],
    "decreasing": []
  },
  "Chloride": {
    "increasing": ["Shrimp", "Crab", "Lobster"],
    "decreasing": []
  },
  "Bicarbonate": {
    "increasing": [],
    "decreasing": []
  },
  "Iron": {
    "increasing": ["Sardines", "Oysters", "Mussels", "Shrimp", "Crab", "Lobster"],
    "decreasing": []
  },
  "Globulin": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Shrimp", "Crab", "Oysters", "Lobster", "Mussels"],
    "decreasing": []
  },
  "Albumin": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Shrimp", "Crab", "Oysters", "Lobster", "Mussels"],
    "decreasing": []
  },
  "Total Protein": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Shrimp", "Crab", "Oysters", "Lobster", "Mussels"],
    "decreasing": []
  },
  "Albumin/Globulin Ratio": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Shrimp", "Crab", "Oysters", "Lobster", "Mussels"],
    "decreasing": []
  },
  "C-Reactive Protein": {
    "increasing": [],
    "decreasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Shrimp", "Crab", "Oysters", "Lobster", "Mussels"]
  },
  "Haptoglobin": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Shrimp", "Crab", "Oysters", "Lobster", "Mussels"],
    "decreasing": []
  },
  "Transferrin": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Shrimp", "Crab", "Oysters", "Lobster", "Mussels"],
    "decreasing": []
  },
  "C-Peptide": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Shrimp", "Crab", "Oysters", "Lobster", "Mussels"],
    "decreasing": []
  },
  "Testosterone": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Shrimp", "Crab", "Oysters", "Lobster", "Mussels"],
    "decreasing": []
  },
  "Estrogen": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Shrimp", "Crab", "Oysters", "Lobster", "Mussels"],
    "decreasing": []
  },
  "Progesterone": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Shrimp", "Crab", "Oysters", "Lobster", "Mussels"],
    "decreasing": []
  },
  "Cortisol": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Shrimp", "Crab", "Oysters", "Lobster", "Mussels"],
    "decreasing": []
  },
  "Aldosterone": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Shrimp", "Crab", "Oysters", "Lobster", "Mussels"],
    "decreasing": []
  },
  "Thyroid-Stimulating Hormone (TSH)": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Shrimp", "Crab", "Oysters", "Lobster", "Mussels"],
    "decreasing": []
  },
  "Free Thyroxine (Free T4)": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Shrimp", "Crab", "Oysters", "Lobster", "Mussels"],
    "decreasing": []
  },
  "Free Triiodothyronine (Free T3)": {
    "increasing": ["Salmon", "Mackerel", "Sardines", "Tuna", "Cod", "Haddock", "Tilapia", "Halibut", "Pollock", "Shrimp", "Crab", "Oysters", "Lobster", "Mussels"],
    "decreasing": []
  },
  "Aspartate Aminotransferase": {
    "increasing": ["Tuna", "Mackerel", "Halibut"],
    "decreasing": ["Salmon", "Cod", "Sardines"]
  },
  "Alanine Aminotransferase": {
    "increasing": ["Tuna", "Mackerel", "Pollock"],
    "decreasing": ["Salmon", "Sardines", "Shrimp"]
  },
  "Alkaline Phosphatase": {
    "increasing": ["Cod", "Halibut", "Mussels"],
    "decreasing": ["Salmon", "Sardines", "Oysters"]
  },
  "Gamma-Glutamyl Transferase": {
    "increasing": ["Tuna", "Mackerel", "Pollock"],
    "decreasing": ["Salmon", "Cod", "Shrimp"]
  },
  "Bilirubin": {
    "increasing": ["Mackerel", "Tuna", "Sardines"],
    "decreasing": ["Salmon", "Cod", "Oysters"]
  },
  "Lactate Dehydrogenase": {
    "increasing": ["Tuna", "Halibut", "Mackerel"],
    "decreasing": ["Salmon", "Cod", "Shrimp"]
  },
  "Prothrombin Time": {
    "increasing": ["Cod", "Pollock", "Shrimp"],
    "decreasing": ["Salmon", "Sardines", "Oysters"]
  },
  "Partial Thromboplastin Time": {
    "increasing": ["Tuna", "Mackerel", "Pollock"],
    "decreasing": ["Salmon", "Cod", "Shrimp"]
  },
  "Fibrinogen": {
    "increasing": ["Halibut", "Mussels", "Oysters"],
    "decreasing": ["Salmon", "Sardines", "Crab"]
  }
}

biochemicals_seeds_diarys = {
  "Blood Glucose": {
    "increasing": ["Whole Milk","Greek Yogurt", "Yogurt"], 
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella"]
  },
  "Hemoglobin A1c": {
    "increasing": ["Whole Milk", "Greek Yogurt", "Yogurt"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella"]
  },
  "Glycated Albumin": {
    "increasing": ["Whole Milk", "Greek Yogurt", "Yogurt"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella"]
  },
  "Total Cholesterol": {
    "increasing": ["Whole Milk", "Cheddar", "Butter", "Ghee", "Mozzarella"],
    "decreasing": ["Almond Milk", "Soy Milk", "Greek Yogurt"]
  },
  "LDL Cholesterol": {
    "increasing": ["Whole Milk", "Cheddar", "Butter", "Ghee", "Mozzarella"],
    "decreasing": ["Almond Milk", "Soy Milk", "Greek Yogurt"]
  },
  "HDL Cholesterol": {
    "increasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Greek Yogurt"],
    "decreasing": ["Whole Milk", "Cheddar", "Butter", "Ghee"]
  },
  "Triglycerides": {
    "increasing": ["Whole Milk", "Cheddar", "Butter", "Ghee", "Mozzarella"],
    "decreasing": ["Almond Milk", "Soy Milk", "Greek Yogurt"]
  },
  "Apolipoprotein A1": {
    "increasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Greek Yogurt"],
    "decreasing": ["Whole Milk", "Cheddar", "Butter", "Ghee"]
  },
  "Apolipoprotein B": {
    "increasing": ["Whole Milk", "Cheddar", "Butter", "Ghee", "Mozzarella"],
    "decreasing": ["Almond Milk", "Soy Milk", "Greek Yogurt"]
  },
  "Vitamin D": {
    "increasing": ["Whole Milk", "Greek Yogurt", "Cheddar"], 
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "Vitamin C": {
    "increasing": [], 
    "decreasing": ["Whole Milk", "Almond Milk", "Soy Milk", "Cheddar", "Mozzarella", "Greek Yogurt", "Yogurt", "Butter", "Ghee"]
  },
  "Vitamin K": {
    "increasing": ["Cheddar", "Mozzarella"], 
    "decreasing": ["Whole Milk", "Almond Milk", "Soy Milk", "Greek Yogurt", "Yogurt", "Butter", "Ghee"]
  },
  "Vitamin B6 (Pyridoxine)": {
    "increasing": ["Greek Yogurt"], 
    "decreasing": ["Whole Milk", "Almond Milk", "Soy Milk", "Cheddar", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "Vitamin B1 (Thiamine)": {
    "increasing": [], 
    "decreasing": ["Whole Milk", "Almond Milk", "Soy Milk", "Cheddar", "Mozzarella", "Greek Yogurt", "Yogurt", "Butter", "Ghee"]
  },
  "Vitamin B2 (Riboflavin)": {
    "increasing": ["Cheddar", "Mozzarella", "Greek Yogurt"], 
    "decreasing": ["Whole Milk", "Almond Milk", "Soy Milk", "Yogurt", "Butter", "Ghee"]
  },
  "Vitamin B3 (Niacin)": {
    "increasing": [], 
    "decreasing": ["Whole Milk", "Almond Milk", "Soy Milk", "Cheddar", "Mozzarella", "Greek Yogurt", "Yogurt", "Butter", "Ghee"]
  },
  "Vitamin B5 (Pantothenic Acid)": {
    "increasing": ["Greek Yogurt"], 
    "decreasing": ["Whole Milk", "Almond Milk", "Soy Milk", "Cheddar", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "Vitamin B7 (Biotin)": {
    "increasing": [], 
    "decreasing": ["Whole Milk", "Almond Milk", "Soy Milk", "Cheddar", "Mozzarella", "Greek Yogurt", "Yogurt", "Butter", "Ghee"]
  },
  "Vitamin B9 (Folate)": {
    "increasing": [], 
    "decreasing": ["Whole Milk", "Almond Milk", "Soy Milk", "Cheddar", "Mozzarella", "Greek Yogurt", "Yogurt", "Butter", "Ghee"]
  },
  "Vitamin B12 (Cobalamin)": {
    "increasing": ["Whole Milk", "Cheddar", "Mozzarella", "Greek Yogurt"], 
    "decreasing": ["Almond Milk", "Soy Milk", "Yogurt", "Butter", "Ghee"]
  },
  "Vitamin A": {
    "increasing": ["Whole Milk", "Cheddar", "Butter", "Ghee"], 
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Greek Yogurt", "Yogurt"]
  },
  "Creatinine": {
    "increasing": ["Whole Milk", "Cheddar", "Greek Yogurt"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "Uric Acid": {
    "increasing": ["Cheddar", "Mozzarella", "Greek Yogurt", "Whole Milk"],
    "decreasing": ["Almond Milk", "Soy Milk", "Yogurt", "Butter", "Ghee"]
  },
  "Blood Urea Nitrogen": {
    "increasing": ["Whole Milk", "Cheddar", "Greek Yogurt"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "Cystatin C": {
    "increasing": ["Whole Milk", "Cheddar", "Greek Yogurt"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "Sodium": {
    "increasing": ["Cheddar", "Mozzarella", "Butter", "Ghee"],
    "decreasing": ["Whole Milk", "Almond Milk", "Soy Milk", "Greek Yogurt", "Yogurt"]
  },
  "Potassium": {
    "increasing": ["Whole Milk", "Almond Milk", "Soy Milk", "Greek Yogurt", "Yogurt"],
    "decreasing": ["Cheddar", "Mozzarella", "Butter", "Ghee"]
  },
  "Calcium": {
    "increasing": ["Whole Milk", "Cheddar", "Mozzarella", "Greek Yogurt", "Yogurt"],
    "decreasing": ["Almond Milk", "Soy Milk", "Butter", "Ghee"]
  },
  "Magnesium": {
    "increasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Greek Yogurt"],
    "decreasing": ["Whole Milk", "Cheddar", "Yogurt", "Butter", "Ghee"]
  },
  "Phosphate": {
    "increasing": ["Whole Milk", "Cheddar", "Greek Yogurt"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "Chloride": {
    "increasing": ["Cheddar", "Mozzarella", "Butter", "Ghee"],
    "decreasing": ["Whole Milk", "Almond Milk", "Soy Milk", "Greek Yogurt", "Yogurt"]
  },
  "Bicarbonate": {
    "increasing": ["Whole Milk", "Cheddar", "Greek Yogurt"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "Iron": {
    "increasing": ["Cheddar", "Greek Yogurt", "Whole Milk"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "Globulin": {
    "increasing": ["Whole Milk", "Cheddar", "Greek Yogurt"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "Albumin": {
    "increasing": ["Whole Milk", "Greek Yogurt", "Mozzarella"],
    "decreasing": ["Almond Milk", "Soy Milk", "Cheddar", "Yogurt", "Butter", "Ghee"]
  },
  "Total Protein": {
    "increasing": ["Whole Milk", "Cheddar", "Greek Yogurt", "Mozzarella"],
    "decreasing": ["Almond Milk", "Soy Milk", "Yogurt", "Butter", "Ghee"]
  },
  "Albumin/Globulin Ratio": {
    "increasing": ["Whole Milk", "Greek Yogurt", "Mozzarella"],
    "decreasing": ["Cheddar", "Almond Milk", "Soy Milk", "Yogurt", "Butter", "Ghee"]
  },
  "C-Reactive Protein": {
    "increasing": ["Cheddar", "Greek Yogurt", "Whole Milk"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "Haptoglobin": {
    "increasing": ["Whole Milk", "Cheddar", "Greek Yogurt"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "Transferrin": {
    "increasing": ["Whole Milk", "Greek Yogurt", "Cheddar"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "C-Peptide": {
    "increasing": ["Whole Milk", "Cheddar", "Greek Yogurt"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "Testosterone": {
    "increasing": ["Cheddar", "Greek Yogurt"],
    "decreasing": ["Whole Milk", "Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "Estrogen": {
    "increasing": ["Whole Milk", "Cheddar", "Greek Yogurt"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "Progesterone": {
    "increasing": ["Whole Milk", "Greek Yogurt"],
    "decreasing": ["Almond Milk", "Soy Milk", "Cheddar", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "Cortisol": {
    "increasing": ["Whole Milk", "Cheddar", "Greek Yogurt"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "Aldosterone": {
    "increasing": ["Cheddar", "Greek Yogurt"],
    "decreasing": ["Whole Milk", "Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "Thyroid-Stimulating Hormone (TSH)": {
    "increasing": ["Whole Milk", "Cheddar"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Greek Yogurt", "Yogurt", "Butter", "Ghee"]
  },
  "Free Thyroxine (Free T4)": {
    "increasing": ["Cheddar", "Greek Yogurt"],
    "decreasing": ["Whole Milk", "Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Butter", "Ghee"]
  },
  "Free Triiodothyronine (Free T3)": {
    "increasing": ["Whole Milk", "Cheddar"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Greek Yogurt", "Yogurt", "Butter", "Ghee"]
  },
  "Aspartate Aminotransferase": {
    "increasing": ["Whole Milk", "Cheddar", "Greek Yogurt", "Butter"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Ghee"]
  },
  "Alanine Aminotransferase": {
    "increasing": ["Whole Milk", "Cheddar", "Greek Yogurt", "Butter"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Ghee"]
  },
  "Alkaline Phosphatase": {
    "increasing": ["Cheddar", "Greek Yogurt", "Butter"],
    "decreasing": ["Whole Milk", "Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Ghee"]
  },
  "Gamma-Glutamyl Transferase": {
    "increasing": ["Cheddar", "Greek Yogurt", "Butter"],
    "decreasing": ["Whole Milk", "Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Ghee"]
  },
  "Bilirubin": {
    "increasing": ["Whole Milk", "Cheddar", "Butter"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Greek Yogurt", "Yogurt", "Ghee"]
  },
  "Lactate Dehydrogenase": {
    "increasing": ["Cheddar", "Greek Yogurt", "Butter"],
    "decreasing": ["Whole Milk", "Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Ghee"]
  },
  "Prothrombin Time": {
    "increasing": ["Whole Milk", "Cheddar", "Greek Yogurt", "Butter"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Ghee"]
  },
  "Partial Thromboplastin Time": {
    "increasing": ["Cheddar", "Greek Yogurt", "Butter"],
    "decreasing": ["Whole Milk", "Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Ghee"]
  },
  "Fibrinogen": {
    "increasing": ["Whole Milk", "Cheddar", "Greek Yogurt", "Butter"],
    "decreasing": ["Almond Milk", "Soy Milk", "Mozzarella", "Yogurt", "Ghee"]
  },
}



biochemicals_meats = {
    "Blood Glucose": {
        "increasing": ["Beef","Pork", "Bacon", "Sausage"],
        "decreasing": ["Chicken", "Lamb", "Ham", "Salami", "Pepperoni"]
    },
    "Hemoglobin A1c": {
        "increasing": ["Beef", "Pork", "Bacon", "Sausage"],
        "decreasing": ["Chicken", "Lamb", "Ham", "Salami", "Pepperoni"]
    },
    "Glycated Albumin": {
        "increasing": ["Beef", "Pork", "Bacon", "Sausage"],
        "decreasing": ["Chicken", "Lamb", "Ham", "Salami", "Pepperoni"]
    },
    "Total Cholesterol": {
        "increasing": ["Beef", "Bacon", "Sausage", "Pepperoni"],
        "decreasing": ["Chicken", "Lamb", "Pork", "Ham", "Salami"]
    },
    "LDL Cholesterol": {
        "increasing": ["Beef", "Bacon", "Sausage", "Pepperoni"],
        "decreasing": ["Chicken", "Lamb", "Pork", "Ham", "Salami"]
    },
    "HDL Cholesterol": {
        "increasing": ["Chicken", "Lamb", "Pork", "Ham"],
        "decreasing": ["Beef", "Bacon", "Sausage", "Salami", "Pepperoni"]
    },
    "Triglycerides": {
        "increasing": ["Beef", "Bacon", "Sausage", "Pepperoni"],
        "decreasing": ["Chicken", "Lamb", "Pork", "Ham", "Salami"]
    },
    "Apolipoprotein A1": {
        "increasing": ["Chicken", "Lamb", "Pork", "Ham"],
        "decreasing": ["Beef", "Bacon", "Sausage", "Salami", "Pepperoni"]
    },
    "Apolipoprotein B": {
        "increasing": ["Beef", "Bacon", "Sausage", "Pepperoni"],
        "decreasing": ["Chicken", "Lamb", "Pork", "Ham", "Salami"]
    },
    "Vitamin D": {
        "increasing": ["Chicken", "Beef", "Lamb", "Pork"],
        "decreasing": ["Bacon", "Sausage", "Ham", "Salami", "Pepperoni"]
    },
    "Vitamin C": {
      "increasing": [],
      "decreasing": ["Chicken", "Beef", "Lamb", "Pork", "Bacon", "Sausage", "Ham", "Salami", "Pepperoni"]
    },
    "Vitamin K": {
      "increasing": ["Chicken", "Beef", "Lamb"],
      "decreasing": ["Pork", "Bacon", "Sausage", "Ham", "Salami", "Pepperoni"]
    },
    "Vitamin B6 (Pyridoxine)": {
      "increasing": ["Chicken", "Beef", "Pork"],
      "decreasing": ["Bacon", "Sausage", "Ham", "Salami", "Pepperoni"]
    },
    "Vitamin B1 (Thiamine)": {
      "increasing": ["Pork"],
      "decreasing": ["Chicken", "Beef", "Lamb", "Bacon", "Sausage", "Ham", "Salami", "Pepperoni"]
    },
    "Vitamin B2 (Riboflavin)": {
      "increasing": ["Chicken", "Beef", "Lamb"],
      "decreasing": ["Pork", "Bacon", "Sausage", "Ham", "Salami", "Pepperoni"]
    },
    "Vitamin B3 (Niacin)": {
      "increasing": ["Chicken", "Beef", "Pork", "Bacon"],
      "decreasing": ["Lamb", "Sausage", "Ham", "Salami", "Pepperoni"]
    },
    "Vitamin B5 (Pantothenic Acid)": {
      "increasing": ["Chicken", "Beef", "Pork"],
      "decreasing": ["Lamb", "Bacon", "Sausage", "Ham", "Salami", "Pepperoni"]
    },
    "Vitamin B7 (Biotin)": {
      "increasing": ["Chicken", "Beef", "Pork"],
      "decreasing": ["Lamb", "Bacon", "Sausage", "Ham", "Salami", "Pepperoni"]
    },
    "Vitamin B9 (Folate)": {
      "increasing": ["Chicken", "Beef", "Pork"],
      "decreasing": ["Lamb", "Bacon", "Sausage", "Ham", "Salami", "Pepperoni"]
    },
    "Vitamin B12 (Cobalamin)": {
      "increasing": ["Chicken", "Beef", "Lamb", "Pork"],
      "decreasing": ["Bacon", "Sausage", "Ham", "Salami", "Pepperoni"]
    },
    "Vitamin A": {
      "increasing": ["Chicken", "Beef", "Lamb"],
      "decreasing": ["Pork", "Bacon", "Sausage", "Ham", "Salami", "Pepperoni"]
    },
    "Creatinine": {
      "increasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Ham", "Salami", "Pepperoni"],
      "decreasing": ["Chicken"]
    },
    "Uric Acid": {
      "increasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Ham", "Salami", "Pepperoni"],
      "decreasing": ["Chicken"]
    },
    "Blood Urea Nitrogen": {
      "increasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Ham", "Salami", "Pepperoni"],
      "decreasing": ["Chicken"]
    },
    "Cystatin C": {
      "increasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Ham", "Salami", "Pepperoni"],
      "decreasing": ["Chicken"]
    },
    "Sodium": {
      "increasing": ["Bacon", "Sausage", "Ham", "Salami", "Pepperoni"],
      "decreasing": ["Chicken", "Beef", "Lamb", "Pork"]
    },
    "Potassium": {
      "increasing": ["Chicken", "Beef", "Lamb", "Pork"],
      "decreasing": ["Bacon", "Sausage", "Ham", "Salami", "Pepperoni"]
    },
    "Calcium": {
      "increasing": ["Chicken"],
      "decreasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Ham", "Salami", "Pepperoni"]
    },
    "Magnesium": {
      "increasing": ["Chicken", "Beef", "Lamb"],
      "decreasing": ["Pork", "Bacon", "Sausage", "Ham", "Salami", "Pepperoni"]
    },
    "Phosphate": {
      "increasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Ham", "Salami", "Pepperoni"],
      "decreasing": ["Chicken"]
    },
    "Chloride": {
      "increasing": ["Bacon", "Sausage", "Ham", "Salami", "Pepperoni"],
      "decreasing": ["Chicken", "Beef", "Lamb", "Pork"]
    },
    "Bicarbonate": {
      "increasing": ["Chicken", "Beef", "Lamb"],
      "decreasing": ["Pork", "Bacon", "Sausage", "Ham", "Salami", "Pepperoni"]
    },
    "Iron": {
      "increasing": ["Beef", "Lamb", "Pork", "Chicken"],
      "decreasing": ["Bacon", "Sausage", "Ham", "Salami", "Pepperoni"]
    },
    "Globulin": {
      "increasing": ["Beef", "Lamb", "Pork", "Chicken", "Bacon", "Sausage", "Ham", "Salami", "Pepperoni"],
      "decreasing": []
    },
    "Albumin": {
      "increasing": ["Chicken", "Beef", "Lamb", "Pork", "Ham"],
      "decreasing": ["Bacon", "Sausage", "Salami", "Pepperoni"]
    },
    "Total Protein": {
      "increasing": ["Chicken", "Beef", "Lamb", "Pork", "Bacon", "Sausage", "Ham", "Salami", "Pepperoni"],
      "decreasing": []
    },
    "Albumin/Globulin Ratio": {
      "increasing": ["Chicken", "Ham"],
      "decreasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Salami", "Pepperoni"]
    },
    "C-Reactive Protein": {
      "increasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Salami", "Pepperoni"],
      "decreasing": ["Chicken", "Ham"]
    },
    "Haptoglobin": {
      "increasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Salami", "Pepperoni"],
      "decreasing": ["Chicken", "Ham"]
    },
    "Transferrin": {
      "increasing": ["Beef", "Lamb", "Pork", "Chicken", "Ham"],
      "decreasing": ["Bacon", "Sausage", "Salami", "Pepperoni"]
    },
    "C-Peptide": {
      "increasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Salami", "Pepperoni"],
      "decreasing": ["Chicken", "Ham"]
    },
    "Testosterone": {
      "increasing": ["Beef", "Lamb", "Pork", "Chicken", "Bacon"],
      "decreasing": ["Sausage", "Ham", "Salami", "Pepperoni"]
    },
    "Estrogen": {
      "increasing": ["Bacon", "Sausage", "Salami", "Pepperoni"],
      "decreasing": ["Chicken", "Beef", "Lamb", "Pork", "Ham"]
    },
    "Progesterone": {
      "increasing": ["Beef", "Lamb", "Pork"],
      "decreasing": ["Chicken", "Bacon", "Sausage", "Ham", "Salami", "Pepperoni"]
    },
    "Cortisol": {
      "increasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Salami", "Pepperoni"],
      "decreasing": ["Chicken", "Ham"]
    },
    "Aldosterone": {
      "increasing": ["Bacon", "Sausage", "Ham", "Salami", "Pepperoni"],
      "decreasing": ["Chicken", "Beef", "Lamb", "Pork"]
    },
    "Thyroid-Stimulating Hormone (TSH)": {
      "increasing": ["Bacon", "Sausage", "Salami", "Pepperoni"],
      "decreasing": ["Chicken", "Beef", "Lamb", "Pork", "Ham"]
    },
    "Free Thyroxine (Free T4)": {
      "increasing": ["Chicken", "Beef", "Lamb", "Pork", "Ham"],
      "decreasing": ["Bacon", "Sausage", "Salami", "Pepperoni"]
    },
    "Free Triiodothyronine (Free T3)": {
      "increasing": ["Chicken", "Beef", "Lamb", "Pork", "Ham"],
      "decreasing": ["Bacon", "Sausage", "Salami", "Pepperoni"]
    },
    "Aspartate Aminotransferase": {
      "increasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Salami", "Pepperoni"],
      "decreasing": ["Chicken", "Ham"]
    },
    "Alanine Aminotransferase": {
      "increasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Salami", "Pepperoni"],
      "decreasing": ["Chicken", "Ham"]
    },
    "Alkaline Phosphatase": {
      "increasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Salami", "Pepperoni"],
      "decreasing": ["Chicken", "Ham"]
    },
    "Gamma-Glutamyl Transferase": {
      "increasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Salami", "Pepperoni"],
      "decreasing": ["Chicken", "Ham"]
    },
    "Bilirubin": {
      "increasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Salami", "Pepperoni"],
      "decreasing": ["Chicken", "Ham"]
    },
    "Lactate Dehydrogenase": {
      "increasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Salami", "Pepperoni"],
      "decreasing": ["Chicken", "Ham"]
    },
    "Prothrombin Time": {
      "increasing": ["Chicken", "Ham"],
      "decreasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Salami", "Pepperoni"]
    },
    "Partial Thromboplastin Time": {
      "increasing": ["Chicken", "Ham"],
      "decreasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Salami", "Pepperoni"]
    },
    "Fibrinogen": {
      "increasing": ["Beef", "Lamb", "Pork", "Bacon", "Sausage", "Salami", "Pepperoni"],
      "decreasing": ["Chicken", "Ham"]
    }
}

biochemicals_food_items = {
  "Blood Glucose": {
    "increasing": ["Pastries", "Cookies","Brownies","Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Oatmeal", "French Fries", "Pizza", "Potato Chips", "Popcorn"],
    "decreasing": ["Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos"]
  },
  "Hemoglobin A1c": {
    "increasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Oatmeal", "French Fries", "Pizza", "Potato Chips", "Popcorn"],
    "decreasing": ["Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos"]
  },
  "Glycated Albumin": {
    "increasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Oatmeal", "French Fries", "Pizza", "Potato Chips", "Popcorn"],
    "decreasing": ["Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos"]
  },
  "Total Cholesterol": {
    "increasing": ["Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos", "Pizza", "French Fries"],
    "decreasing": ["Eggs", "Cereals", "Oatmeal", "Guacamole", "Salsa"]
  },
  "LDL Cholesterol": {
    "increasing": ["Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos", "Pizza", "French Fries"],
    "decreasing": ["Eggs", "Cereals", "Oatmeal", "Guacamole", "Salsa"]
  },
  "HDL Cholesterol": {
    "increasing": ["Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "French Fries", "Pizza", "Potato Chips", "Popcorn"]
  },
  "Triglycerides": {
    "increasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "French Fries", "Pizza", "Potato Chips", "Popcorn"],
    "decreasing": ["Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos"]
  },
  "Apolipoprotein A1": {
    "increasing": ["Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "French Fries", "Pizza", "Potato Chips", "Popcorn"]
  },
  "Apolipoprotein B": {
    "increasing": ["Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos", "Pizza", "French Fries"],
    "decreasing": ["Eggs", "Cereals", "Oatmeal", "Guacamole", "Salsa"]
  },
  "Vitamin D": {
    "increasing": ["Ice Cream", "Cereals", "Eggs"],
    "decreasing": ["Coca Cola", "Pepsi", "Coffee", "Tea", "Beer"]
  },
  "Vitamin C": {
    "increasing": ["Lemonade", "Guacamole", "Salsa", "Ketchup"],
    "decreasing": ["Coca Cola", "Pepsi", "Coffee", "Tea", "Beer"]
  },
  "Vitamin K": {
    "increasing": ["Eggs", "Guacamole", "Salsa"],
    "decreasing": ["Coca Cola", "Pepsi", "Coffee", "Tea", "Beer"]
  },
  "Vitamin B6 (Pyridoxine)": {
    "increasing": ["Cereals", "Oatmeal", "Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Coca Cola", "Pepsi", "Coffee", "Tea", "Beer"]
  },
  "Vitamin B1 (Thiamine)": {
    "increasing": ["Cereals", "Oatmeal", "Eggs", "Bread", "Beef Jerky", "Burgers"],
    "decreasing": ["Coca Cola", "Pepsi", "Coffee", "Tea", "Beer"]
  },
  "Vitamin B2 (Riboflavin)": {
    "increasing": ["Cereals", "Oatmeal", "Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets"],
    "decreasing": ["Coca Cola", "Pepsi", "Coffee", "Tea", "Beer"]
  },
  "Vitamin B3 (Niacin)": {
    "increasing": ["Cereals", "Oatmeal", "Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets"],
    "decreasing": ["Coca Cola", "Pepsi", "Coffee", "Tea", "Beer"]
  },
  "Vitamin B5 (Pantothenic Acid)": {
    "increasing": ["Cereals", "Oatmeal", "Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets"],
    "decreasing": ["Coca Cola", "Pepsi", "Coffee", "Tea", "Beer"]
  },
  "Vitamin B7 (Biotin)": {
    "increasing": ["Cereals", "Oatmeal", "Eggs", "Beef Jerky", "Burgers"],
    "decreasing": ["Coca Cola", "Pepsi", "Coffee", "Tea", "Beer"]
  },
  "Vitamin B9 (Folate)": {
    "increasing": ["Cereals", "Oatmeal", "Eggs", "Bread", "Beef Jerky", "Burgers", "Guacamole"],
    "decreasing": ["Coca Cola", "Pepsi", "Coffee", "Tea", "Beer"]
  },
  "Vitamin B12 (Cobalamin)": {
    "increasing": ["Cereals", "Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Coca Cola", "Pepsi", "Coffee", "Tea", "Beer"]
  },
  "Vitamin A": {
    "increasing": ["Eggs", "Cereals", "Ice Cream", "Guacamole", "Salsa"],
    "decreasing": ["Coca Cola", "Pepsi", "Coffee", "Tea", "Beer"]
  },
  "Creatinine": {
    "increasing": ["Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Oatmeal", "Eggs", "Coffee", "Tea", "Lemonade", "Guacamole", "Salsa"]
  },
  "Uric Acid": {
    "increasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Beer", "Beef Jerky", "Burgers", "French Fries", "Pizza", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Oatmeal", "Eggs", "Coffee", "Tea", "Lemonade", "Guacamole", "Salsa"]
  },
  "Blood Urea Nitrogen": {
    "increasing": ["Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos", "Eggs"],
    "decreasing": ["Oatmeal", "Coffee", "Tea", "Lemonade", "Guacamole", "Salsa"]
  },
  "Cystatin C": {
    "increasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer", "Potato Chips", "French Fries", "Pizza"],
    "decreasing": ["Oatmeal", "Eggs", "Coffee", "Tea", "Guacamole", "Salsa"]
  },
  "Sodium": {
    "increasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Potato Chips", "Popcorn", "Crackers", "Beef Jerky", "Burgers", "French Fries", "Pizza", "Chicken Nuggets", "Tacos", "Ketchup", "Mayonnaise"],
    "decreasing": ["Oatmeal", "Eggs", "Coffee", "Tea", "Lemonade", "Guacamole", "Salsa"]
  },
  "Potassium": {
    "increasing": ["Oatmeal", "Eggs", "Coffee", "Tea", "Lemonade", "Guacamole", "Salsa", "Potato Chips", "French Fries", "Tacos"],
    "decreasing": ["Coca Cola", "Pepsi", "Beer"]
  },
  "Calcium": {
    "increasing": ["Ice Cream", "Eggs", "Cereals", "Pizza"],
    "decreasing": ["Coca Cola", "Pepsi", "Coffee", "Beer"]
  },
  "Magnesium": {
    "increasing": ["Oatmeal", "Eggs", "Cereals", "Bread", "Guacamole", "Salsa", "Popcorn", "Beef Jerky"],
    "decreasing": ["Coca Cola", "Pepsi", "Coffee", "Beer", "French Fries"]
  },
  "Phosphate": {
    "increasing": ["Coca Cola", "Pepsi", "Beer", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Oatmeal", "Eggs", "Coffee", "Tea", "Lemonade", "Guacamole", "Salsa"]
  },
  "Chloride": {
    "increasing": ["Potato Chips", "Popcorn", "Crackers", "Beef Jerky", "Burgers", "French Fries", "Pizza", "Chicken Nuggets", "Tacos", "Ketchup", "Mayonnaise"],
    "decreasing": ["Oatmeal", "Eggs", "Coffee", "Tea", "Lemonade", "Guacamole", "Salsa"]
  },
  "Bicarbonate": {
    "increasing": ["Oatmeal", "Eggs", "Coffee", "Tea", "Lemonade", "Guacamole", "Salsa"],
    "decreasing": ["Coca Cola", "Pepsi", "Beer", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos"]
  },
  "Iron": {
    "increasing": ["Cereals", "Oatmeal", "Eggs", "Beef Jerky", "Burgers", "Tacos"],
    "decreasing": ["Coffee", "Tea", "Coca Cola", "Pepsi", "Beer"]
  },
  "Globulin": {
    "increasing": ["Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos", "Oatmeal"],
    "decreasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer", "Potato Chips", "French Fries", "Pizza"]
  },
  "Albumin": {
    "increasing": ["Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos", "Oatmeal"],
    "decreasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer", "Potato Chips", "French Fries", "Pizza"]
  },
  "Total Protein": {
    "increasing": ["Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos", "Oatmeal"],
    "decreasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer", "Potato Chips", "French Fries", "Pizza"]
  },
  "Albumin/Globulin Ratio": {
    "increasing": ["Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer", "Potato Chips", "French Fries", "Pizza"]
  },
  "C-Reactive Protein": {
    "increasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer", "Potato Chips", "French Fries", "Pizza", "Burgers", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Oatmeal", "Eggs", "Coffee", "Tea", "Guacamole", "Salsa"]
  },
  "Haptoglobin": {
    "increasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer", "Potato Chips", "French Fries", "Pizza", "Burgers", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Oatmeal", "Eggs", "Coffee", "Tea", "Guacamole", "Salsa"]
  },
  "Transferrin": {
    "increasing": ["Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos", "Oatmeal"],
    "decreasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer", "Potato Chips", "French Fries", "Pizza"]
  },
  "C-Peptide": {
    "increasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer", "Potato Chips", "French Fries", "Pizza", "Burgers", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Oatmeal", "Eggs", "Coffee", "Tea", "Guacamole", "Salsa"]
  },
  "Testosterone": {
    "increasing": ["Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer"]
  },
  "Estrogen": {
    "increasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Beer"],
    "decreasing": ["Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos", "Coffee", "Tea"]
  },
  "Progesterone": {
    "increasing": ["Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer"]
  },
  "Cortisol": {
    "increasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Coffee", "Beer"],
    "decreasing": ["Oatmeal", "Eggs", "Tea", "Guacamole", "Salsa"]
  },
  "Aldosterone": {
    "increasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer", "Potato Chips", "French Fries", "Pizza", "Burgers", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Oatmeal", "Eggs", "Coffee", "Tea", "Guacamole", "Salsa"]
  },
  "Thyroid-Stimulating Hormone (TSH)": {
    "increasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer"],
    "decreasing": ["Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos", "Coffee", "Tea"]
  },
  "Free Thyroxine (Free T4)": {
    "increasing": ["Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos", "Coffee", "Tea"],
    "decreasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer"]
  },
  "Free Triiodothyronine (Free T3)": {
    "increasing": ["Eggs", "Beef Jerky", "Burgers", "Chicken Nuggets", "Tacos", "Coffee", "Tea"],
    "decreasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer"]
  },
  "Aspartate Aminotransferase": {
    "increasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer", "Potato Chips", "Burgers", "French Fries", "Pizza", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Oatmeal", "Eggs", "Coffee", "Tea", "Lemonade", "Guacamole", "Salsa", "Popcorn", "Crackers", "Beef Jerky"]
  },
  "Alanine Aminotransferase": {
    "increasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer", "Potato Chips", "Burgers", "French Fries", "Pizza", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Oatmeal", "Eggs", "Coffee", "Tea", "Lemonade", "Guacamole", "Salsa", "Popcorn", "Crackers", "Beef Jerky"]
  },
  "Alkaline Phosphatase": {
    "increasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer", "Potato Chips", "Burgers", "French Fries", "Pizza", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Oatmeal", "Eggs", "Coffee", "Tea", "Lemonade", "Guacamole", "Salsa", "Popcorn", "Crackers", "Beef Jerky"]
  },
  "Gamma-Glutamyl Transferase": {
    "increasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer", "Potato Chips", "Burgers", "French Fries", "Pizza", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Oatmeal", "Eggs", "Coffee", "Tea", "Lemonade", "Guacamole", "Salsa", "Popcorn", "Crackers", "Beef Jerky"]
  },
  "Bilirubin": {
    "increasing": ["Beer", "Burgers", "French Fries", "Pizza", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Oatmeal", "Eggs", "Coca Cola", "Pepsi", "Coffee", "Tea", "Lemonade", "Mayonnaise", "Guacamole", "Salsa", "Ketchup", "Potato Chips", "Popcorn", "Crackers", "Beef Jerky"]
  },
  "Lactate Dehydrogenase": {
    "increasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer", "Potato Chips", "Burgers", "French Fries", "Pizza", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Oatmeal", "Eggs", "Coffee", "Tea", "Lemonade", "Guacamole", "Salsa", "Popcorn", "Crackers", "Beef Jerky"]
  },
  "Prothrombin Time": {
    "increasing": ["Beer", "Burgers", "French Fries", "Pizza", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Oatmeal", "Eggs", "Coca Cola", "Pepsi", "Coffee", "Tea", "Lemonade", "Mayonnaise", "Guacamole", "Salsa", "Ketchup", "Potato Chips", "Popcorn", "Crackers", "Beef Jerky"]
  },
  "Partial Thromboplastin Time": {
    "increasing": ["Beer", "Burgers", "French Fries", "Pizza", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Bread", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Oatmeal", "Eggs", "Coca Cola", "Pepsi", "Coffee", "Tea", "Lemonade", "Mayonnaise", "Guacamole", "Salsa", "Ketchup", "Potato Chips", "Popcorn", "Crackers", "Beef Jerky"]
  },
  "Fibrinogen": {
    "increasing": ["Pastries", "Cookies", "Brownies", "Muffins", "Croissants", "Ice Cream", "Pies", "Cakes", "Donuts", "Cereals", "Pancakes", "Waffles", "Coca Cola", "Pepsi", "Beer", "Potato Chips", "Burgers", "French Fries", "Pizza", "Chicken Nuggets", "Tacos"],
    "decreasing": ["Oatmeal", "Eggs", "Coffee", "Tea", "Lemonade", "Guacamole", "Salsa", "Popcorn", "Crackers", "Beef Jerky"]
  }
}



biochemicals_test = {
    "Blood Glucose": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Hemoglobin A1c": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Glycated Albumin": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Total Cholesterol": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "LDL Cholesterol": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "HDL Cholesterol": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Triglycerides": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Apolipoprotein A1": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Apolipoprotein B": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Vitamin D": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Vitamin C": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Vitamin K": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Vitamin B6 (Pyridoxine)": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Vitamin B1 (Thiamine)": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Vitamin B2 (Riboflavin)": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Vitamin B3 (Niacin)": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Vitamin B5 (Pantothenic Acid)": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Vitamin B7 (Biotin)": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Vitamin B9 (Folate)": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Vitamin B12 (Cobalamin)": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Vitamin A": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Creatinine": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Uric Acid": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Blood Urea Nitrogen": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Cystatin C": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Sodium": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Potassium": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Calcium": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Magnesium": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Phosphate": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Chloride": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Bicarbonate": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Iron": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Globulin": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Albumin": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Total Protein": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Albumin/Globulin Ratio": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "C-Reactive Protein": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Haptoglobin": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Transferrin": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "C-Peptide": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Testosterone": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Estrogen": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Progesterone": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Cortisol": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Aldosterone": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Thyroid-Stimulating Hormone (TSH)": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Free Thyroxine (Free T4)": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Free Triiodothyronine (Free T3)": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Aspartate Aminotransferase": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Alanine Aminotransferase": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Alkaline Phosphatase": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Gamma-Glutamyl Transferase": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Bilirubin": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Lactate Dehydrogenase": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Prothrombin Time": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Partial Thromboplastin Time": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
    "Fibrinogen": {
      "increasing" : [], # add all the diary from the diary list i gave that can increase this biochemichal even slighty 
      "decreasing" : [],#add all the diary from the diary list i gave that can decrease this biochemichal even slighty 
    },
}