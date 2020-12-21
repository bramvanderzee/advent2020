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

total = {}
total_missing = set(ingredients)
for k,v in allergens.items():
    ingr = max(set([x for x in v if not x in total.values()]), key = v.count)
    total[k] = ingr
    total_missing.discard(ingr)

total_missing = [x for x in ingredients if x in total_missing]
print(len(total_missing))