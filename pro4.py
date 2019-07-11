n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if(l[i]+l[j]==k):
            print("yes",l[i],l[j])
            break
        else:
            print("no")
        break
    break
