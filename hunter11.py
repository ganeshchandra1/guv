l1=list(input().split())
for i in l1:
    print(''.join(sorted(i,reverse=True)),end=' ')
