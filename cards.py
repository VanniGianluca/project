# some exercises about a deck of cards
import random
# from collections import namedtuple
cards = []

class Card:
    '''class representing a card of a deck'''
    # # Card = namedtuple('Card', ['number', 'suit'])

    def __str__(self):
        '''describes better the card'''
        return f'Questa carta è un {self.number} di {self.suit}'

    def __init__(self, number, suit):
        '''initialise card object'''
        suits = ['spade', 'coppe', 'denari', 'bastoni']
        numbers = list(range(1, 11))
        self.number = number
        self.suit = suit
        if self.suit not in suits:
            raise ValueError("Il seme non è valido!")
        if self.number not in numbers:
            raise ValueError("Il seme non è valido!")

    def describe_card(self):
        '''describe the card'''
        print(f'Questa carta è un {self.number} di {self.suit}')


def generate_random_card():
    '''generate a random card and append it to cards list'''
    suits = ['spade', 'coppe', 'denari', 'bastoni']
    numbers = list(range(1, 11))
    new_card = Card(random.choice(numbers), random.choice(suits))
    cards.append(new_card)
    print(f'Il programma ha generato un {new_card.number} di {new_card.suit}.')
# you can see a random card of the deck
# you can divide the deck into smaller decks
# you can put individual cards in other decks
# you can put random cards into other decks
# you can shuffle decks


