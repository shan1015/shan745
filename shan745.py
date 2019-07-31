n,k=map(int,input().split())
a=0
l=list(map(int,input().split()))
for i in range(0,len(l)):
	if l[i]==k:
		a=a+1
print(a)
