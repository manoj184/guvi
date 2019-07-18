manu=int(input())
prashu=list(map(int,input().split()))
flag=0
rrr=[]
for i in range(0,manu):
	if(prashu[i]==i):
		temp=prashu[i]
		flag=1
		rrr.append(temp)
		rrr=sorted(rrr)
print(*rrr)
if(flag==0):
	print(-1)
