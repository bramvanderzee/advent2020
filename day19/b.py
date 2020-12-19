import re
rules = True
R = {}
messages = []
with open('input.txt') as f:
    for x in f:
        x = x.strip()
        if x == '':
            rules = False
            continue
        if rules:
            n, r = x.split(': ')
            R[int(n)] = r
        else:
            messages.append(x)

def parse_regex(rules: dict, rule: str, depth: int) -> str:
    regex_rule = ''
    depth += 1
    if depth > 30:
        return regex_rule
    if rule.count('"') > 0:
        return rule.replace('"', '')
    elif rule.count('|') == 0:
        indices = [int(x) for x in rule.split()]
        for i in indices:
            regex_rule += parse_regex(rules, rules[i], depth)
        return regex_rule
    else:
        a, b = rule.split(' | ', 1)
        a = parse_regex(rules, a, depth)
        b = parse_regex(rules, b, depth)
        regex_rule += '(' + a + '|' + b + ')'
        return regex_rule

R[8] = '42 | 42 8'
R[11] = '42 31 | 42 11 31'
rules_regex = {k:parse_regex(R, v, 0) for k,v in R.items()}

ans = 0
for line in messages:
    if re.match('^' + rules_regex[0] + '$', line):
        ans += 1

print(ans)
