expenses = []
with open('input_a.txt') as f:
    for x in f:
        expenses.append(int(x))

for e1 in expenses:
    for e2 in expenses:
        for e3 in expenses:
            if e1 + e2 + e3 == 2020:
                print(e1*e2*e3)
                break