TIP_RATIO = 0.15

bill = float(input('Vad går notan på? ').replace(',', '.'))

tip = bill * TIP_RATIO

print('Dricksa {} kr (betala totalt {} kr)'.format(tip, bill + tip))
