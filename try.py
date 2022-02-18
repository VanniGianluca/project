import cards
from cards import *
asso_di_bastoni = Card(1, 'bastoni')
# due_di_denari = Card(4, 'pillola')
asso_di_bastoni.describe_card()
# due_di_denari.describe_card()

think_random_card()
think_random_card()
think_random_card()
print(cards_though[0])
print(cards_though[2])

create_new_deck()
print(decks[0])
print(decks[0].cards_deck[0])
print(decks[0].cards_deck[1])