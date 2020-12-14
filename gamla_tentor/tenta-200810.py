# Uppgift 1 a)
'''
pengar = int(input('Ange hur mycket pengar: '))
rest = pengar
antal_hundralappar = rest // 100
rest = rest % 100
antal_femtiolappar = rest // 50
rest = rest % 50
antal_tjugolappar = rest // 20
rest = rest % 20
antal_enkronor = rest
print(pengar, 'kronor motsvarar', antal_hundralappar,
    'hundralappar,', antal_femtiolappar,
    'femtiolappar,', antal_tjugolappar,
    'tjugolappar och', antal_enkronor, 'enkronor')
'''
# Uppgift 1 b)
'''
((4 > 2) or (1.0 == 1.0))
((4 > 2) or (1.0 < 1.0))
((4 > 2) or (1.0 > 1.0))
((4 > 2) or (1.0 <= 1.0))
((4 > 2) or (1.0 >= 1.0))
((4 > 2) or (1.0 != 1.0))
((4 >= 2) or (1.0 == 1.0))
((4 >= 2) or (1.0 < 1.0))
((4 >= 2) or (1.0 > 1.0))
((4 >= 2) or (1.0 <= 1.0))
((4 >= 2) or (1.0 >= 1.0))
((4 >= 2) or (1.0 != 1.0))
((4 != 2) or (1.0 == 1.0))
((4 != 2) or (1.0 < 1.0))
((4 != 2) or (1.0 > 1.0))
((4 != 2) or (1.0 <= 1.0))
((4 != 2) or (1.0 >= 1.0))
((4 != 2) or (1.0 != 1.0))
((4 < 2) or (1.0 == 1.0))
((4 < 2) or (1.0 <= 1.0))
((4 < 2) or (1.0 >= 1.0))
((4 <= 2) or (1.0 == 1.0))
((4 <= 2) or (1.0 <= 1.0))
((4 <= 2) or (1.0 >= 1.0))
((4 == 2) or (1.0 == 1.0))
((4 == 2) or (1.0 <= 1.0))
((4 == 2) or (1.0 >= 1.0))
'''

# Uppgift 2 a)
'''
x = int(input('Ange x: '))
y = sum(range(x**2))
print(y)
'''

# Uppgift 2 b)
'''
tal = int(input('Ange tal: '))
for x in range(1, tal + 1):
    for y in range(x, tal + 1):
        for z in range(y, tal + 1):
            if x**2 + y**2 == z**2:
                print(f'( {x} , {y} , {z} )')
'''

# Uppgift 3 a)
'''
def foo_bar(string):
    string2 = ''
    ending = ''
    for i in range(len(string)):
        if string[i] in ('a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö'):
            string2 += string[i]
            ending += string[i]
        else:
            string2 += string[i] + string[i]

    return string2 + ending
'''
# Uppgift 3 b)
# i) Samma som värdet på var
# ii) Värden som är > 1 eller < -1
# iii) Första gången bar() anropas med ett negativt tal returneras ett positivt,
#      därefter kommer loopen i foo() fortsätta med positiva värden
# iv)
'''
def bar(value):
    return value * (value - 1)

def foo(value):
    if value in range(-1, 2):
        return value

    while True:
        if value > 10:
            break
        else:
            value += bar(value)
    return value
'''

# Uppgift 4
# a) foo() öppnar en fil som specificeras i arg1 och skriver arg2 rader med 1:or, med lika många 1:or som
#    radens nummer (första raden räknas som 0, så den är tom)
#    bar() anropar först foo() med samma argument, därefter öppnar den samma fil för läsning och räknar
#    det totala antalet 1:or i filen, samt returnerar det värdet
# b) Då kommer även radbrytningen (\n) räknas med i längden på raden
# c) 6

# Uppgift 5
# a) Både foo() och bar() returnerar en dictionary med de bokstäver som förekommer både i string1 och string2 som nycklar,
#    och det sammanlagda antalet av dessa bostäver i string 1 och string2 som värden.
# b) {'h': 4, 'e': 4, 'j': 4, ' ': 3} två gånger. (ordningen  i den andra kan variera eftersom set inte garanterar ordning)

