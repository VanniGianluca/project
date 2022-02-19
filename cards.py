# some exercises about a deck of cards_thought
import random

cards_thought = []
suits = ('spade', 'coppe', 'denari', 'bastoni')
numbers = (range(1, 11))
decks = []

class Card:
    '''class representing a card of a deck'''
    def __init__(self, number, suit):
        '''initialise card object'''
        suits = ('spade', 'coppe', 'denari', 'bastoni')
        numbers = list(range(1, 11))
        self.number = number
        self.suit = suit
        if self.suit not in suits:
            raise ValueError("Il seme non è valido!")
        if self.number not in numbers:
            raise ValueError("Il seme non è valido!")

    def __str__(self):
        '''describes better the card'''
        return f'Questa carta è un {self.number} di {self.suit}'

    def describe_card(self):
        '''describe the card'''
        print(f'Questa carta è un {self.number} di {self.suit}')

def think_random_card():
    '''generate a random card and append it to cards_thought list'''
    suits = ('spade', 'coppe', 'denari', 'bastoni')
    numbers = list(range(1, 11))
    new_card = Card(random.choice(numbers), random.choice(suits))
    cards_thought.append(new_card)
    print(f'Sto pensando a un {new_card.number} di {new_card.suit}.')

class Deck:
    '''a class representing a deck'''
    def __init__(self, cards_deck=[]):
        '''initialise deck attributes'''
        self.cards_deck = cards_deck

    def __str__(self):
        '''better describe the deck'''
        return f'Questo mazzo ha {len(self.cards_deck)} carte.'

    def shuffle_deck(self):
        print('Il mazzo è stato mischiato.')
        return random.shuffle(self.cards_deck)

    def look_next_card(self):
        self.cards_deck = iter(self.cards_deck)
        return print(next(self.cards_deck, 'Il mazzo è finito.'))


def create_new_deck():
    '''create a new dew'''
    new_deck = Deck()
    new_deck.cards_deck = [Card(number, suit) for number in numbers for suit in suits]
    return decks.append(new_deck)




