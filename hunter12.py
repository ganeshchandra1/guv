n,m=map(int,input().split())
k=input().split()
l2=[]
l3=[]
for i in k:
    l2.append(int(i))
l3=sorted(l2)
print(l3[-m])