# Uppgift 6
'''
import math

class Ball:
    def __init__(self, radius):
        self.radius = radius

    def compute_volume(self):
        return (4 * math.pi * self.radius**3) / 3

    def __str__(self):
        return 'Bollen har volymen: ' + str(self.compute_volume())

boll = Ball(1)
print(boll)
'''

# Uppgift 7 a)
'''
class KeyValue:
    def __init__(self, key, value):
        self.__key = key
        self.__value = int(value)

    def set_key(self, key):
        self.__key = key

    def set_value(self, value):
        self.__value = value

    def get_key(self):
        return self.__key

    def get_value(self):
        return self.__value

    def __str__(self):
        return f'{{{self.__key}: {self.__value}}}'

    def __repr__(self):
        return str(self)
'''
# Uppgift 7 b)
'''
import random

def generate_map(string):
    letters = set(string)
    keyvalue_list = []
    for letter in letters:
        rnd = random.randint(100, 999)
        while rnd in [kv.get_value() for kv in keyvalue_list]:
            rnd = random.randint(100, 999)
        keyvalue_list.append(KeyValue(letter, rnd))
    return keyvalue_list

print(generate_map('hej hej'))
'''

# Uppgift 8
class Deck:
    VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
    SUITES = ('Clubs', 'Spades', 'Hearts', 'Diamonds')
    def __init__(self):
        self.__deck = set()
        self.reset()

    def reset(self):
        for suite in Deck.SUITES:
            for value in Deck.VALUES:
                self.__deck.add((value, suite))

    def remove_card(self, card):
        if self.has_card(card):
            self.__deck.remove(card)

    def add_card(self, card):
        if Deck.is_valid_card(card):
            self.__deck.add(card)

    def has_card(self, card):
        return card in self.__deck

    def draw_random(self):
        if len(self.__deck) > 0:
            return self.__deck.pop()
        return None

    def __str__(self):
        return f'Deck of {len(self.__deck)} cards'

    @staticmethod
    def is_valid_card(card):
        return card is not None and \
            len(card) == 2 and \
            card[0] in Deck.VALUES and \
            card[1] in Deck.SUITES

    @staticmethod
    def card_repr(card):
        if Deck.is_valid_card(card):
            return f'{card[0]} of {card[1]}'
        return None

    @staticmethod
    def compare_pairs(pair1, pair2):
        if Deck.compare_cards(*pair1) == 0:
            if Deck.compare_cards(*pair2) == 0:
                return Deck.compare_cards(pair1[0], pair2[0])
            return 1
        if Deck.compare_cards(*pair2) == 0:
            return -1

        p1_sorted = sorted(pair1, key=lambda c: Deck.VALUES.index(c[0]))
        p2_sorted = sorted(pair2, key=lambda c: Deck.VALUES.index(c[0]))

        return Deck.compare_cards(p1_sorted[1], p2_sorted[1]) or Deck.compare_cards(p1_sorted[0], p2_sorted[0])

    @staticmethod
    def compare_cards(card1, card2):
        c1_index = Deck.VALUES.index(card1[0])
        c2_index = Deck.VALUES.index(card2[0])
        if c1_index > c2_index:
            return 1
        elif c1_index < c2_index:
            return -1
        return 0

deck = Deck()
pair1 = (deck.draw_random(), deck.draw_random())
pair2 = (deck.draw_random(), deck.draw_random())
result = Deck.compare_pairs(pair1, pair2)
if result == 1:
    print(f'{tuple(map(Deck.card_repr, pair1))} beats {tuple(map(Deck.card_repr, pair2))}')
elif result == -1:
    print(f'{tuple(map(Deck.card_repr, pair2))} beats {tuple(map(Deck.card_repr, pair1))}')
else:
    print(f'{tuple(map(Deck.card_repr, pair1))} and {tuple(map(Deck.card_repr, pair2))} have the same value')
