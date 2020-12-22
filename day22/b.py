deck1 = []
deck2 = []
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

def calc_points(deck: list) -> int:
    points = 0
    mult = [x + 1 for x in range(len(deck))]
    for mult,card in zip(mult,reversed(deck)):
        points += mult * card
    return points

def play_game(deck1: list, deck2: list):
    seen_configs = []
    playing = True
    while len(deck1) > 0 and len(deck2) > 0 and playing:
        deck1_s = ','.join([str(x) for x in deck1])
        deck2_s = ','.join([str(x) for x in deck2])
        if (deck1_s, deck2_s) in seen_configs:
            playing = False
            return 1, calc_points(deck1)
        else:
            seen_configs.append((deck1_s, deck2_s))

        card_one = deck1.pop(0)
        card_two = deck2.pop(0)

        if len(deck1) >= card_one and len(deck2) >= card_two:
            winner, _ = play_game(deck1[:card_one], deck2[:card_two])
            if winner == 1:
                deck1.append(card_one)
                deck1.append(card_two)
            else:
                deck2.append(card_two)
                deck2.append(card_one)
        elif card_one > card_two:
            deck1.append(card_one)
            deck1.append(card_two)
        elif card_one < card_two:
            deck2.append(card_two)
            deck2.append(card_one)
    winner = 1 if len(deck2) == 0 else 2
    score = calc_points(deck1) if winner == 1 else calc_points(deck2)
    return winner, score

winner, score = play_game(deck1, deck2)

print(winner, score)