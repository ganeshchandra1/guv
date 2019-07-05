n,k=map(int,input().split())
list1=[]
for i in range(max(n,k),max(n,k)+1):
    if(i%n==0 and i%k==0):
        print(i)
