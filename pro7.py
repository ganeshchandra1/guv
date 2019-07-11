k = int(input())
l = list(map(int, input().split()))
n = int(len(l)/2)
if sum(l[:n])//len(l[:n]) == sum(l[n:])//len(l[n:]):
    print('yes')
else:
    print('no')
