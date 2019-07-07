n=int(input())
k=input()
l=list(k)
di={}
for i in l:
    if i not in di.keys():
        di[i]=l.count(i)
print(min(di, key=di.get))
