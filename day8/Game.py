class Game:
    def __init__(self, program: list):
        self.program = program.copy()
        self.acc = 0
        self.pointer = 0
        self.visited = []
        self.finished = False

    def has_next(self) -> bool:
        if self.pointer == -1:
            return False
        if self.pointer == len(self.program):
            print('Gracefully stopped: acc: ' + str(self.acc))
            self.finished = True
            return False
        if self.pointer < len(self.program):
            return True
        return False

    def read_cmd(self, index):
        if not 0 <= index < len(self.program):
            self.pointer = -1
            return ('stop', 0)
        cmd = self.program[index]
        c, i = cmd.split(' ', 1)
        return (str(c), int(i))

    def next(self):
        c, i = self.read_cmd(self.pointer)
        if self.pointer in self.visited:
            print('Stopping program: ' + str(self.pointer) + ':' + str(self.visited[-1]))
            self.pointer = -1
        else:
            self.visited.append(self.pointer)
            if c == 'nop':
                self.pointer += 1
            elif c == 'acc':
                self.acc += i
                self.pointer += 1
            elif c == 'jmp':
                self.pointer += i
            else:
                print('Unknown command: ', c, i)

    def swap(self, index):
        c, i = self.read_cmd(index)
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
        return True

    def get_acc(self) -> int:
        return self.acc

    def has_finished(self) -> bool:
        return self.finished