class Game:
    def __init__(self, program: list):
        self.program = program
        self.acc = 0
        self.index = 0
        self.visited = []
        self.finished = False

    def numSteps(self) -> int:
        return len(self.visited)

    def hasNext(self) -> bool:
        if self.index == -1:
            return False
        if self.index == len(self.program):
            print('Gracefully stopped: acc: ' + str(self.acc))
            self.finished = True
            return False
        if self.index < len(self.program):
            return True
        return False

    def readCmd(self, index) -> (str, int):
        if not 0 <= index < len(self.program) - 1:
            if index == len(self.program):
                self.finished = True
            self.index = -1
            return ('nop', 0)
        cmd = self.program[index]
        c, i = cmd.split(' ', 1)
        return (str(c), int(i))

    def prev(self):
        c, i = self.readCmd(self.index)
        try:
            self.visited.remove(self.index)
        except:
            pass
        if c == 'nop':
            self.index -= 1
        elif c == 'acc':
            self.acc -= i
            self.index -= 1
        elif c == 'jmp':
            self.index -= i
        else:
            print('Unknown command: ' + c + i)

    def next(self):
        c, i = self.readCmd(self.index)
        if self.index in self.visited:
            print('Stopping program: ' + str(self.index) + ':' + str(self.visited[-1]))
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

    def swap(self, index):
        c, i = self.readCmd(index)
        if c == 'jmp':
            c = 'nop'
        elif c == 'nop':
            c = 'jmp'
        elif c == 'acc':
            return False
        if i >= 0:
            ins = ' +' + str(i)
        else:
            ins = ' ' + str(i)
        self.program[index] = c + ins
        print(self.program)

    def nextSwp(self):
        c, i = self.readCmd(self.index)
        if self.index in self.visited:
            print('Stopping program: exit code -1')
            print('At index: ' + str(self.index))
            print('Prev index: ' + str(self.visited[-1]))
            self.index = -1
            return
        else:
            self.visited.append(self.index)
        if c == 'jmp':
            self.index += 1
        elif c == 'acc':
            self.acc += i
            self.index += 1
        elif c == 'nop':
            self.index += i
        else:
            print('Unknown command: ' + c + i)

    def getAcc(self) -> int:
        return self.acc

    def hasFinished(self) -> bool:
        return self.finished

lines = []
with open('input_ex.txt') as f:
    for x in f:
        lines.append(x.strip())

finished = False
indexToSwap = -1
while not finished:
    indexToSwap += 1
    if indexToSwap == len(lines):
        break
    game = Game(lines.copy())
    if not game.swap(indexToSwap):
        continue
    while game.hasNext():
        game.next()
    finished = game.hasFinished()
    if finished:
        print(game.getAcc())

