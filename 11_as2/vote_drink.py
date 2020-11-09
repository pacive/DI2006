VOTING_AGE = 18
DRINKING_AGE = 21

# Function to count the number of elements in an array of numbers that are higher than 
# or equal to lower_limit
def count_higher(array, lower_limit):
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
    try:
        ages.append(int(user_input))
    except:
        print('Ogiltigt värde')

print('{} av personerna får rösta'.format(count_higher(ages, VOTING_AGE)))
print('{} av personerna får dricka'.format(count_higher(ages, DRINKING_AGE)))
