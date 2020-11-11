# Define a dictionary of the price factors you can select
PRICE_FACTORS = { '1': 0.9, '2': 0.95, '3': 1, '4': 1.2 }

price = float(input('Ange pris: ').replace(',', '.'))

print('''
Välj betalningssätt:
1. Kontant
2. Kort
3. 2 månaders avbetalning
4. 3 månaders avbetalning
''')

plan = input()
# Check that the selection is valid
while plan not in PRICE_FACTORS:
    plan = input('Ogiltigt val, försök igen: ')

final_price = price * PRICE_FACTORS[plan]

print(f'Du behöver betala totalt {final_price:.2f} kr')
