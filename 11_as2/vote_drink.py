VOTING_AGE = 18
DRINKING_AGE = 21

def count_above(array, lower_limit):
    count = 0
    for number in array:
        if number >= lower_limit:
            count += 1
    return count

ages = []

while True:
    user_input = input('Skriv in en ålder (eller q för att avsluta): ')
    if user_input == 'q':
        break
    ages.append(int(user_input))
    
print('{} av personerna får rösta'.format(count_above(ages, VOTING_AGE)))
print('{} av personerna får dricka'.format(count_above(ages, DRINKING_AGE)))
