comprehensive_biochemicals = {
    'Macronutrients': [
        "Glucose", 
        "Glycogen", 
        "Amino Acids", 
        "Triglycerides", 
        "Cholesterol"
    ],
    'Vitamins': [
        "Retinol", 
        "Thiamine", 
        "Riboflavin", 
        "Niacin", 
        "Pantothenic Acid", 
        "Pyridoxine", 
        "Biotin", 
        "Folate", 
        "Cobalamin", 
        "Ascorbic Acid", 
        "Calciferol", 
        "Tocopherols", 
        "Phylloquinone",
        'vitamin_a',
        'vitamin_e',
        'vitamin_k',
        'vitamin_b12',
        'choline'
    ],
    'Minerals': [
        "Calcium", 
        "Ferritin", 
        "Magnesium", 
        "Phosphate", 
        "Potassium", 
        "Sodium", 
        "Zinc", 
        "Copper", 
        "Manganese", 
        "Selenium", 
        "Iodine",
        'iron',
        'tibc',
        'transferrin_saturation',
        'chromium',
        'molybdenum',
        'boron',
        'cobalt',
        'nickel',
        'silicon',
        'vanadium'
    ],
    'Amino Acids': [
        "Alanine", 
        "Arginine", 
        "Asparagine", 
        "Aspartic Acid", 
        "Cysteine", 
        "Glutamic Acid", 
        "Glutamine", 
        "Glycine", 
        "Histidine", 
        "Isoleucine", 
        "Leucine", 
        "Lysine", 
        "Methionine", 
        "Phenylalanine", 
        "Proline", 
        "Serine", 
        "Threonine", 
        "Tryptophan", 
        "Tyrosine", 
        "Valine",
        'arginine',
        'carnitine',
        'taurine'
    ],
    'Fatty Acids': [
        "Saturated Fatty Acids", 
        "Monounsaturated Fatty Acids", 
        "Polyunsaturated Fatty Acids", 
        "Omega-3 Fatty Acids", 
        "Omega-6 Fatty Acids", 
        "Trans Fatty Acids",
        'omega_3_fatty_acids',
        'omega_6_fatty_acids'
    ],
    'Phytochemicals': [
        "Flavonoids", 
        "Carotenoids", 
        "Polyphenols", 
        "Glucosinolates", 
        "Phytosterols"
    ],
    'Sugars': [
        "Glucose", 
        "Fructose", 
        "Sucrose"
    ],
    'Organic Acids': [
        "Citric Acid", 
        "Lactic Acid"
    ],
    'Other': [
        "Fiber", 
        "Antioxidants", 
        "Probiotics", 
        "Prebiotics", 
        "Water", 
        "Alcohol", 
        "Caffeine", 
        "Theobromine", 
        "Tannins", 
        "Lectins", 
        "Phytic Acid", 
        "Oxalates", 
        "Urea", 
        "Creatinine", 
        "Bilirubin", 
        "Ammonia",
        'inositol',
        'coenzyme_q10',
        'glutathione'
    ],
    'Hormones': [
        "Insulin", 
        "Glucagon", 
        "Cortisol", 
        "Thyroid Hormones", 
        "Estrogen", 
        "Testosterone",
        'tsh',
        'free_t4',
        'free_t3',
        'hba1c',
        'fasting_blood_glucose',
        'ogtt',
        'progesterone',
        'prolactin',
        'vitamin_d',
        'vitamin_b12',
        'folate'
    ],
    'Enzymes': [
        "Amylase", 
        "Lipase", 
        "Pepsin", 
        "Trypsin", 
        "Lactase",
        'alkaline_phosphatase',
        'alt',
        'ast'
    ],
    'Coenzymes and Cofactors': [
        "Nicotinamide Adenine Dinucleotide", 
        "Flavin Adenine Dinucleotide", 
        "Coenzyme A"
    ],
    'Antioxidants': [
        "Glutathione", 
        "Uric Acid", 
        "Alpha-Lipoic Acid"
    ],
    'Hematology': [
        'hemoglobin',
        'white_blood_cell_count',
        'platelet_count'
    ],
    'Biochemistry': [
        'calcium',
        'sodium',
        'potassium',
        'chloride',
        'blood_urea_nitrogen',
        'creatinine',
        'albumin',
        'total_protein',
        'bilirubin_total',
        'bilirubin_direct',
        'total_cholesterol',
        'hdl_cholesterol',
        'ldl_cholesterol',
        'triglycerides'
    ],
    'Electrolytes': [
        'sodium',
        'potassium',
        'chloride',
        'blood_urea_nitrogen',
        'creatinine',
        'glomerular_filtration_rate'
    ],
    'Cardiac': [
        'troponin',
        'ck_mb',
        'bnp'
    ],
    'Liver': [
        'bilirubin_total',
        'bilirubin_direct'
    ],
    'Inflammatory': [
        'crp',
        'esr',
        'procalcitonin'
    ],
    'Coagulation': [
        'prothrombin_time',
        'inr',
        'aptt',
        'd_dimer',
        'fibrinogen'
    ],
    'Neurotransmitters': [
        'epo',
        'oxytocin',
        'melatonin',
        'histamine',
        'serotonin',
        'dopamine',
        'norepinephrine',
        'epinephrine',
        'acetylcholine',
        'gaba',
        'glutamate'
    ],
    'Urine': [
        'ph',
        'protein',
        'glucose',
        'ketones',
        'blood',
        'leukocytes',
        'nitrites'
    ]
}

print(f"Total number of biochemical groups listed: {len(comprehensive_biochemicals)}")
print("\nList of Biochemicals by Group:")
for group, biochemicals in comprehensive_biochemicals.items():
    print(f"{group}:")
    for biochemical in biochemicals:
        print(f"  - {biochemical}")
