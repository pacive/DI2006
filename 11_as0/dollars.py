EXCHANGE_RATE = 0.11

sek = float(input('Hur mycket pengar har du? ').replace(',', '.'))

dollars = sek * EXCHANGE_RATE

print('Du kan köpa ${:.2f}'.format(dollars))
