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

def parse_regex(rules: dict, rule: str) -> str:
    regex_rule = ''
    if rule.count('"') > 0:
        return rule.replace('"', '')
    elif rule.count('|') == 0:
        indices = [int(x) for x in rule.split()]
        for i in indices:
            regex_rule += parse_regex(rules, rules[i])
        return regex_rule
    else:
        a, b = rule.split(' | ', 1)
        a = parse_regex(rules, a)
        b = parse_regex(rules, b)
        regex_rule += '(' + a + '|' + b + ')'
        return regex_rule

rules_regex = {k:parse_regex(R, v) for k,v in R.items()}

ans = 0
for line in messages:
    if re.match('^' + rules_regex[0] + '$', line):
        ans += 1

print(ans)