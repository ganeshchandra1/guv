n=int(input())
k=input()
l=list(k)
dict={}
for i in l:
    if i not in dict.keys():
        dict[i]=l.count(i)
print(min(dict, key=dict.get))
