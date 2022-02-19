from cards import *

print(f'Adesso penserò a 3 carte...')
think_random_card()
think_random_card()
think_random_card()

print(f'Ora creerò un mazzo...')
create_new_deck()
print(f'{decks[0]}')
print(f'Ora elencherò le prime 10 carte del mazzo...')
for a in range(10):
    decks[0].look_next_card()
print(f'Ora elencherò le prossime 20 carte del mazzo...')
for a in range(20):
    decks[0].look_next_card()
print(f'Ora elencherò le ultime 10 carte del mazzo...')
for a in range(10):
    decks[0].look_next_card()
decks[0].look_next_card()
print(f'Ora mischierò il mazzo...')
decks[0].shuffle_deck()
print(f'Ora guarderò la prossima carta del mazzo...')
decks[0].look_next_card()