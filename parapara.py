manu,prashu=map(int,input().split())
count=0
for k in range(manu,prashu+1):
  if k>1:

    for p in range(2,k):
      if k%p==0:
        break
    else:
      count=count+1
print(count)
