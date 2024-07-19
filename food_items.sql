-- Create the Food table
CREATE TABLE Food (
    food_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    food_name VARCHAR(200),
    category VARCHAR(200),
    sub_category VARCHAR(200),
    nutriscore DECIMAL(1),
    quantity DECIMAL(10000,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
);


CREATE TABLE Nutrient (
    nutrients_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    food_id uuid,
    name VARCHAR(200),
    category VARCHAR(200),
    healthy_minimum DECIMAL(10,2),
    healthy_maximum DECIMAL(10,2),
    FOREIGN KEY (food_id) REFERENCES Food(food_id)
);


-- all of the nurtients are stoirng in µg (micrograms)
-- Create the Macronutrients table
CREATE TABLE Macronutrients (
    macronutrient_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    food_id uuid,
    carbohydrates DECIMAL(10,2),
    proteins DECIMAL(10,2),
    fats DECIMAL(10,2),
    FOREIGN KEY (food_id) REFERENCES Food(food_id)
);

-- Create the Vitamins table
CREATE TABLE Vitamins (
    vitamin_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    food_id uuid,
    vitamin_a DECIMAL(10,2),
    vitamin_b1_thiamine DECIMAL(10,2),
    vitamin_b2_riboflavin DECIMAL(10,2),
    vitamin_b3_niacin DECIMAL(10,2),
    vitamin_b5_pantothenic_acid DECIMAL(10,2),
    vitamin_b6_pyridoxine DECIMAL(10,2),
    vitamin_b7_biotin DECIMAL(10,2),
    vitamin_b9_folate DECIMAL(10,2),
    vitamin_b12_cobalamin DECIMAL(10,2),
    vitamin_c_ascorbic_acid DECIMAL(10,2),
    vitamin_d DECIMAL(10,2),
    vitamin_e DECIMAL(10,2),
    vitamin_k DECIMAL(10,2),
    FOREIGN KEY (food_id) REFERENCES Food(food_id)
);

-- Create the Minerals table
CREATE TABLE Minerals (
    mineral_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    food_id uuid,
    calcium DECIMAL(10,2),
    iron DECIMAL(10,2),
    magnesium DECIMAL(10,2),
    phosphorus DECIMAL(10,2),
    potassium DECIMAL(10,2),
    sodium DECIMAL(10,2),
    zinc DECIMAL(10,2),
    copper DECIMAL(10,2),
    manganese DECIMAL(10,2),
    selenium DECIMAL(10,2),
    iodine DECIMAL(10,2),
    FOREIGN KEY (food_id) REFERENCES Food(food_id)
);

-- Create the AminoAcids table
CREATE TABLE AminoAcids (
    amino_acid_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    food_id uuid,
    alanine DECIMAL(10,2),
    arginine DECIMAL(10,2),
    asparagine DECIMAL(10,2),
    aspartic_acid DECIMAL(10,2),
    cysteine DECIMAL(10,2),
    glutamic_acid DECIMAL(10,2),
    glutamine DECIMAL(10,2),
    glycine DECIMAL(10,2),
    histidine DECIMAL(10,2),
    isoleucine DECIMAL(10,2),
    leucine DECIMAL(10,2),
    lysine DECIMAL(10,2),
    methionine DECIMAL(10,2),
    phenylalanine DECIMAL(10,2),
    proline DECIMAL(10,2),
    serine DECIMAL(10,2),
    threonine DECIMAL(10,2),
    tryptophan DECIMAL(10,2),
    tyrosine DECIMAL(10,2),
    valine DECIMAL(10,2),
    FOREIGN KEY (food_id) REFERENCES Food(food_id)
);

-- Create the FattyAcids table
CREATE TABLE FattyAcids (
    fatty_acid_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    food_id uuid,
    saturated_fatty_acids DECIMAL(10,2),
    monounsaturated_fatty_acids DECIMAL(10,2),
    polyunsaturated_fatty_acids DECIMAL(10,2),
    omega_3_fatty_acids DECIMAL(10,2),
    omega_6_fatty_acids DECIMAL(10,2),
    trans_fatty_acids DECIMAL(10,2),
    FOREIGN KEY (food_id) REFERENCES Food(food_id)
);

-- Create the Phytochemicals table
CREATE TABLE Phytochemicals (
    phytochemical_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    food_id uuid,
    flavonoids DECIMAL(10,2),
    carotenoids DECIMAL(10,2),
    polyphenols DECIMAL(10,2),
    glucosinolates DECIMAL(10,2),
    phytosterols DECIMAL(10,2),
    FOREIGN KEY (food_id) REFERENCES Food(food_id)
);

-- Create the OtherBiochemicals table
CREATE TABLE OtherBiochemicals (
    other_biochemicals_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    food_id uuid,
    fiber DECIMAL(10,2),
    cholesterol DECIMAL(10,2),
    antioxidants DECIMAL(10,2),
    probiotics DECIMAL(10,2),
    prebiotics DECIMAL(10,2),
    water DECIMAL(10,2),
    sugars_glucose_fructose_sucrose DECIMAL(10,2),
    organic_acids_citric_acid_lactic_acid DECIMAL(10,2),
    alcohol_ethanol DECIMAL(10,2),
    caffeine DECIMAL(10,2),
    theobromine DECIMAL(10,2),
    tannins DECIMAL(10,2),
    lectins DECIMAL(10,2),
    phytic_acid DECIMAL(10,2),
    oxalates DECIMAL(10,2),
    FOREIGN KEY (food_id) REFERENCES Food(food_id)
);


