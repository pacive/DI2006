def is_perfect(num):
    sum_of_factors = 0
    # Calculate sum of numbers that divide num
    for i in range(1, num):
        if num % i == 0:
            sum_of_factors += i

    # Return whether the sum of the factors equals num
    return sum_of_factors == num

number = int(input('Skriv ett tal: '))

if is_perfect(number):
    print('{} är ett perfekt tal'.format(number))
else:
    print('{} är inte ett perfekt tal'.format(number))
