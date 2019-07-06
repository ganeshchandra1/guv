n=str(input())
list1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C']
for i in n:
    if i in list1:
        k=list1.index(i)
        print(list1[k+3],end='')
        
