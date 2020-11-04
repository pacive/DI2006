from math import pi

radius = float(input('Radie: ').replace(',', '.'))
degrees = float(input('Grader: ').replace(',', '.'))

full_circle_area = pi * radius ** 2
sector_area = full_circle_area / 360 * degrees

print('Cirkelsektorns area är {}'.format(sector_area))