manu=int(input())
prashu=list(map(int,input().split()))
for k in prashu:
	if prashu.count(k)==1:
		print(k)
		break
