n=str(input())
d={}

for i in n:
    if i not in d.keys():
        d[i]=n.count(i)
print(max(d, key=d.get))
