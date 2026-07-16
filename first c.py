from itertools import combinations
list = [-1,5,7,-8,-9]
print("positive combinations")
for r in range(1,len(list)+1):
    for combo in combinations(list,r):
        if all(num>0 for num in combo):
            print(combo)
