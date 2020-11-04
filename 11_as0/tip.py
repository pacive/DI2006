bill = float(input('Vad går notan på? ').replace(',', '.'))

tip = bill * 0.15

print('Dricksa {} kr (betala totalt {} kr)'.format(tip, bill + tip))
