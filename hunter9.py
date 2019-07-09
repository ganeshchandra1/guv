n=int(input())
l=input().split()
dic=dict()
target=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        dic.update({l[i]+" "+l[j]:int(l[i])+int(l[j])})
d=dict(sorted(dic.items(), key=lambda x: x[1]))
for i,j in d.items():
    if(j==0):
        print(i)
        break
    else:
        key, value = min(d.items(), key=lambda kv : abs(kv[1] - target))
        print(key)
        break

