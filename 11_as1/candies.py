money = float(input('Hur mycket pengar har du? ').replace(',', '.'))
price = float(input('Hur mycket kostar godiset per styck? ').replace(',', '.'))

number_of_candies = int(money / price)
money_left = money % price

print(f'Du kan köpa {number_of_candies} godisbitar, och har sedan {money_left:.2f} kr kvar')
