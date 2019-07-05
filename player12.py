n,k=map(int,input().split())
e=list(input().split())
print(' '.join(e[-k:]+e[:-k]))
