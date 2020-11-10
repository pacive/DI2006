from math import pi

radius = float(input('Hur stor radie har banan? ').replace(',', '.'))
length = float(input('Hur långt har du sprungit? ').replace(',', '.'))

circumference = 2 * radius * pi
laps = length / circumference

print(f'Du har sprungit {laps} varv')