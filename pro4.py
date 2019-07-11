n,k=map(int,input().split())
l=list(map(int,input().split()))
l1=[]
for i in range(0,len(l)):
    for j in range(i,len(l)):
        if(l[i]+l[j]==k):
            l1.append("yes")
            break
        else:
            l1.append("no")
            break
        break
if "yes" in l1:
    print("yes")
else:
    print("no")
