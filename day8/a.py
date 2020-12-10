class Game:
    def __init__(self, program: list):
        self.program = program
        self.acc = 0
        self.index = 0
        self.visited = []

    def hasNext(self) -> bool:
        if self.index == -1:
            print('Stopping program: exit code -1')
            return False
        if self.index <= len(self.program):
            return True
        return False

    def readCmd(self, cmd) -> (str, int):
        c, i = cmd.split(' ', 1)
        return (str(c), int(i))

    def next(self):
        c, i = self.readCmd(self.program[self.index])
        if self.index in self.visited:
            self.index = -1
            return
        else:
            self.visited.append(self.index)
        if c == 'nop':
            self.index += 1
        elif c == 'acc':
            self.acc += i
            self.index += 1
        elif c == 'jmp':
            self.index += i
        else:
            print('Unknown command: ' + c + i)

    def getAcc(self) -> int:
        return self.acc

lines = []
with open('input_a.txt') as f:
    for x in f:
        lines.append(x.strip())

game = Game(lines)
while(game.hasNext()):
    game.next()

print(game.getAcc())
