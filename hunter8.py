n=int(input())
l=input().split()
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            if(int(l[i])+int(l[j])==int(l[k])):
                print(l[i],l[j],l[k])
