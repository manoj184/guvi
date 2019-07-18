manoj=int(input())
manju=list(map(int,input().split()))
prashu=[]
for k in manju:
	if(manju.count(k)>=2 and k not in prashu):
		prashu.append(k)
if(len(prashu)==0):
	print("unique")
else:
	for k in prashu:
		print(k,end="")
