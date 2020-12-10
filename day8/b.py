import Game

lines = []
with open('input_a.txt') as f:
    for x in f:
        lines.append(x.strip())

finished = False
indexToSwap = -1
while not finished:
    indexToSwap += 1
    if indexToSwap == len(lines):
        break
    game = Game.Game(lines)
    if not game.swap(indexToSwap):
        continue
    while game.has_next():
        game.next()

    finished = game.has_finished()
