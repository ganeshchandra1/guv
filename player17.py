n,k=map(int,input().split())
for i in range(max(n,k),100000):
    if(i%n==0 and i%k==0):
        print(i)
        break
