n=int(input())
k=input()
l=list(k)
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if(l[i]==l[j]):
            print(l[i])
            break
    break
