class Node:
    def __init__(self, data:int, prev=None, nxt=None):
        self.data = data
        self.prev = prev
        self.next = nxt

    def __repr__(self):
        return self.data
    
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.data == other.data
        elif isinstance(other, int):
            return self.data == other
    
    def __add__(self, other):
        if isinstance(other, Node):
            return self.data + other.data
        elif isinstance(other, int):
            return self.data + other
    
    def __sub__(self, other):
        if isinstance(other, Node):
            return self.data - other.data
        elif isinstance(other, int):
            return self.data - other
    
    def get(self):
        return self.data

class LinkedList:
    def __init__(self, data=None):
        self.head = None
        self.first = None
        if not data == None:
            self.head = Node(data.pop(0))
            self.first = self.head
            prev = self.head
            for node in data:
                self.head = Node(node, prev)
                prev.next = self.head
                prev = self.head
            prev.next = self.first

    def __getitem__(self, index):
        self.head = self.first
        for _ in range(index):
            self.head = self.head.next
        return self.head
    
    def __repr__(self):
        nodes = []
        while self.head.next != None:
            nodes.append(str(self.head.data))
            self.head = self.head.next
        return ','.join(nodes)

    def insert(self, index, items):
        prev = self.__getitem__(index-1)
        after = prev.next
        for i in items:
            prev.next = Node(i, prev)
            prev = prev.next
        prev.next = after
    
    def remove(self, item):
        item.prev.next, item.next.prev = item.next, item.prev
    
    def index(self, item):
        index = 0
        while not self.head == item:
            index += 1
            self.head = self.head.next
        return index

CUPS = [] 
with open('input.txt') as f:
    CUPS = [int(x) for x in f.readline().strip()]

from_cup = max(CUPS)+1
CUPS.extend([x+from_cup for x in range(1000000-len(CUPS))])
MIN = min(CUPS)
MAX = max(CUPS)
SIZE = len(CUPS)
CUPS = LinkedList(CUPS)

def do_move(index: int):
    global CUPS
    cur_cup = CUPS[index]
    indices = [(index+x)%SIZE for x in range(1,4)]
    picked = [CUPS[x] for x in indices]
    for cup in picked:
        CUPS.remove(cup)
    dest_cup = cur_cup - 1 if not cur_cup == MIN else MAX
    
    while dest_cup in picked:
        dest_cup -= 1
        if dest_cup < MIN:
            dest_cup = MAX
    
    dest_cup_i = CUPS.index(dest_cup) + 1
    CUPS.insert(dest_cup_i, picked[::-1])

cur_cup_i = 0
for move in range(1, 10000001):
    prev = CUPS[cur_cup_i]
    do_move(cur_cup_i)
    cur_cup_i = (CUPS.index(prev)+1)%SIZE
    if move%10000 == 0:
        print(move)

index1 = CUPS.index(1)
cup1, cup2 = CUPS[(index1+1)%SIZE], CUPS[(index1+2)%SIZE]
ans = cup1 * cup2
print()
print(cup1, cup2)
print(ans)