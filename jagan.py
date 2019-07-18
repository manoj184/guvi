manu=list(map(str,input()))
prashu=p1=0
for k in range(0,len(manu)-1):
  r=manu[k]
  if int(r)!=0:
   for t in range(k+1,k+2):
    r=r+manu[t]
    if int(r)<27 and int(r)>0: prashu=prashu+1
    elif int(r)==0: prashu=prashu-1
    else: break
if prashu!=1: p1=prashu%2
print(prashu+p1+1)
