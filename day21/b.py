from collections import defaultdict
allergens = defaultdict(lambda: [])
ingredients = []
with open('input.txt') as f:
    for x in f:
        ingr, aller = x.split(' (contains ')
        ingr = [y for y in ingr.split()]
        aller = [y.strip().replace(')','') for y in aller.split(', ')]

        ingredients.extend(ingr)
        for a in aller:
            allergens[a].extend(ingr)

possibles = {}
for k,v in allergens.items():
    most_common = v[0]
    for val in v:
        if v.count(val) > v.count(most_common[0]):
            most_common = [val]
        elif v.count(val) == v.count(most_common[0]) and not val in most_common:
            most_common.append(val)
    possibles[k] = most_common

sorted_possibles = sorted(possibles, key=lambda k: len(possibles[k]))
sorted_possibles = {k:possibles[k] for k in sorted_possibles}
total = {}
for k in list(sorted_possibles.keys()):
    total[k] = sorted_possibles[k][0]
    for v in sorted_possibles.values():
        if total[k] in v:
            v.remove(total[k])
    

sorted_allergens = sorted([k for k in total.keys()])
print(','.join([total[a] for a in sorted_allergens]))