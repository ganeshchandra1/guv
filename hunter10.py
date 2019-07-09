n,m=map(int,input().split())
l1=list(input().split())
l2=list(input().split())
if set(l1) <= set(l2):
    print("YES")
else:
    print("NO")
