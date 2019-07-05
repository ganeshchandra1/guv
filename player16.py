n=int(input())
k=input()
l=list(k)
d={}
for i in l:
    if i not in d.keys():
        d[i]=l.count(i)
print(min(d, key=d.get))
