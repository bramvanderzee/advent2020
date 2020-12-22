from collections import deque
deck1 = deque()
deck2 = deque()
first_deck = True
with open('input.txt') as f:
    for x in f:
        x = x.strip()
        if first_deck:
            if x.endswith(' 1:'):
                continue
            if x == '':
                continue
            if x.endswith(' 2:'):
                first_deck = False
                continue
            deck1.append(int(x))
            continue
        deck2.append(int(x))

def calc_points(deck: deque) -> int:
    points = 0
    mult = [x + 1 for x in range(len(deck))]
    for mult,card in zip(mult,reversed(deck)):
        points += mult * card
    return points

while len(deck1) > 0 and len(deck2) > 0:
    card_one = deck1.popleft()
    card_two = deck2.popleft()
    if card_one > card_two:
        deck1.append(card_one)
        deck1.append(card_two)
    else:
        deck2.append(card_two)
        deck2.append(card_one)

if len(deck1) == 0:
    print('Player 2 won with:', calc_points(deck2))
elif len(deck2) == 0:
    print('Player 1 won with:', calc_points(deck1))