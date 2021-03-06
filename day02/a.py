def check_password(mi, ma, ch, pwd):
    num = pwd.count(ch)
    if(mi <= num <= ma):
        return True
    else:
        return False

lines = []
with open('input_a.txt') as f:
    for x in f:
        (minimal, temp) = x.strip().split('-', 1)
        (maximal, temp) = temp.split(' ', 1)
        (character, password) = temp.split(': ', 1)
        lines.append((int(minimal), int(maximal), character, password))

count = 0

for x in lines:
    if(check_password(*x)):
        count += 1

print(count)