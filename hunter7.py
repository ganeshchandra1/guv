n=int(input())
l=input().split()
for i in range(0,len(l)):
    if(i%2==0):
        if(int(l[i])%2==1):
            print(l[i],end=' ')
    else:
        if(int(l[i])%2==0):
            print(l[i],end=' ')
