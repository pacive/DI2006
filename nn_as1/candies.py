money = float(input('Hur mycket pengar har du? ').replace(',', '.'))
price = float(input('Hur mycket kostar godiset per styck? ').replace(',', '.'))

number_of_candies = int(money / price)
money_left = money % price

print('Du kan köpa {} godisbitar, och har sedan {:.2f} kr kvar'.format(number_of_candies, money_left))