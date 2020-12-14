mem = {}
with open('input.txt') as f:
    mask = 'X'*36
    for x in f:
        line = x.strip()
        k, v = line.split(' = ', 1)
        if k == 'mask':
            mask = v
        else:
            addr = int(k[4:-1])
            if addr not in mem.keys():
                mem[addr] = 0
            val = str(bin(int(v)))[2:]
            towrite = list(reversed(val)) + ['0'] * (36-len(val)) 
            for i, m_ in enumerate(reversed(mask)):
                if m_ != 'X':
                    towrite[i] = m_
            towrite = int(''.join(reversed(towrite)),2)
            mem[addr] = towrite

print(sum(mem.values()))