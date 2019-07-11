n=int(input())
l=[]
l2=[]
for i in range(n):
    l.append(input().split())
print(l)
for x in l:
    for y in x:
        l2.append(int(y))
for i in sorted(l2):
    print(i,end=' ')
