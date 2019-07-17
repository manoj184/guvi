m,p=map(int,input().split())
for i in range (m+1,p):
    for j in range(2,i):
        if (i%j==0):
            break
    else:
        print(i, end=' ')
