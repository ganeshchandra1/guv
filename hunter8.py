n=int(input())
l=input().split()
for i in l:
    for j in l:
        if(j>i):
            for k in l:
                if(k>j):
                    if(int(i)+int(j)==int(k)):
                        print(i+" "+j+" "+k)
