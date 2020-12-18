import Game

lines = []
with open('input_working.txt') as f:
    for x in f:
        lines.append(x.strip())

game = Game.Game(lines)
while game.has_next():
    game.next()

print(game.has_finished())
print(game.get_acc())