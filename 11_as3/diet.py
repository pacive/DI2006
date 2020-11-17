'''Program that uses various body measurements to calculate fitness level,
and recommends nutrient intake and examples of food that satisfies the recommendations'''
import math
import random

# Constants for gender
MALE = 'M'
FEMALE = 'F'

# Constants for diffetent nutrients
PROTEIN = 'protein'
CARBOHYDRATES = 'carbohydrates'
FAT = 'fat'

# Different categories related to body fat
ESSENTIAL = 'Essential fat'
ATHLETE = 'Athlete'
FITNESS = 'Fitness'
ACCEPTABLE = 'Acceptable'
OVERWEIGHT = 'Overweight'

# Calories per gram of the different nutrients
CALORIE_CONTENT = { PROTEIN: 4, CARBOHYDRATES: 4, FAT: 9 }

# Factors for calculating maintenance calories, based on level of activity on
# on a scale from 1-5
ACTIVITY_LEVEL_FACTOR = { 1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9 }

# Recommended percentage of calories from different nutrients
PERCENT_CALORIE_INTAKE = { PROTEIN: 0.4, CARBOHYDRATES: 0.3, FAT: 0.3 }

# Example food, with how many percent of the weight constitutes nutrients
EXAMPLE_FOOD = {
    PROTEIN: [
        ( 'Chicken breast', 0.21 )
    ],
    CARBOHYDRATES: [
        ( 'Sweet potato', 0.2 )
    ],
    FAT: [
        ( 'Olive oil', 1 )
    ]
}

class FitnessProfile():
    '''Class for calculating various measurements related to fitness and diet'''
    def __init__(self, gender, activity_level, height, weight, neck, waist, hip=None):
        self.gender = gender
        self.activity_level = activity_level
        self.height = height
        self.weight = weight
        self.neck = neck
        self.waist = waist
        if gender == FEMALE and hip is None:
            raise ValueError('Hip measurement must be included')

        self.hip = hip

    def fat_percent(self):
        '''Calculates the fat percent dependant on gender and different measurements'''
        if self.gender == MALE:
            return 495 / (1.0324 - 0.19077*math.log10(self.waist-self.neck) + 0.15456*math.log10(self.height)) - 450

        return 495 / (1.29579 - 0.35004*math.log10(self.waist+self.hip-self.neck) + 0.221*math.log10(self.height)) - 450

    def body_fat_category(self):
        '''Use fat percent to assign different categories'''
        body_fat_percent = self.fat_percent()
        if self.gender == FEMALE:
            if body_fat_percent < 14:
                return ESSENTIAL
            if body_fat_percent <= 20:
                return ATHLETE
            if body_fat_percent <= 24:
                return FITNESS
            if body_fat_percent <= 31:
                return ACCEPTABLE
        else:
            if body_fat_percent < 6:
                return ESSENTIAL
            if body_fat_percent <= 13:
                return ATHLETE
            if body_fat_percent <= 17:
                return FITNESS
            if body_fat_percent <= 24:
                return ACCEPTABLE

        return OVERWEIGHT


    def base_metabolic_rate(self):
        '''Calculates base metabolic rate'''
        return 370 + 21.6 * (1 - (self.fat_percent() / 100)) * self.weight

    def maintenance_calories(self):
        '''Use base metabolic rate and activity level to calculate maintenance calories per day'''
        return self.base_metabolic_rate() * ACTIVITY_LEVEL_FACTOR[self.activity_level]

    def adjusted_maintenance_calories(self):
        '''Adjust number of calories if person's body fat category is ESSENTIAL or OVERWEIGHT'''
        category = self.body_fat_category()
        calories = self.maintenance_calories()
        if category == ESSENTIAL:
            return calories * 1.15
        if category == OVERWEIGHT:
            return calories * 0.85

        return calories

    def recommended_intake(self, nutrient):
        '''Calculates recommended intake of specified nutrient'''
        calories_from_nutrient = self.adjusted_maintenance_calories() * PERCENT_CALORIE_INTAKE[nutrient]
        return calories_from_nutrient / CALORIE_CONTENT[nutrient]

    def example_food(self, nutrient):
        '''Gives an example of food that satisfies the recommended intake'''
        food_source = EXAMPLE_FOOD[nutrient][random.randint(0, len(EXAMPLE_FOOD[nutrient]) - 1)]
        food_amount = self.recommended_intake(nutrient) / food_source[1]
        return (food_source[0], food_amount)

profile = FitnessProfile(gender=MALE, activity_level=2, height=180, weight=80, neck=39, waist=98)

print(profile.fat_percent())
print(profile.body_fat_category())
print(profile.base_metabolic_rate())
print(profile.maintenance_calories())
print(profile.adjusted_maintenance_calories())
print(profile.recommended_intake(PROTEIN))
print(profile.recommended_intake(CARBOHYDRATES))
print(profile.recommended_intake(FAT))
print(profile.example_food(PROTEIN))
print(profile.example_food(CARBOHYDRATES))
print(profile.example_food(FAT))
