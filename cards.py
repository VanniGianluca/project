# some exercises about a deck of cards_thought
import random

# define the lists needed
cards_thought = []
suits = ('spade', 'coppe', 'denari', 'bastoni')
numbers = (range(1, 11))
decks = []
hand = []


class Card:
    """class representing a card of a deck"""

    def __init__(self, number, suit):
        """initialise card object"""
        # noinspection PyShadowingNames
        suits = ('spade', 'coppe', 'denari', 'bastoni')
        # noinspection PyShadowingNames
        numbers = list(range(1, 11))
        self.number = number
        self.suit = suit
        if self.suit not in suits:
            raise ValueError("Il seme non è valido!")
        if self.number not in numbers:
            raise ValueError("Il seme non è valido!")

    def __str__(self):
        """describes better the card"""
        return f'Questa carta è un {self.number} di {self.suit}'

    def describe_card(self):
        """describe the card"""
        print(f'Questa carta è un {self.number} di {self.suit}')


def think_random_card():
    """generate a random card and append it to cards_thought list"""
    # noinspection PyShadowingNames
    suits = ('spade', 'coppe', 'denari', 'bastoni')
    # noinspection PyShadowingNames
    numbers = list(range(1, 11))
    new_card = Card(random.choice(numbers), random.choice(suits))
    cards_thought.append(new_card)
    print(f'Sto pensando a un {new_card.number} di {new_card.suit}.')


class Deck:
    """a class representing a deck"""

    def __init__(self, cards_deck=None):
        """initialise deck attributes"""
        if cards_deck is None:
            cards_deck = []
        self.cards_deck = cards_deck

    def __str__(self):
        """better describe the deck"""
        return f'Questo mazzo ha {len(self.cards_deck)} carte.'

    def shuffle_deck(self):
        """shuffle the deck"""
        print('Il mazzo è stato mischiato.')
        return random.shuffle(self.cards_deck)

    def first_card(self):
        """look at the first card in the deck"""
        print(self.cards_deck[0])

    def last_card(self):
        """look at the last card of the deck"""
        print(self.cards_deck[-1])

    def see_cards(self):
        """look at all the cards of the deck"""
        for card in self.cards_deck:
            print(card)

    def first_last(self):
        add = self.cards_deck.pop(0)
        self.cards_deck.append(add)
        print(f"Adesso la prima carta è l'ultima!")

    def first_x_cards(self, x):
        """look at the first X card in the deck"""
        for a in range(x):
            print(self.cards_deck[a])

    def last_x_cards(self, y):
        """look at the first X card in the deck"""
        for a in range(-1, -y-1, -1):
            print(self.cards_deck[a])


def create_new_deck():
    """create a new deck"""
    new_deck = Deck()
    new_deck.cards_deck = [Card(number, suit) for number in numbers for suit in suits]
    return decks.append(new_deck)
