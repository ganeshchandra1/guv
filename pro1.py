n=int(input())
k=[]
for i in range(n):
    k.append(input())
for i in range(0,len(k)):
    for j in range(i+1,len(k)):
        if k[i] in k[j]:
            print(k[i])
            break
        break
    break
