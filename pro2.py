n,q=map(int,input().split())
l=list(map(int,input().split()))
lis=[]
li=[]
for i in range(q):
    lis=input().split()
    li.append(sum(l[int(lis[0])-1:int(lis[1])]))
for i in li:
    print(i,end='\n')
