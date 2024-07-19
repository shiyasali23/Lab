CREATE TABLE Users (
    user_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    gender VARCHAR(10),
    date_of_birth DATE,
    age INT,
    email_address VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Address (
    address_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid,
    address VARCHAR(255),
    city VARCHAR(100),
    country VARCHAR(100),
    postal_code VARCHAR(20),
    phone_number VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE VitalSigns (
    vital_sign_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid,
    body_temperature DECIMAL(4,1),
    heart_rate INT,
    blood_pressure_systolic INT,
    blood_pressure_diastolic INT,
    respiratory_rate INT,
    oxygen_saturation DECIMAL(4,1),
    blood_glucose_level DECIMAL(5,2),
    weight DECIMAL(5,2),
    height DECIMAL(5,2),
    body_mass_index DECIMAL(4,1),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE ActivityMonitoring (
    activity_monitoring_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid,
    steps_taken INT,
    distance_walked DECIMAL(5,2),
    calories_burned INT,
    active_minutes INT,
    sleep_duration DECIMAL(4,2),
    sleep_quality DECIMAL(4,2),
    exercise_type VARCHAR(50),
    exercise_duration DECIMAL(4,2),
    exercise_intensity VARCHAR(50),
    water_intake DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Exercise (
    exercise_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID,
    exercise_type VARCHAR(50),
    exercise_duration DECIMAL(4,2),
    exercise_intensity INT,
    calories_burned INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE GeneralActivityMonitoring (
    activity_monitoring_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID,
    sleep_duration DECIMAL(4,2),
    sleep_quality INT,
    water_intake DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE HealthEvents (
    health_event_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid,
    date_of_event DATE,
    type_of_event VARCHAR(50),
    event_description TEXT,
    severity DECIMAL(3,2),
    duration_in_minutes DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Report (
    report_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid,
    report_provider_name VARCHAR(100),
    description TEXT,
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE MedicationAdherence (
    medication_adherence_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid,
    medical_history_id UUID,
    medication_name VARCHAR(100),
    dosage_in_mg DECIMAL(5,2),
    medication_type VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (medical_history_id) REFERENCES Report(report_id)
);

CREATE TABLE MentalHealthMonitoring (
    mental_health_monitoring_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid,
    mood DECIMAL(5,2),
    stress_level DECIMAL(5,2),
    anxiety_level DECIMAL(5,2),
    depression_level DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Hematology (
    hematology_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid,
    hemoglobin DECIMAL(10,2),
    white_blood_cell_count DECIMAL(10,2),
    platelet_count DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Biochemistry (
    biochemistry_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid,
    glucose DECIMAL(10,2),
    calcium DECIMAL(10,2),
    sodium DECIMAL(10,2),
    potassium DECIMAL(10,2),
    chloride DECIMAL(10,2),
    blood_urea_nitrogen DECIMAL(10,2),
    creatinine DECIMAL(10,2),
    albumin DECIMAL(10,2),
    total_protein DECIMAL(10,2),
    alkaline_phosphatase DECIMAL(10,2),
    alt DECIMAL(10,2),
    ast DECIMAL(10,2),
    bilirubin_total DECIMAL(10,2),
    bilirubin_direct DECIMAL(10,2),
    total_cholesterol DECIMAL(10,2),
    hdl_cholesterol DECIMAL(10,2),
    ldl_cholesterol DECIMAL(10,2),
    triglycerides DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Endocrine (
    endocrine_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid,
    tsh DECIMAL(10,2),
    free_t4 DECIMAL(10,2),
    free_t3 DECIMAL(10,2),
    hba1c DECIMAL(10,2),
    fasting_blood_glucose DECIMAL(10,2),
    ogtt DECIMAL(10,2),
    estrogen DECIMAL(10,2),
    progesterone DECIMAL(10,2),
    testosterone DECIMAL(10,2),
    cortisol DECIMAL(10,2),
    prolactin DECIMAL(10,2),
    vitamin_d DECIMAL(10,2),
    vitamin_b12 DECIMAL(10,2),
    folate DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Electrolytes (
    electrolytes_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid,
    sodium DECIMAL(10,2),
    potassium DECIMAL(10,2),
    chloride DECIMAL(10,2),
    blood_urea_nitrogen DECIMAL(10,2),
    creatinine DECIMAL(10,2),
    glomerular_filtration_rate DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Cardiac (
    cardiac_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid,
    troponin DECIMAL(10,2),
    ck_mb DECIMAL(10,2),
    bnp DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Liver (
    liver_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid,
    alt DECIMAL(10,2),
    ast DECIMAL(10,2),
    alkaline_phosphatase DECIMAL(10,2),
    bilirubin_total DECIMAL(10,2),
    bilirubin_direct DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Inflammatory (
    inflammatory_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid,
    crp DECIMAL(10,2),
    esr DECIMAL(10,2),
    procalcitonin DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Coagulation (
    coagulation_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid,
    prothrombin_time DECIMAL(10,2),
    inr DECIMAL(10,2),
    aptt DECIMAL(10,2),
    d_dimer DECIMAL(10,2),
    fibrinogen DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Nutritional (
    nutritional_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid,
    iron DECIMAL(10,2),
    ferritin DECIMAL(10,2),
    tibc DECIMAL(10,2),
    transferrin_saturation DECIMAL(10,2),
    magnesium DECIMAL(10,2),
    zinc DECIMAL(10,2),
    copper DECIMAL(10,2),
    manganese DECIMAL(10,2),
    phosphorus DECIMAL(10,2),
    selenium DECIMAL(10,2),
    iodine DECIMAL(10,2),
    molybdenum DECIMAL(10,2),
    boron DECIMAL(10,2),
    chromium DECIMAL(10,2),
    cobalt DECIMAL(10,2),
    nickel DECIMAL(10,2),
    silicon DECIMAL(10,2),
    vanadium DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Neurotransmitters (
    neurotransmitters_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid,
    epo DECIMAL(10,2),
    oxytocin DECIMAL(10,2),
    melatonin DECIMAL(10,2),
    histamine DECIMAL(10,2),
    serotonin DECIMAL(10,2),
    dopamine DECIMAL(10,2),
    norepinephrine DECIMAL(10,2),
    epinephrine DECIMAL(10,2),
    acetylcholine DECIMAL(10,2),
    gaba DECIMAL(10,2),
    glutamate DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Vitamins (
    vitamins_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid,
    vitamin_a DECIMAL(10,2),
    vitamin_e DECIMAL(10,2),
    vitamin_k DECIMAL(10,2),
    vitamin_b12 DECIMAL(10,2),
    omega_3_fatty_acids DECIMAL(10,2),
    omega_6_fatty_acids DECIMAL(10,2),
    arginine DECIMAL(10,2),
    carnitine DECIMAL(10,2),
    coenzyme_q10 DECIMAL(10,2),
    glutathione DECIMAL(10,2),
    inositol DECIMAL(10,2),
    taurine DECIMAL(10,2),
    choline DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Urine (
    urine_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid,
    ph DECIMAL(10,2),
    protein DECIMAL(10,2),
    glucose DECIMAL(10,2),
    ketones DECIMAL(10,2),
    blood DECIMAL(10,2),
    leukocytes DECIMAL(10,2),
    nitrites DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

------FoodItems-------------


CREATE TABLE Macronutrients (
    macro_nutrient_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    food_item_id uuid,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    calories DECIMAL(10,2),
    carbohydrates DECIMAL(10,2),
    protein DECIMAL(10,2),
    fat DECIMAL(10,2),
    fiber DECIMAL(10,2),
    FOREIGN KEY (food_item_id) REFERENCES FoodItem(food_item_id)
);

CREATE TABLE FoodVitamins (
    food_vitamin_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    food_item_id uuid,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    vitamin_a DECIMAL(10,2),
    vitamin_c DECIMAL(10,2),
    vitamin_d DECIMAL(10,2),
    vitamin_e DECIMAL(10,2),
    vitamin_k DECIMAL(10,2),
    thiamin DECIMAL(10,2),
    riboflavin DECIMAL(10,2),
    niacin DECIMAL(10,2),
    vitamin_b6 DECIMAL(10,2),
    folate DECIMAL(10,2),
    vitamin_b12 DECIMAL(10,2),
    pantothenic_acid DECIMAL(10,2),
    biotin DECIMAL(10,2),
    FOREIGN KEY (food_item_id) REFERENCES FoodItem(food_item_id)
);

CREATE TABLE Minerals (
    mineral_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    food_item_id uuid,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    calcium DECIMAL(10,2),
    iron DECIMAL(10,2),
    sodium DECIMAL(10,2),
    potassium DECIMAL(10,2),
    magnesium DECIMAL(10,2),
    zinc DECIMAL(10,2),
    copper DECIMAL(10,2),
    selenium DECIMAL(10,2),
    manganese DECIMAL(10,2),
    phosphorus DECIMAL(10,2),
    total_sugars DECIMAL(10,2),
    water_content DECIMAL(10,2),
    FOREIGN KEY (food_item_id) REFERENCES FoodItem(food_item_id)
);

CREATE TABLE FattyAcids (
    fatty_acid_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    food_item_id uuid,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    omega_3_ala DECIMAL(10,2),
    omega_3_epa DECIMAL(10,2),
    omega_3_dha DECIMAL(10,2),
    omega_6 DECIMAL(10,2),
    monounsaturated_fats DECIMAL(10,2),
    polyunsaturated_fats DECIMAL(10,2),
    trans_fats DECIMAL(10,2),
    cholesterol DECIMAL(10,2),
    FOREIGN KEY (food_item_id) REFERENCES FoodItem(food_item_id)
);
