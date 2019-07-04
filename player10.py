n,k=map(list,input().split())
count=0
if(len(n)==len(k)):
    for i in range(0,len(n)):
        if(n[i]==k[i]):
            continue
        else:
            count=count+1

print(count)
