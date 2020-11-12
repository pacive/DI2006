def is_perfect(num):
    sum_of_factors = 0
    # Calculate sum of numbers that divide num
    for n in range(1, num):
        if num % n == 0:
            sum_of_factors += n

    # Return whether the sum of the factors equals num
    return sum_of_factors == num

number = int(input('Skriv ett tal: '))

if is_perfect(number):
    print(f'{number} är ett perfekt tal')
else:
    print(f'{number} är inte ett perfekt tal')
