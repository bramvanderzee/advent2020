ts = 0
busses = []

with open('input_ex.txt') as f:
    _ = int(f.readline().strip())
    busses = [x for x in f.readline().strip().split(',')]
remainders = [int(bus)-i for i,bus in enumerate(busses) if bus != 'x']
print([bus for bus in busses if bus != 'x'])
print(remainders)
#667437230788118
#chinese remainder theory: dcode.fr/chinese-remainder