from itertools import permutations
n=input("")
l=permutations(n)
for i in list(l):
    print("".join(i))
