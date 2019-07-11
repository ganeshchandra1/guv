n,m=map(int,input().split())
l=[]
l2=[]
for i in range(n):
        l.append(input())
for i in l:
    l2.append(i.count('1'))
if 0 in l2:
    l2.remove(0)
for i in range(min(l2)):
    for j in range(min(l2)-1):
        print(1,end=' ')
    print(end='1\n')
