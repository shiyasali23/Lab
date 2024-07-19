food_categories = {
    "fruit": ([
        "apple", "apricot", "avocado", "banana", "blackberry", "blueberry", "boysenberry", "cantaloupe",
        "cherry", "clementine", "coconut", "cranberry", "date", "dragonfruit", "durian", "elderberry",
        "fig", "gooseberry", "grapefruit", "grape", "guava", "honeydew", "jackfruit", "kiwi", "kumquat",
        "lemon", "lime", "lychee", "mango", "mulberry", "nectarine", "orange", "papaya", "passionfruit",
        "peach", "pear", "persimmon", "pineapple", "plum", "pomegranate", "quince", "raspberry",
        "redcurrant", "starfruit", "strawberry", "tangerine", "watermelon"
    ],),
    "vegetable": [
        "artichoke", "arugula", "asparagus", "beet", "bell_pepper", "bok_choy", "broccoli",
        "brussels_sprout", "cabbage", "carrot", "cauliflower", "celeriac", "celery", "chard", "chayote",
        "collard_greens", "corn", "cucumber", "daikon", "eggplant", "endive", "fennel", "garlic", "ginger",
        "green_bean", "horseradish", "jicama", "kale", "kohlrabi", "leek", "lettuce", "mushroom",
        "mustard_greens", "okra", "onion", "parsnip", "peas", "potato", "pumpkin", "radicchio", "radish",
        "rhubarb", "rutabaga", "scallion", "shallot", "spinach", "squash", "sweet_potato", "tomatillo",
        "tomato", "turnip", "watercress", "yam", "zucchini"
    ],
    "meat": [
        "chicken", "beef", "pork", "lamb", "turkey", "bacon", "sausage", "ham", "salami", "pepperoni"
    ],
    "fish_and_seafood": [
        "salmon", "tuna", "shrimp", "crab", "lobster", "cod", "trout", "tilapia", "haddock", "halibut",
        "mackerel", "sardine", "snapper", "bass", "catfish", "perch", "pollock", "flounder", "grouper",
        "sole", "anchovy", "herring", "mahi_mahi", "clam", "mussel", "octopus", "oyster", "squid", "prawn"
    ],
    "nut_and_seed": [
        "almond", "cashew", "chestnut", "coconut", "hazelnut", "macadamia", "pecan", "pine_nut",
        "pistachio", "walnut", "peanut", "sesame_seed", "sunflower_seed", "chia_seed", "flaxseed",
        "hemp_seed", "poppy_seed", "Brazil_nut", "lotus_seed", "watermelon_seed", "pumpkin_seed",
        "sesame", "cacao_bean", "quinoa", "amaranth", "buckwheat", "safflower_seed", "soybean",
        "canola_seed"
    ],
    "grain": [
        "Wheat", "Rice", "Corn", "Barley", "Oats", "Rye", "Millet", "Sorghum", "Quinoa", "Buckwheat",
        "Amaranth", "Teff", "Spelt", "Farro", "Kamut", "Chia Seeds", "Flaxseed", "Emmer", "Triticale"
    ],
    "dairy": [
        "Milk", "Butter", "Cream", "Ghee", "Buttermilk", "Whey", "Yogurt"
    ],
    "legume_and_pulse": [
        "Black Beans", "Kidney Beans", "Pinto Beans", "Chickpeas", "Lentils", "Green Lentils", "Red Lentils",
        "Brown Lentils", "Yellow Lentils", "Split Peas", "Green Peas", "Black-Eyed Peas", "Fava Beans",
        "Soybeans", "Adzuki Beans", "Cannellini Beans", "Navy Beans", "Great Northern Beans", "Mung Beans",
        "Lima Beans", "Garbanzo Beans", "Cowpeas", "Pigeon Peas", "Lablab Beans", "Bambara Beans",
        "Runner Beans", "Broad Beans"
    ],
    "herbs": [
        "Basil", "Parsley", "Cilantro", "Mint", "Thyme", "Rosemary", "Sage", "Oregano", "Chives", "Dill",
        "Coriander", "Bay Leaf", "Marjoram", "Tarragon", "Lemongrass", "Lavender", "Fennel", "Chervil",
        "Borage", "Savory", "Stevia", "Sorrel", "Lovage", "Rue", "Hyssop"
    ],
    "spice": [
        "Cinnamon", "Turmeric", "Paprika", "Cumin", "Coriander", "Cardamom", "Nutmeg", "Cloves", "Allspice",
        "Ginger", "Garlic", "Chili Powder", "Black Pepper", "White Pepper", "Cayenne Pepper", "Mustard Seed",
        "Fenugreek", "Fennel Seed", "Caraway Seed", "Celery Seed", "Poppy Seed", "Saffron", "Vanilla",
        "Bay Leaf", "Star Anise", "Anise Seed", "Tamarind", "Sesame Seed", "Sumac"
    ]
}


# Biochemicals in edibles
biochemicals_in_edibles = {
    'Macronutrients': [
        "Carbohydrates",
        "Proteins",
        "Fats"
    ],
    'Vitamins': [
        "Vitamin A",
        "Vitamin B1",
        "Vitamin B2",
        "Vitamin B3",
        "Vitamin B5",
        "Vitamin B6",
        "Vitamin B7",
        "Vitamin B9",
        "Vitamin B12",
        "Vitamin C",
        "Vitamin D",
        "Vitamin E",
        "Vitamin K"
    ],
    'Minerals': [
        "Calcium",
        "Iron",
        "Magnesium",
        "Phosphorus",
        "Potassium",
        "Sodium",
        "Zinc",
        "Copper",
        "Manganese",
        "Selenium",
        "Iodine"
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
        "Valine"
    ],
    'Fatty Acids': [
        "Saturated Fatty Acids",
        "Monounsaturated Fatty Acids",
        "Polyunsaturated Fatty Acids",
        "Omega-3 Fatty Acids",
        "Omega-6 Fatty Acids",
        "Trans Fatty Acids"
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
        "Cholesterol",
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
        "Oxalates"
    ]
}