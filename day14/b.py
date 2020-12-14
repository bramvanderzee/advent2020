mem = {}
with open('input.txt') as f:
    mask = '0'*36
    for x in f:
        line = x.strip()
        k, v = line.split(' = ', 1)
        if k == 'mask':
            mask = v
        else:
            addr = str(bin(int(k[4:-1])))[2:]
            masked_addr = ['0'] * (36-len(addr)) + list(addr)
            for i, m_ in enumerate(mask):
                if m_ == '1':
                    masked_addr[i] = '1'
                elif m_ == 'X':
                    masked_addr[i] = 'X'

            adresses = []
            for x in range(2**masked_addr.count('X')):
                new_mask = masked_addr.copy()
                sub = ['0']*36 + list(str(bin(x))[2:])
                for i, b in enumerate(new_mask):
                    if b == 'X':
                        new_mask[i] = sub.pop()
                adresses.append(int(''.join(new_mask), 2))


            for a in adresses:
                mem[a] = int(v)
print(sum(mem.values()))