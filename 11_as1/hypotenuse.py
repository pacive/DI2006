import math

a = float(input('Längd katet 1: ').replace(',', '.'))
b = float(input('Längd katet 2: ').replace(',', '.'))

c = math.sqrt(a**2 + b**2)

print(f'Hypotenusan är {c}')