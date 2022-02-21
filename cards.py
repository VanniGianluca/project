# some exercises about a deck of cards_thought
import random
import itertools

# define the lists needed
cards_thought = []
suits = ('spade', 'coppe', 'denari', 'bastoni')
numbers = (range(1, 11))
decks = []
hand = []


class Card :
    '''class representing a card of a deck'''

    def __init__(self, number, suit) :
        '''initialise card object'''
        suits = ('spade', 'coppe', 'denari', 'bastoni')
        numbers = list(range(1, 11))
        self.number = number
        self.suit = suit
        if self.suit not in suits :
            raise ValueError("Il seme non è valido!")
        if self.number not in numbers :
            raise ValueError("Il seme non è valido!")

    def __str__(self) :
        '''describes better the card'''
        return f'Questa carta è un {self.number} di {self.suit}'

    def describe_card(self) :
        '''describe the card'''
        print(f'Questa carta è un {self.number} di {self.suit}')


def think_random_card() :
    '''generate a random card and append it to cards_thought list'''
    suits = ('spade', 'coppe', 'denari', 'bastoni')
    numbers = list(range(1, 11))
    new_card = Card(random.choice(numbers), random.choice(suits))
    cards_thought.append(new_card)
    print(f'Sto pensando a un {new_card.number} di {new_card.suit}.')


# def cycle(iterable) :
#     # cycle('ABCD') --> A B C D A B C D A B C D ...
#     saved = []
#     for element in iterable :
#         yield element
#         saved.append(element)
#     while saved :
#         for element in saved :
#             yield element


class Deck :
    '''a class representing a deck'''

    def __init__(self, cards_deck=[], c=0) :
        '''initialise deck attributes'''
        self.cards_deck = cards_deck
        self.c = c

    def __str__(self) :
        '''better describe the deck'''
        return f'Questo mazzo ha {len(self.cards_deck)} carte.'

    def shuffle_deck(self) :
        '''shuffle the deck'''
        print('Il mazzo è stato mischiato.')
        self.c = 0
        return random.shuffle(self.cards_deck)

    def first_card(self) :
        #     '''look at the first card in the deck'''
        print(self.cards_deck[0])
        self.c = +1

    def next_card(self) :
        #     '''look at the first card in the deck'''
        print(self.cards_deck[self.c])
        self.c = self.c + 1
        if self.c >= len(self.cards_deck):
            self.c = 0




    # def see_cards(self):
    #     #     '''look at the cards in the deck one after the other'''
    #     i1 = itertools.cycle(self.cards_deck)
    #     c = 1
    #     for a in i1:
    #         print(a)
    #         c+=1
    #         if c==len(self.cards_deck):
    #             break


def create_new_deck() :
    '''create a new dew'''
    new_deck = Deck()
    new_deck.cards_deck = [Card(number, suit) for number in numbers for suit in suits]
    return decks.append(new_deck)
